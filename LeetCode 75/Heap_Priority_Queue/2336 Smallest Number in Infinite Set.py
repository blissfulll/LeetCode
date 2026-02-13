class SmallestInfiniteSet:

    def __init__(self):
        # self.sis = []
        self.del_flags = []
        for i in range(1000):
            # self.sis.append(i+1)
            self.del_flags.append(False)

    def popSmallest(self) -> int:
        i = 0
        while self.del_flags[i]:
            i += 1

        self.del_flags[i] = True

        return i + 1

    def addBack(self, num: int) -> None:
        if self.del_flags[num-1]:
            self.del_flags[num-1] = False
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
