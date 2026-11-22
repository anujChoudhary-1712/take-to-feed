# Signal Desk reel

This 15-second vertical video uses the [selected hook](../hooks.md) and the same three product states as the [carousel](../deck.json). The footage is a fictional screen capture simulated from a screenshot. The narration was generated with eSpeak NG. The checked-in [word timings](sources) came from faster-whisper and were corrected for wording and punctuation.

| Output time | Narration and visual |
| --- | --- |
| 0:00–0:05.897 | “Give every edit note a home.” Show the note at 12:40 in the episode. |
| 0:05.897–0:09.612 | Select the exact range and assign it to Leah. Show the assignment screen capture. |
| 0:09.612–0:14.581 | Mark the note resolved and show that the timestamp remains visible. |

**Cover copy:** Give every edit note a home

**Post caption:** Give each podcast edit note a timestamp, an owner, and a resolution. Here’s a three-step walkthrough in a fictional review tool.

## Rebuild with Remotion

From this folder, use Python 3 and Node.js with npm. The bundled source files let you render without transcribing again.

```sh
npm ci
python3 ../../../skills/short-form-video/scripts/retime_words.py cuts.json captions-timed.json
npm run render
```

The first render can download Chrome Headless Shell. [cuts.json](cuts.json) orders the source narration clips; [captions-timed.json](captions-timed.json) puts their word timings on the output timeline. If you change a cut, regenerate the timed captions before rendering. The composition is specific to this example's three shots. Use [the editing guide](../../../skills/short-form-video/references/editing-stack.md) to adapt the workflow to your own footage.

[Finished Remotion MP4](reel.mp4)

## Rebuild with HyperFrames

Use the same word timings and media to render the HTML composition. From this folder, run the following with Node.js and FFmpeg available.

```sh
python3 ../../../skills/short-form-video/scripts/retime_words.py cuts.json captions-timed.json
node build-hyperframes.mjs
npx --yes hyperframes@0.9.80 lint
npx --yes hyperframes@0.9.80 render --output reel-hyperframes.mp4
```

The build script regenerates [index.html](index.html). Both renderers use the same headline and caption grouping rules in [timeline.mjs](timeline.mjs).

[Finished HyperFrames MP4](reel-hyperframes.mp4)
