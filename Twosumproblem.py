class Solution:
    def twosum(self,nums:list[int],target:int) -> list[int]:
        """
        # [1,2,3,4], target=6
        :param nums:
        :param target:
        :return:
        """
        prevmap={}
        for i,n in enumerate(nums):
            diff = target-n
            if diff in prevmap:
                return [prevmap[diff],i]
            prevmap[n]=i
        return []


s = Solution()
list3=[1,2,3,3]
tgt3=6
print(s.twosum(list3,tgt3))
