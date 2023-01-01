#! /bin/bash

# remove
touch interactive_slack_chat_bot.zip
rm interactive_slack_chat_bot.zip
cd interactive_slack_chat_bot

# compress
zip -r ../interactive_slack_chat_bot.zip ./*
cd ..