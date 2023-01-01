import os
import json
import boto3
import slack_functions as slack

def lambda_handler(event, context):
  channel = "C04G56FP3S7"
  message = "今年もよろしくお願いします。"
  res = slack.post_channel_message(channel, message)
  return (res)

if __name__ == "__lambda_function__":
  lambda_handler()