#!/usr/bin/env python3
"""Load 15-3sum/3sum.py and run LeetCode's sample cases."""

from __future__ import annotations

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOLUTION = ROOT / "15-3sum" / "3sum.py"


def load_solution():
    spec = importlib.util.spec_from_file_location("three_sum", SOLUTION)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.Solution()


def main() -> None:
    solver = load_solution()
    cases = (
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 1, 1], []),
        ([0, 0, 0], [[0, 0, 0]]),
    )
    for nums, expected in cases:
        got = solver.threeSum(list(nums))
        got_sorted = sorted(sorted(t) for t in got)
        expected_sorted = sorted(sorted(t) for t in expected)
        status = "ok" if got_sorted == expected_sorted else "FAIL"
        print(f"{status}  nums={nums}  ->  {got}")


if __name__ == "__main__":
    main()
