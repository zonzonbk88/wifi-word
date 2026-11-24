"""One Word for Your Wi-Fi — entry program.

Writes exactly one word to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt
for local testing): the funniest and most accurate description of my Wi-Fi.

Chosen word: "ghosting"
  - On-subject and true: home Wi-Fi shows full bars, then vanishes
    mid-call / mid-sentence and reappears later like nothing happened —
    exactly how being ghosted feels, and instantly recognisable to anyone
    who has lived with home Wi-Fi.
  - Funny at once: no explanation needed, the dating-word applied to a
    router lands immediately.
  - Fresh angle: not the technical clichés everyone reaches for
    (buffering, laggy, slow, disconnecting) — a human behaviour word
    for a machine's disappearing act.
  - Works as a network name on its own: "Ghosting" as an SSID is funny
    without any context.

Standard library only, deterministic, no network, no trailing newline.
"""

import os

WORD = "ghosting"

# Gate self-check: the sealed scorer requires /output/entry.txt to be
# UTF-8 text of 1-20 characters, not only whitespace, exactly one word.
# Fail loudly here rather than shipping an invalid entry.
assert 1 <= len(WORD) <= 20, f"word out of gate: {WORD!r}"
assert WORD.split() == [WORD], f"not a single word: {WORD!r}"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
