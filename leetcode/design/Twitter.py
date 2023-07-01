from typing import List
from heapq import heappush, heappop


class Twitter:
    global_time = 0

    def __init__(self):
        self.idToUser = {}

    class User:
        def __init__(self, id: int):
            self.userId = id
            self.follow_users_id_set = set()
            self.headTweet = None

        def get_headTweet(self):
            return self.headTweet

        def follow(self, other_user):
            self.follow_users_id_set.add(other_user)

        def unfollow(self, other_user):
            self.follow_users_id_set.discard(other_user)

        def post(self, tweet):
            tweet.set_next(self.headTweet)
            self.headTweet = tweet

        def follow(self, follower_id):
            self.follow_users_id_set.add(follower_id)
            # print(self.follow_users_id_set)

        def unfollow(self, follower_id):
            self.follow_users_id_set.discard(follower_id)

    class Tweet:
        def __init__(self, tweet_id: int):
            self.tweet_id = tweet_id
            self.timestamp = Twitter.global_time
            self.next = None
            Twitter.global_time += 1

        def get_next(self):
            return self.next

        def set_next(self, next_tweet):
            self.next = next_tweet

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.idToUser:
            self.idToUser[userId] = Twitter.User(userId)
        user = self.idToUser.get(userId)
        user.post(Twitter.Tweet(tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        pq = []
        if userId not in self.idToUser:
            return

        user = self.idToUser[userId]

        following = user.follow_users_id_set
        # print(following)
        for followee_id in following:
            followee = self.idToUser[followee_id]
            if followee.get_headTweet():
                heappush(pq, (-followee.headTweet.timestamp, followee.headTweet))

        if user.headTweet:
            heappush(pq, (-user.headTweet.timestamp, user.headTweet))
        count = 0
        res = []
        while count < 10 and pq:
            _, headTweet = heappop(pq)
            res.append(headTweet.tweet_id)
            if headTweet.get_next():
                heappush(pq, (-headTweet.get_next().timestamp, headTweet.get_next()))
            count += 1
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.idToUser:
            self.idToUser[followerId] = Twitter.User(followerId)
        if followeeId not in self.idToUser:
            self.idToUser[followeeId] = Twitter.User(followeeId)
        follower_user = self.idToUser.get(followerId)
        follower_user.follow(followeeId)

        # print(follower_user.follow_users_id_set)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.idToUser or followeeId not in self.idToUser:
            return
        follower_user = self.idToUser[followerId]
        follower_user.unfollow(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)