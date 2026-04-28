class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        for i in nums:
            hashMap[i] = 1 + hashMap.get(i, 0)
        
        frequent = []
        print(hashMap)
        for i in range(k):
            m = 0
            e = 0
            for j in hashMap:
                if hashMap[j] > m:
                    m = hashMap[j]
                    e = j
            frequent.append(e)
            hashMap.pop(e)
        return frequent