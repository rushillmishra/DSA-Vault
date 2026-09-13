class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq_dic = {}
        for a in arr: 
            if a in freq_dic:
                freq_dic[a] += 1
            else:
                freq_dic[a] = 1
        max_key = -1
        for key in freq_dic:
            if key == freq_dic[key] and key>max_key:
                max_key = key
        
        return max_key