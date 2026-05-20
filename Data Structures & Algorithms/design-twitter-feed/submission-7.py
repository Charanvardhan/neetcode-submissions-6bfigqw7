import heapq
from collections import defaultdict
class Twitter:

    def __init__(self):
        self.count = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count += 1
        self.tweets[userId].append([self.count,tweetId]) #O(n)
        

    def getNewsFeed(self, userId: int) -> List[int]:
        allTweets = list(self.following[userId])
        if userId not in self.following[userId]:
            allTweets.append(userId)
        hq = []

        for i in allTweets:
            for tweet in self.tweets[i]:
                heapq.heappush(hq, tweet)
                while len(hq) > 10:
                    heapq.heappop(hq)
        
        op = []
        # k = 10
        while len(hq) > 0:
            temp = heapq.heappop(hq)
            op.append(temp[1])
            # k -= 1
            
        return op[::-1]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)     

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
        
