class Solution:

    def checkString(self, s, pointer) -> tuple(bool, str):
        sett = set()
        for l in range(len(s)-pointer+1):
            if s[l:l+pointer] in sett:
                return True, s[l:l+pointer]
            else:
                sett.add(s[l:l+pointer])

        return False, "" 

    def longestDupSubstring(self, s: str) -> str:
        
        l, r, result = 0, len(s), ""

        while l+1 < r:
            mid = l + (r - l) // 2
            # print(mid)
            is_found, rresult = self.checkString(s, mid)
            # print(result)
            if is_found:
                l, result = mid, rresult
            else:
                r = mid
        
        return result
