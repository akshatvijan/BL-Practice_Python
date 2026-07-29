class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        my_dict={}
        my_list=[]
        for i,value in enumerate(nums):
            ans=target-value
            if(ans in my_dict):
                my_list=[i,my_dict[ans]]
            my_dict.update({value:i})
        return my_list
    

               
        