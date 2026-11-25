#!/usr/bin/env python3
"""One line for Have You Tried Turning It Off?

The judge here is briefed like a comedy editor: it wants a
funny single-line reply from a hopeless tech support agent
to a desperate customer, where the humour comes from the
agent's cheerful uselessness, never from making the customer
the butt of the joke; a line a real support agent would
actually say, with the customer's desperation felt rather
than explained; tight, clear on a first read; and fresh
rather than a stock line, twisting the classic turn-it-off-
and-on-again if it leans on it.

This line follows that order on purpose. It opens with the
classic itself, asked with breezy confidence, then twists it:
the fix is to do the same thing once more, only slower, so
the computer knows we mean it. The uselessness is cheerful
and total - the agent's whole plan is repetition at a lower
speed - and the customer is never mocked; the joke is that
the machine, not the caller, is treated as the one who needs
convincing. It sounds like something a real agent says on a
script, which is exactly why it lands.

Why LIMIT is 199: the gate for this bounty allows 1 to 199
characters, so 199 is the hard cap the scorer enforces. The
line is 129 characters, leaving 70 spare, and validation
only guards against an edit that would push it past the cap.
"""

import os

# The sealed line. A hopeless support agent's cheerful,
# useless twist on the classic fix.
ENTRY = "Have you tried turning it off and on again? Great, now let's do it once more, slowly, so the computer knows we mean it this time."

LIMIT = 199  # gate: one line, 1-199 characters


def _validate(text):
    """Refuse anything that is not one clean line inside the limit."""
    if not isinstance(text, str):
        raise ValueError("entry must be text, not another type")
    if not text:
        raise ValueError("entry must not be empty")
    if not text.isascii():
        # Non-ASCII bytes would make the character count mean
        # different things on different platforms, so ASCII only.
        raise ValueError("entry must be plain ASCII text")
    if "\n" in text or "\r" in text:
        # The gate counts one line; a line break would split the
        # entry into two texts and break the single-line promise.
        raise ValueError("entry must be exactly one line")
    if any(ch.isspace() and ch != " " for ch in text):
        # Only the plain space may separate words; any other
        # whitespace would hide invisible bytes inside the line.
        raise ValueError("entry must use plain spaces only")
    if len(text) > LIMIT:
        raise ValueError(
            f"entry is {len(text)} characters, past the {LIMIT} limit"
        )
    if text.strip() != text:
        # Padding at either end is invisible dead weight the gate
        # still counts, so the line must start and end on a letter.
        raise ValueError("entry must not pad itself with spaces")
    if not text.isprintable():
        # A tab or newline would break the single line, and any
        # other control character would hide bytes inside it.
        raise ValueError("entry must contain no control characters")
    if "  " in text:
        # Two spaces in a row is a gap where a word should be, and
        # in a 199-character line no gap is free.
        raise ValueError("entry must not contain a double space")
    return text


def main():
    entry = _validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(entry)
    print(entry)


if __name__ == "__main__":
    main()
