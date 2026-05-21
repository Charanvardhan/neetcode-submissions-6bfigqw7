import heapq
from collections import defaultdict

class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count -= 1
        self.tweetMap[userId].append([self.count, tweetId])
        

    def getNewsFeed(self, userId: int) -> List[int]:
        result = []
        hp = []

        followingIds = self.followMap[userId] | {userId}

        for uid in followingIds:
            tweets = self.tweetMap[uid]
            if tweets:
                idx = len(tweets) - 1
                count, tweetid = tweets[idx]
                heapq.heappush(hp, [count, tweetid, uid,idx])
            
        while hp and len(result) < 10:
            count, tweetid, uid, idx = heapq.heappop(hp)
            nextIdx = idx - 1
            result.append(tweetid)

            if nextIdx >= 0:
                count, tweetid = self.tweetMap[uid][nextIdx]
                heapq.heappush(hp, [count, tweetid, uid, nextIdx])
        
        return result


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        
