class User:
    def __init__(self, username):
        self.username = username
        self.allow_channels_notification = []
        self.following_channels = []
        self.notifications = []

    def turn_notification(self, channel, flag=True):
        if flag and channel.channel_name not in self.allow_channels_notification:
            self.allow_channels_notification.append(channel.channel_name)
        elif flag is False and channel.channel_name in self.allow_channels_notification:
            self.allow_channels_notification.remove(channel.channel_name)
        else:
            return

    def follow(self, channel):
        self.following_channels.append(channel.channel_name)
        channel.followers.append(self)

    def unfollow(self, channel):
        self.following_channels.remove(channel.channel_name)
        channel.followers.remove(self)

    def __repr__(self):
        return f"User: {self.username}, following_channels: {self.following_channels}"


class Channel:
    def __init__(self, channel_name):
        self.channel_name = channel_name
        self.followers = []
        self.videos = []

    def upload_video(self, video_title: str):
        self.videos.append(video_title)
        self.sent_notification_about_new_video(video_title.title())

    def sent_notification_about_new_video(self, video_title):
        for follower in self.followers:
            if self.channel_name in follower.allow_channels_notification:
                follower.notifications.append(f"Вийшло нове відео на каналі {self.channel_name}: {video_title}")

    def __repr__(self):
        return f"Channel: {self.channel_name}, count followers: {len(self.followers)}, videos: {self.videos}"

    def unfollow(self, user: User):
        self.followers.remove(user)


user1 = User("Peter")
user2 = User("Mike")
user3 = User("Lindtt")
user4 = User("Kira")
user5 = User("Miron")

channel1 = Channel("Weather Forecast")
channel2 = Channel("World News")

user1.follow(channel1)
user2.follow(channel1)

user1.follow(channel2)
user3.follow(channel2)
user4.follow(channel2)

print(channel1)
print(channel2)
print(user1)

user1.turn_notification(channel1)
channel1.upload_video("Погода на завтра (06.11.2023)")
print(user1.notifications)

channel2.unfollow(user1)
channel2.unfollow(user3)
print(channel2)
