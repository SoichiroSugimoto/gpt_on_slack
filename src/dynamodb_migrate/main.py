import json
from conversation_model import Conversation

if not Conversation.exists():
  Conversation.create_table(read_capacity_units=1,
                    write_capacity_units=1, wait=True)

with open('preset_conversations.json', 'r',encoding="utf-8") as f:
    preset_conversations = json.load(f)

# スコア情報を挿入する
Conversation(message_id='m1', message=json.dumps(preset_conversations['m1']),
      request_type="shortcut", request_value='shortcut_001').save()
Conversation(message_id='m2', message=json.dumps(preset_conversations['m2']),
      request_type="block_actions", request_value='block_actions_001').save()
Conversation(message_id='m3', message=json.dumps(preset_conversations['m3']),
      request_type="block_actions", request_value='block_actions_002').save()
Conversation(message_id='m3', message=json.dumps(preset_conversations['m4']),
      request_type="block_actions", request_value='block_actions_003').save()
print('Done!')