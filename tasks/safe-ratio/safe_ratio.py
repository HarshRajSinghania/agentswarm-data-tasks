from __future__ import annotations


_MIN = -1_000_000_000
_MAX = 1_000_000_000


def safe_ratio(numerator: int, denominator: int) -> float | None:
    """Return numerator / denominator for exact built-in ints, or None for zero denominator."""
    for value in (numerator, denominator):
        if isinstance(value, bool) or type(value) is not int:
            raise TypeError("numerator and denominator must be exact built-in ints")

    for value in (numerator, denominator):
        if not _MIN <= value <= _MAX:
            raise ValueError("numerator and denominator must be within [-1000000000, 1000000000]")

    if denominator == 0:
        return None

    return numerator / denominator
