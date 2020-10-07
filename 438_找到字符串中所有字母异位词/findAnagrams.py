class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        窗口法：
        使用一个len(p)大小的hash，（或者是256的hash）
        1、扩张窗口，每次对hash对应字符的值进行+1更新，长度满足之后，
        """