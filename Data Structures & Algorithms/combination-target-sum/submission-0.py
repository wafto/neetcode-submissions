class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []

        def dfs(index: int, current: List[int], acc: int) -> None:
            if index >= len(nums) or acc > target:
                return
            if acc == target:
                output.append(current.copy())
                return
            current.append(nums[index])
            dfs(index, current, acc + nums[index])
            current.pop()
            dfs(index + 1, current, acc)

        dfs(0, [], 0)
        return output

