"""
Utility functions for the example app.
"""

from typing import List

def sum_list(nums: List[int]) -> int:
    """Return sum of integer list (safe)."""
    return sum(int(x) for x in nums)

def greet(name: str) -> str:
    """Return a greeting message."""
    return f"Hello, {name}!"
