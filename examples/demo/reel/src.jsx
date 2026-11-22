import React from 'react';
import {
  AbsoluteFill, Audio, Composition, Img, OffthreadVideo, Sequence,
  registerRoot, staticFile, useCurrentFrame,
} from 'remotion';
import {THEMES, beatFor, groupCaptions} from './timeline.mjs';
import cuts from './cuts.json';
import timedCaptions from './captions-timed.json';

const FPS = 30;
const frameAt = (milliseconds) => Math.round(milliseconds * FPS / 1000);
const asset = (path) => staticFile(path.replace(/^public\//, ''));
const IMAGE_STYLE = {width: '100%', display: 'block', borderRadius: 22};
const captions = groupCaptions(timedCaptions.words);

function Shot({cut, beat}) {
  const [headline, accent] = THEMES[beat];
  return (
    <AbsoluteFill style={{padding: '168px 80px', background: '#14291f', color: '#f9f8ee',
      fontFamily: 'Arial, sans-serif'}}>
      <Audio src={asset(cut.media)} startFrom={frameAt(cut.start_ms)} />
      <div style={{fontSize: 32, letterSpacing: 5, color: accent}}>SIGNAL DESK / DEMO</div>
      <div style={{fontSize: 88, fontWeight: 700, lineHeight: 1.03, margin: '76px 0 52px'}}>
        {headline}
      </div>
      {beat === 'assignment'
        ? <OffthreadVideo src={staticFile('assignment-screen.mp4')} muted style={IMAGE_STYLE} />
        : <Img src={staticFile(`${beat}.png`)} style={IMAGE_STYLE} />}
    </AbsoluteFill>
  );
}

function Reel() {
  const now = useCurrentFrame() * 1000 / FPS;
  const caption = captions.find(({startMs, endMs}) => startMs <= now && now < endMs);
  let offset = 0;
  const scenes = cuts.map((cut) => {
    const from = frameAt(offset);
    offset += cut.end_ms - cut.start_ms;
    const beat = beatFor(cut);
    return <Sequence key={from} from={from} durationInFrames={frameAt(offset) - from}>
      <Shot cut={cut} beat={beat} />
    </Sequence>;
  });

  return (
    <AbsoluteFill>
      {scenes}
      {caption && <div style={{position: 'absolute', bottom: 290, left: 100, right: 100,
        padding: '24px 32px', borderRadius: 20, textAlign: 'center', background: '#f6f3e8',
        color: '#14291f', fontFamily: 'Arial, sans-serif', fontSize: 58, fontWeight: 700}}>
        {caption.text}
      </div>}
    </AbsoluteFill>
  );
}

function Root() {
  return <Composition id="SignalDeskReel" component={Reel}
    durationInFrames={frameAt(timedCaptions.durationMs)} fps={FPS} width={1080} height={1920} />;
}

registerRoot(Root);
