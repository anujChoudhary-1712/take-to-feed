# Edit and render real footage

Use Whisper for timing, then build the edit in Remotion or HyperFrames. Reuse the project's existing renderer and versioned dependencies. For a new project, choose Remotion for reusable React compositions or HyperFrames for HTML/CSS scenes.

## 1. Transcribe the originals

From the reel folder, run the Whisper CLI with FFmpeg available. Use a distinct filename for each take. If the project already uses faster-whisper, reuse it and export the same `segments[].words[]` shape with `word`, `start`, and `end` in seconds.

```sh
mkdir -p sources exports
whisper raw/take-01.mp4 --word_timestamps True --output_format json --output_dir sources
```

Listen through the opening and proof beats. Correct product names and misheard words in the transcript. Check suggested cuts against the waveform and footage. Cut pauses and retakes where the sentence still sounds natural. Keep screen captures separate from the talking-head audio and align them with the line they illustrate.

[Whisper CLI source](https://github.com/openai/whisper/blob/main/whisper/transcribe.py) · [faster-whisper word timestamps](https://github.com/SYSTRAN/faster-whisper#word-level-timestamps)

## 2. Retiming after the rough cut

Copy [cuts.json](../assets/starter/cuts.json) into the reel folder and replace its sample entries. List the primary audio cuts in playback order. Use integer milliseconds measured from the original media, with paths relative to `cuts.json`. Silent B-roll stays in the visual edit plan. Each cut follows the last immediately at normal speed.

```sh
python "$SKILL_DIR/scripts/retime_words.py" cuts.json captions-timed.json
```

The helper emits output duration and word cues with `text`, `startMs`, and `endMs`. Group the cues into readable phrases when styling captions. If the edit includes speed changes, gaps, overlap, or replaced narration, get timings from that actual timeline or transcribe the exported rough cut. Re-run the timing step after changes.

## 3. Build and render

**Remotion.** Use the project's vertical composition. For a new project, follow the official starter and register a vertical composition. Pass the edit data as props your composition explicitly reads. Derive clip placement and composition duration from the cut list, trim media at source offsets, and place subtitle groups on the output timeline. Quantize the cuts and captions to the same FPS. Resolve footage paths through the project's media loader or public assets. Review the timing and layout in Studio before exporting.

```sh
npx remotion studio
npx remotion render src/index.ts Reel exports/reel-v1.mp4 --props=render-props.json
```

Use the entry point and composition ID registered by your project. The props file is the adapter between the cut/caption files and your composition's API. [Remotion starter](https://www.remotion.dev/docs/cli/create-video) · [Render CLI](https://www.remotion.dev/docs/cli/render)

**HyperFrames.** Use an existing HTML composition or scaffold one with `npx hyperframes init my-video`. In the composition, set the vertical dimensions and scene durations. Place clips and caption groups using output times in seconds. Check the generated HTML with the CLI and preview the proof beat and caption transitions before exporting.

```sh
npx hyperframes lint
npx hyperframes check
npx hyperframes render --output exports/reel-v1.mp4
```

Run from the HyperFrames project root and create the export directory there. [HyperFrames CLI](https://github.com/heygen-com/hyperframes/blob/main/docs/developers/cli.mdx) · [Composition skill](https://github.com/heygen-com/hyperframes/tree/main/skills/hyperframes)

## 4. Check the actual MP4

Play the opening, every cut around speech, and the final line. Check that the proof appears with the corresponding spoken claim, captions stay clear of platform controls, and music leaves the voice intelligible. Deliver the MP4 with the edit plan and post caption. If tools or footage are missing, deliver the edit plan with the missing input or failed step identified.
