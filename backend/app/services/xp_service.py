"""
XP calculation rules:
  Easy   correct → +5 XP
  Medium correct → +10 XP
  Hard   correct → +20 XP
  Speed bonus (answered in < 20 s) → +5 XP extra
  Wrong answer → 0 XP (no penalty)
"""

XP_TABLE = {"easy": 5, "medium": 10, "hard": 20}
SPEED_BONUS = 5
SPEED_THRESHOLD = 20   # seconds


def calculate_xp(difficulty: str, is_correct: bool, time_taken: int) -> int:
    if not is_correct:
        return 0

    base_xp = XP_TABLE.get(difficulty.lower(), 5)
    bonus   = SPEED_BONUS if time_taken < SPEED_THRESHOLD else 0
    return base_xp + bonus
