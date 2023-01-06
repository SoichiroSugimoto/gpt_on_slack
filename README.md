# slack-based_fine-tuning


## Docker compose and Docker usage
- create docker image and run docker container docker compose

`$ docker compose up -d --build`


- run docker container through docker compose

`$ docker compose up`


- use bash on the docker container through docker compose

`$ docker compose exec python3 bash`


- use Jupyter Notebook as development environment (acssess to http://127.0.0.1:7777 after run the command)

`$ docker run -v $PWD/opt:/root/src -w /root/src -it --rm -p 7777:8888 slack-based_fine-tuning-python3 jupyter-lab --ip 0.0.0.0 --allow-root -b localhost`

<br><br>
## Architecture

![application-architecture](https://github.com/SoichiroSugimoto/slack-based_fine-tuning/blob/main/architecture.png)
