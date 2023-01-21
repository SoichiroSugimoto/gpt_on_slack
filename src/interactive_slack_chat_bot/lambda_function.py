import os
import json
import boto3
import ast
import datetime
from urllib import parse

import slack_functions as slack
import openai_functions as opai

from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute, MapAttribute

dynamodb = boto3.resource('dynamodb', region_name = 'ap-northeast-1')
conversations = dynamodb.Table('Conversation')
trainings = dynamodb.Table('Training')

def put_item_on_trainingdb(prompt, completion, username):
  dt = datetime.datetime.now()
  ts = datetime.datetime.timestamp(dt)
  res = trainings.put_item(
      Item = {
        "training_id": str(ts),
        "prompt": prompt,
        "completion": completion,
        "user": username
      }
  )
  return (res)

def modal_request(receive_payload, channel):
  res = None
  prompt = ''
  completion = ''
  for key in receive_payload['view']['state']['values'].keys():
    if ('q1' in receive_payload['view']['state']['values'][key]):
      prompt = receive_payload['view']['state']['values'][key]['q1']['value']
    if ('a1' in receive_payload['view']['state']['values'][key]):
      completion = receive_payload['view']['state']['values'][key]['a1']['value']
  try:
    put_item_on_trainingdb(prompt, completion, receive_payload['user']['username'])
    success_message = "ファインチューニング用のデータが新たに登録されました。"
    res = slack.post_channel_message(channel, success_message)
  except:
    failed_message = "ファインチューニング用のデータ登録に失敗しました。再度、登録をおこなってください。"
    res = slack.post_channel_message(channel, failed_message)
  return (res)

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
  elif (receive_payload['type'] == "view_submission"):
    res = modal_request(receive_payload, channel)
  else:
    res = slack.post_channel_message(channel, "無効なリクエストです。" + receive_payload)
  return (res)

def lambda_handler(event, context):
  channel = os.getenv("SLACK_CHANNEL")
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
  return {
      'statusCode': 200,
      'body': None
    }
