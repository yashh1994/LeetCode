from heapq import heapify,heappop,heappush
class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        n = len(times)
        av_chair = list(range(n))
        heapify(av_chair)
        used_chair = []
        time = [[a,l,i] for i,(a,l) in enumerate(times)]
        time = sorted(time,key=lambda x:x[0])
        print(time)
        for a,l,ind in time:
            while used_chair and used_chair[0][0] <= a:
                _,i = heappop(used_chair)
                heappush(av_chair,i)
            pos = heappop(av_chair)
            if ind == targetFriend:
                return pos
            heappush(used_chair,[l,pos])
        return -1


        