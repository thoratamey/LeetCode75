class SmallestInfiniteSet:

    def __init__(self):
        self.smallest = 1 #current smallest
        self.removed = set() #set of removed elemts

    def popSmallest(self) -> int:
        returning = self.smallest #next smallest which is about to be popped
        self.removed.add(returning) #adding it to our removed hashset
        self.smallest += 1 #keeping track of the next smallest in our smallest variable
        while self.smallest in self.removed: #what if that smallest number is already in our removed set
            self.smallest += 1 #if found same number, we have to increment it by 1
        return returning #return the next smallest number

    def addBack(self, num: int) -> None:
        if num in self.removed: #if num is in removed hashset
            self.removed.remove(num) # we remove it from the removed hashset
            if num < self.smallest: #if it's smaller than our current num
                self.smallest = num # we assign that num to be our smallest


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
