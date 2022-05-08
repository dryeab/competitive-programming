

class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        nums = list(set(nums1)) + list(set(nums2)) + list(set(nums3))
        answer, count = [], Counter(nums)
        for i in count:
            if count[i] > 1:
                answer.append(i)
        return answer
