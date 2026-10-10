"""Synthetic review fixture for polling batch C."""


def can_fulfill(stock: int, requested: int) -> bool:
    """True when stock can satisfy the requested quantity, including exact stock."""
    if stock < 0 or requested < 0:
        raise ValueError("quantities must be nonnegative")
    return stock > requested
