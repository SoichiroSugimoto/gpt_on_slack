FROM amazon/aws-sam-cli-build-image-python3.9
USER root

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

RUN pip install pynamodb python-dotenv
RUN pip install --upgrade openai
RUN pip install jupyterlab
