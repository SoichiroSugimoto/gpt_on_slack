# slack-based_fine-tuning
This is AI chatbot using GPT from [OpenAI](https://openai.com/). It is working on Slack and triggered by mention.

You can chat with it interactively. And, it will be your friend. 😉

<br><br>
![usage](https://github.com/SoichiroSugimoto/slack-based_fine-tuning/blob/demo/demo.gif)


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
