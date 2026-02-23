class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def check(min_speed, max_speed):
            k = min_speed + max_speed // 2
            count = 0
            for pile in piles:
                if pile % k != 0:
                    count += pile // k + 1
                else:
                    count += pile / k

            if count <= h:
                return check()

            return k

        min_speed = 0
        max_speed = max(piles)

        check(min_speed, max_speed)
            
