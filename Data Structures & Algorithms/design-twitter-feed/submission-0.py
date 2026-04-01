class Twitter:

    def __init__(self):
        self.reverseTime = 0
        self.tweetMap = defaultdict(list) # userId -> list of [(reverse timestamp, tweetId)]
        self.followMap = defaultdict(set) # userId -> set of followeeIds

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.reverseTime, tweetId))
        self.reverseTime -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res, heap = [], []
        
        # temporarily add user as a follower of self, to retrieve their tweets as well for the news feed
        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                reverseTime, tweetId = self.tweetMap[followeeId][-1]
                nextIdx = len(self.tweetMap[followeeId]) - 2
                heapq.heappush(heap, [reverseTime, tweetId, followeeId, nextIdx])
        
        while len(res) < 10 and heap:
            _, tweetId, followeeId, nextIdx = heapq.heappop(heap)
            res.append(tweetId)
            if nextIdx >= 0:
                reverseTime, tweetId = self.tweetMap[followeeId][nextIdx]
                heapq.heappush(heap, [reverseTime, tweetId, followeeId, nextIdx - 1])
        
        # remove user as follower of self
        self.followMap[userId].remove(userId)
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)
