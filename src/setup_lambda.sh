#! /bin/bash

# remove
touch interactive_slack_chat_bot.zip
rm interactive_slack_chat_bot.zip
cd interactive_slack_chat_bot

# compress
zip -r ../interactive_slack_chat_bot.zip ./*
cd ..

if [ ! -f ./lambda_layer.zip ]; then
  mkdir python
  pip install -t ./python numpy --upgrade
  pip install -t ./python requests
  pip install -t ./python pynamodb
  pip install -t ./python openai
  zip -r ./lambda_layer.zip ./python
fi
