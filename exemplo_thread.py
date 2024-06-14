from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

file = client.files.create(
  file=open("chatbot/dados/data.csv", "rb"),
  purpose='assistants'
)

print(file.id)

assistant = client.beta.assistants.create(
  name="Robô de finanças pessoais",
  description="Um assistente excelente em criar projeções financeiras",
  instructions="Você é um assistente amigável.",
  model="gpt-4-1106-preview",
  tools=[{"type": "code_interpreter"}],
  file_ids=[file.id]
)

thread = client.beta.threads.create(
  messages=[
    {
      "role": "user",
      "content": "Crie 3 visualizações de dados com base nas tendências deste arquivo.",
      "file_ids": [file.id]
    }
  ]
)

run = client.beta.threads.runs.create(
  thread_id=thread.id,
  assistant_id=assistant.id
)

STATUS_COMPLETED = "completed"
while run.status != STATUS_COMPLETED:
    run = client.beta.threads.runs.retrieve(
        thread_id=thread.id,
        run_id=run.id
    )
    print(run.status)

historico = list(client.beta.threads.messages.list(thread_id=thread.id).data)
resposta = historico[0]
print("Resposta: ", resposta)

client.beta.assistants.delete(assistant_id=assistant.id)
client.beta.threads.delete(thread_id=thread.id)
