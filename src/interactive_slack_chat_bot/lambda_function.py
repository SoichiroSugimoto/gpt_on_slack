import os
import json
import boto3
from urllib import parse

import slack_functions as slack

def lambda_handler(event, context):
  receive_body = parse.parse_qs(event['body'])
  receive_payload = json.loads(receive_body["payload"][0])
  message = "こんにちは" + receive_payload["user"]["username"] + "さん."
  slack.post_channel_message(channel, message)
  return (receive_payload)
