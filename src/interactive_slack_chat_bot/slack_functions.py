import os
import requests

slack_bot_token = os.getenv('SLACK_BOT_TOKEN')

def post_channel_by_params(channel, params):
  slack_request_headers = {"Authorization": "Bearer " + slack_bot_token}
  params["channel"] = channel

  response = requests.post("https://slack.com/api/chat.postMessage", headers=slack_request_headers, params=params)
  return (response.json())

def post_channel_message(channel, message):
  slack_request_headers = {"Authorization": "Bearer " + slack_bot_token}
  params={
              "channel": channel,
              "text": message
          }

  response = requests.post("https://slack.com/api/chat.postMessage", headers=slack_request_headers, params=params)
  return (response.json())

def post_channel_reply(channel, message, ts):
  slack_request_headers = {"Authorization": "Bearer " + slack_bot_token}
  params={
              "channel": channel,
              "text": message,
              "channel": channel,
              "thread_ts": ts
          }

  response = requests.post("https://slack.com/api/chat.postMessage", headers=slack_request_headers, params=params)
  return (response.json())

def get_channel_message(channel):
  slack_request_headers = {"Authorization": "Bearer " + slack_bot_token}
  params = {
    "channel": channel
  }

  response = requests.get("https://slack.com/api/conversations.history", headers=slack_request_headers, params=params)
  return (response.json())

def get_channel_thread(channel, ts):
  slack_request_headers = {"Authorization": "Bearer " + slack_bot_token}
  params = {
    "channel": channel,
    "ts": ts
  }

  response = requests.get("https://slack.com/api/conversations.replies", headers=slack_request_headers, params=params)
  return (response.json())