import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

with open('input.py') as f:
    prompt = f.read()

response = openai.Completion.create(
  model="code-davinci-002",
  prompt=prompt,
  temperature=0,
  max_tokens=300,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

completed_text = response['choices'][0]['text']

with open('output.py', "w") as f:
    f.write(prompt)
    f.write(completed_text)