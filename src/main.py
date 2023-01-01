import os
import json
import boto3
import slack_functions as slack

def main():
  channel = "C04G56FP3S7"
  message = "今年もよろしくお願いします。"
  res = slack.post_channel_message(channel, message)
  print (res)

if __name__ == "__main__":
  main()