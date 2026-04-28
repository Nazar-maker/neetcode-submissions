class MedianFinder:

    def __init__(self):
        self.values = []

    def addNum(self, num: int) -> None:
        if len(self.values) == 0: 
            self.values.append(num)
            return
        for i in range(len(self.values)):
            if num >= self.values[i]: continue
            self.values.insert(i, num)
            return
        self.values.append(num)
        
    def findMedian(self) -> float:
        if len(self.values) % 2 == 0:
            return (self.values[len(self.values)//2-1] + self.values[len(self.values)//2]) / 2
        else:
            return self.values[len(self.values)//2]
        