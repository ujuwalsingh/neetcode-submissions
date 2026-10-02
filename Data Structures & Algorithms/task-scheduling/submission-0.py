from collections import Counter


class Solution:

  def leastInterval(self, tasks: list[str], n: int) -> int:
    counts = Counter(tasks).values()
    max_freq = max(counts)
    max_count = sum(1 for c in counts if c == max_freq)

    return max(len(tasks), (max_freq - 1) * (n + 1) + max_count)
        