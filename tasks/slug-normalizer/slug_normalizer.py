"""Normalize an authored task title into a bounded ASCII slug; see SPEC.md."""
import unicodedata


def normalize_slug(text, max_length=64):
    if not isinstance(text, str):
        raise TypeError("text must be str")
    if not isinstance(max_length, int) or isinstance(max_length, bool):
        raise TypeError("max_length must be int")
    if not (1 <= max_length <= 128):
        raise ValueError("max_length must be between 1 and 128")

    # Unicode casefold
    s = text.casefold()
    # NFKD normalization
    s = unicodedata.normalize("NFKD", s)
    # Remove combining marks (category starts with M)
    s = "".join(c for c in s if not unicodedata.category(c).startswith("M"))

    # Replace maximal runs outside ASCII [a-z0-9] with one hyphen
    result = []
    in_sep = False
    for c in s:
        if "a" <= c <= "z" or "0" <= c <= "9":
            if in_sep:
                result.append("-")
                in_sep = False
            result.append(c)
        else:
            in_sep = True
    slug = "".join(result)

    # Trim hyphens from both ends
    slug = slug.strip("-")

    # Truncate to first max_length ASCII characters
    slug = slug[:max_length]

    # Remove trailing hyphens again
    slug = slug.rstrip("-")

    # If nothing remains, return first max_length characters of literal "task"
    if not slug:
        return "task"[:max_length]

    return slug
