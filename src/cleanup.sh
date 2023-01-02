#! /bin/bash

# remove
if [ -f ./interactive_slack_chat_bot.zip ]; then
  rm ./interactive_slack_chat_bot.zip
fi

if [ -f ./labmda_layer.zip ]; then
  rm ./labmda_layer.zip
fi

if [ -d ./python ]; then
  rm -r ./python
fi
