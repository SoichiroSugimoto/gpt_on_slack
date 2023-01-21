# slack-based_fine-tuning
This is AI chatbot using GPT from [OpenAI](https://openai.com/). It is working on Slack and triggered by mention.

You can chat with it interactively. And, it will be your friend. 😉

<br><br>
![usage](https://github.com/SoichiroSugimoto/slack-based_fine-tuning/blob/demo/demo.gif)

## Preparation
slack-based_fine-tuning/src/dynamodb_migrate/.env
```
aws_access_key_id=[aws_access_key_id]
aws_secret_access_key=[aws_access_key_id]
```

Eenvironment variables on AWS Lambda
```
- SLACK_BOT_TOKEN
- SLACK_CHANNEL
- OPENAI_API_KEY
```

## Docker compose and Docker usage
- create docker image and run docker container docker compose

`$ docker compose up -d --build`


- run docker container through docker compose

`$ docker compose up`


- use bash on the docker container through docker compose

`$ docker compose exec python3 bash`



<br><br>
## Architecture

![application-architecture](https://github.com/SoichiroSugimoto/slack-based_fine-tuning/blob/demo/architecture.png)


<br><br>
## 日本語記事
[GPT-3.5 × AWS Lambda × Amazon DynamoDB × Amazon API Gatewayを使ったSlackのチャットボットをPythonで実装する](https://qiita.com/nosandone/items/831336aba63bafc536e5)
