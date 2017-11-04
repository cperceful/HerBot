import praw;
import os
from time import sleep

if not os.path.isfile("repliedComments.txt"):
    repliedComments = []
else:
    with open("repliedComments.txt", "r") as f:
        repliedComments = f.read()
        repliedComments = repliedComments.split("\n")
        repliedComments = list(filter(None, repliedComments))

TARGET_NAME = "Ann"
MESSAGE = "Her?"

bot = praw.Reddit('bot1')

subreddit = bot.subreddit('mysecrettestingplace')
comments = subreddit.stream.comments()

for comment in comments:
    text = comment.body
    if TARGET_NAME in text and comment.id not in repliedComments:
        print("Ann detected: ")
        print(text)

        try:
            comment.reply(MESSAGE)
            repliedComments.append(comment.id)
            with open("repliedComments.txt", "w") as f:
                for commentId in repliedComments:
                    f.write(commentId + "\n")
        except praw.exceptions.APIException as e:
            print("[ERROR]: " + e)
            sleep(30)
