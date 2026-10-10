"""Synthetic review fixture for polling batch B."""


def retry_delay_seconds(attempt: int, base_seconds: float = 1.0) -> float:
    """Return exponential delay in seconds; attempt zero waits base_seconds."""
    if attempt < 0 or base_seconds <= 0:
        raise ValueError("invalid retry parameters")
    return base_seconds * (2 ** attempt) * 1000
