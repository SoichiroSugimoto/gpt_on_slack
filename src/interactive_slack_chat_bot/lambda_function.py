import os
import json
import boto3
import ast
from urllib import parse

import slack_functions as slack
import openai_functions as opai

from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute, MapAttribute

dynamodb = boto3.resource('dynamodb', region_name = 'ap-northeast-1')
conversations = dynamodb.Table('Conversation')

def usage_guide(receive_payload, channel):
  res = None
  if (receive_payload['type'] == "shortcut"):
    callback_id = receive_payload['callback_id']
    data = conversations.get_item( Key={'message_id':callback_id} )
    if (callback_id == 'modal_001'):
      modal = data['Item']['message']
      slack.open_modal(receive_payload['trigger_id'], modal)
    else:
      message = data['Item']['message']
      value = json.dumps(json.loads(message)["blocks"])
      res = slack.post_channel_by_params(channel, {"blocks": value})
  elif (receive_payload['type'] == "block_actions"):
    action_value = receive_payload['actions'][0]["value"]
    data = conversations.get_item( Key={'message_id':action_value} )
    message = data['Item']['message']
    value = json.loads(message)
    res = slack.post_channel_by_params(channel, value)
  else:
    res = slack.post_channel_message(channel, "無効なリクエストです。" + receive_payload)
  return (res)

def lambda_handler(event, context):
  channel = "C04HQ5GFYHL"
  receive_body = []
  try:
    receive_body = parse.parse_qs(event['body'])
    receive_payload = json.loads(receive_body["payload"][0])
  except:
    receive_payload = json.loads(event['body'])
  if not ('type' in receive_payload):
    res = slack.post_channel_message(channel, "Error")
  elif (receive_payload['type'] == 'url_verification'):
    return {
      'statusCode': 200,
      'body': json.dumps( {'challenge': receive_payload['challenge'] } )
    }
  elif (receive_payload["type"] == "event_callback" and
        receive_payload["event"]["user"] != "U04HAFAP9FW" and
        int(json.loads(event['headers']['X-Slack-Retry-Num'])) == 1):
    channel = receive_payload['event']['channel']
    request_text = ''
    if ('thread_ts' in receive_payload["event"]):
      request_text = slack.get_text_element_as_thread(channel, receive_payload['event']['thread_ts'])
    else:
      request_text = slack.get_text_element(receive_payload)
    reply_text = opai.openai_prompt(request_text)
    response = slack.post_channel_reply(channel, reply_text, receive_payload["event"]["ts"])
  else:
    response = usage_guide(receive_payload, channel)
  return (response)