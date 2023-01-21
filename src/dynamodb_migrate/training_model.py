import os
from dotenv import load_dotenv
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute,NumberAttribute

load_dotenv('.env')

class Training(Model):
  class Meta:
    table_name = 'Training'
    region = 'ap-northeast-1'
    read_capacity_units = 1
    write_capacity_units = 1
    aws_access_key_id = os.getenv('aws_access_key_id')
    aws_secret_access_key = os.getenv('aws_secret_access_key')

  training_id = UnicodeAttribute(hash_key=True)
  prompt = UnicodeAttribute()
  completion = UnicodeAttribute()
  user = UnicodeAttribute()