class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n, output = len(nums), []
        nums.sort()

        for i in range(n - 2):
            if nums[i] > 0:
                continue

            if i > 0 and nums[i - 1] == nums[i]:
                continue
            
            j, k = i + 1, n - 1

            while j < k:
                addition = nums[i] + nums[j] + nums[k]

                if addition == 0:
                    output.append([nums[i], nums[j], nums[k]])
                    j, k = j + 1, k - 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
                elif addition < 0:
                    j += 1
                else:
                    k -= 1

        return output

            

