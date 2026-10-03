import heapq
from collections import defaultdict

class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.timestamp, tweetId))
        self.timestamp -= 1

    def getNewsFeed(self, userId: int) -> list[int]:
        heap = []
        users = self.following[userId] | {userId}

        for u in users:
            if self.tweets[u]:
                idx = len(self.tweets[u]) - 1
                time, tweetId = self.tweets[u][idx]
                heap.append((time, tweetId, u, idx))

        heapq.heapify(heap)
        feed = []

        while heap and len(feed) < 10:
            time, tweetId, u, idx = heapq.heappop(heap)
            feed.append(tweetId)
            if idx > 0:
                next_idx = idx - 1
                next_time, next_tweetId = self.tweets[u][next_idx]
                heapq.heappush(heap, (next_time, next_tweetId, u, next_idx))

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
