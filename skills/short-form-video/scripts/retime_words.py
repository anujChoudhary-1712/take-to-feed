"""Map Whisper word timings onto a sequence of hard cuts."""

import argparse
import json
from pathlib import Path


def retime(cuts, project):
    transcripts = {}
    output_words = []
    output_start = 0
    for cut in cuts:
        start = cut["start_ms"]
        end = cut["end_ms"]
        if type(start) is not int or type(end) is not int or not 0 <= start < end:
            raise ValueError("Each cut needs integer times with 0 <= start_ms < end_ms.")
        transcript = project / cut["transcript"]
        if transcript not in transcripts:
            data = json.loads(transcript.read_text(encoding="utf-8"))
            transcripts[transcript] = [
                word for segment in data["segments"] for word in segment["words"]
            ]

        for word in transcripts[transcript]:
            word_start = max(start, round(word["start"] * 1000))
            word_end = min(end, round(word["end"] * 1000))
            if word_start < word_end:
                output_words.append({
                    "text": word["word"],
                    "startMs": output_start + word_start - start,
                    "endMs": output_start + word_end - start,
                })
        output_start += end - start

    return {"durationMs": output_start, "words": output_words}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("cuts", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    try:
        cuts = json.loads(args.cuts.read_text(encoding="utf-8"))
        if not isinstance(cuts, list) or not cuts:
            raise ValueError("The cut list must be a nonempty JSON array.")
        result = retime(cuts, args.cuts.parent)
        args.output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    except (KeyError, TypeError, ValueError, OSError) as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
