class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def check(min_speed, max_speed):
            k = 0
            while min_speed < max_speed: 

                k = (min_speed + max_speed) // 2
                # print(k)

                if k == 0:
                    return k+1

                count = 0
                for pile in piles:
                    if pile % k != 0:
                        count += pile // k + 1
                    else:
                        count += pile / k

                # print(count)
                if count > h:
                    if min_speed == k:
                        break
                    min_speed = k
                elif count <= h:
                    if max_speed == k:
                        break
                    max_speed = k

            return k+1

        min_speed = 0
        max_speed = max(piles)

        if len(piles) == h:
            return max_speed
        
        return check(min_speed, max_speed)
