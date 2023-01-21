import json
from training_model import Training
from conversation_model import Conversation

if not Training.exists():
  Training.create_table(read_capacity_units=1,
                    write_capacity_units=1, wait=True)

if not Conversation.exists():
  Conversation.create_table(read_capacity_units=1,
                    write_capacity_units=1, wait=True)

with open('preset_conversations.json', 'r',encoding="utf-8") as f:
    preset_conversations = json.load(f)

# スコア情報を挿入する
Conversation(message_id='shortcut_001', message=json.dumps(preset_conversations['shortcut_001']),
      request_type="shortcut").save()
Conversation(message_id='block_actions_001', message=json.dumps(preset_conversations['block_actions_001']),
      request_type="block_actions").save()
Conversation(message_id='block_actions_002', message=json.dumps(preset_conversations['block_actions_002']),
      request_type="block_actions").save()
Conversation(message_id='block_actions_003', message=json.dumps(preset_conversations['block_actions_003']),
      request_type="block_actions").save()
Conversation(message_id='modal_001', message=json.dumps(preset_conversations['modal_001']),
      request_type="view_submission").save()
print('Done!')