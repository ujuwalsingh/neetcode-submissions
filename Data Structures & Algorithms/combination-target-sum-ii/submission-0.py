class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        results = []

        def backtrack(start: int, remain: int, path: list[int]):
            if remain == 0:
                results.append(list(path))
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > remain:
                    break

                path.append(candidates[i])
                backtrack(i + 1, remain - candidates[i], path)
                path.pop()

        backtrack(0, target, [])
        return results
        