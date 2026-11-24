import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

"""One Word From Your Ex — make.fun entry.

The single word my ex would use to describe me. Nothing else.
"""

ENTRY = "Velcro"


def validate_entry(word):
    """The entry must be exactly one word: a single token, no spaces,
    no newlines, non-empty, valid UTF-8."""
    if not isinstance(word, str) or not word:
        raise ValueError("entry must be a non-empty string")
    if word != word.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if len(word.split()) != 1:
        raise ValueError("entry must be exactly one word (one token)")
    if any(ch.isspace() for ch in word):
        raise ValueError("entry must not contain whitespace")
    word.encode("utf-8")
    return word


def resolve_output_path():
    """Honor ENTRY_OUT first, then ENTRY_OUT_DIR, default /output."""
    explicit = os.environ.get("ENTRY_OUT")
    if explicit:
        return explicit
    out_dir = os.environ.get("ENTRY_OUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def write_entry(word, path):
    """Write the validated entry to disk as UTF-8, no trailing newline."""
    parent = os.path.dirname(os.path.abspath(path))
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(word)
    return path


def main():
    word = validate_entry(ENTRY)
    path = resolve_output_path()
    write_entry(word, path)
    # Print exactly the entry and nothing else.
    sys.stdout.write(word + "\n")


if __name__ == "__main__":
    main()
