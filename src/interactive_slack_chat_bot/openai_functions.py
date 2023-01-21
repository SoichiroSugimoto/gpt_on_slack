import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.list()

def openai_prompt(prompt):
  openai_request_headers = {
      "Content-Type": "application/json",
      "Authorization": "Bearer " + openai.api_key
      }

  response = openai.Completion.create(
    model='text-davinci-003',
    prompt=prompt,
    temperature=0,
    max_tokens=1000,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
  )

  texts = ''.join([choice['text'] for choice in response.choices])
  return (texts)