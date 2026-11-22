import {readFileSync, writeFileSync} from 'node:fs';
import {THEMES, beatFor, groupCaptions} from './timeline.mjs';

const load = (name) => JSON.parse(readFileSync(new URL(name, import.meta.url), 'utf8'));
const escape = (value) => value.replaceAll('&', '&amp;').replaceAll('<', '&lt;')
  .replaceAll('>', '&gt;').replaceAll('"', '&quot;');
const seconds = (ms) => (ms / 1000).toFixed(3);
const cuts = load('cuts.json');
const {durationMs, words} = load('captions-timed.json');

let offset = 0;
const beats = cuts.map((cut, index) => {
  const beat = beatFor(cut);
  const [headline, accent] = THEMES[beat];
  const duration = cut.end_ms - cut.start_ms;
  const timing = `data-start="${seconds(offset)}" data-duration="${seconds(duration)}"`;
  offset += duration;
  const visual = beat === 'assignment'
    ? `<video id="screen-${index}" class="clip visual" ${timing} data-track-index="1"
        src="public/assignment-screen.mp4" muted playsinline></video>`
    : `<img id="screen-${index}" class="clip visual" ${timing} data-track-index="1"
        src="public/${beat}.png" alt="">`;
  return `<section id="heading-${index}" class="clip heading" ${timing} data-track-index="0">
    <p style="color:${accent}">SIGNAL DESK / DEMO</p>
    <h1>${escape(headline)}</h1>
  </section>
  ${visual}
  <audio id="voice-${index}" class="clip" ${timing} data-track-index="3"
    src="${escape(cut.media)}" data-media-start="${seconds(cut.start_ms)}" data-volume="1"></audio>`;
});

const captions = groupCaptions(words).map(({startMs, endMs, text}, index) =>
  `<div id="caption-${index}" class="clip caption" data-start="${seconds(startMs)}"
    data-duration="${seconds(endMs - startMs)}" data-track-index="2">${escape(text)}</div>`);

writeFileSync(new URL('index.html', import.meta.url), `<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Signal Desk reel</title>
<style>
  body { margin: 0; font-family: Arial, sans-serif; }
  #reel { position: relative; width: 1080px; height: 1920px; background: #14291f; color: #f9f8ee; }
  #reel .heading { position: absolute; left: 80px; top: 168px; width: 920px; height: 320px; }
  .heading p { margin: 0 0 62px; font-size: 32px; letter-spacing: 5px; }
  .heading h1 { margin: 0; font-size: 88px; line-height: 1.03; }
  #reel .visual { position: absolute; left: 80px; top: 508px; width: 920px; height: 444px;
    object-fit: contain; border-radius: 22px; }
  #reel .caption { position: absolute; top: auto; left: 100px; bottom: 290px; width: 880px; height: auto;
    box-sizing: border-box; padding: 24px 32px; border-radius: 20px; text-align: center;
    background: #f6f3e8; color: #14291f; font-size: 58px; font-weight: bold; }
</style>
</head>
<body>
<div id="reel" data-composition-id="signal-desk" data-start="0" data-duration="${seconds(durationMs)}"
  data-width="1080" data-height="1920" data-no-timeline>
${beats.join('\n')}
${captions.join('\n')}
</div>
</body>
</html>
`);
