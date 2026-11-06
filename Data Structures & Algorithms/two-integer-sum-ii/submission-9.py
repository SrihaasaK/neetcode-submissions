class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lp = 0
        rp = len(numbers) - 1
        while numbers[lp] + numbers[rp] != target:
            if numbers[lp] + numbers[rp] > target:
                rp -= 1
            else:
                lp += 1
        return [lp+1,rp+1]