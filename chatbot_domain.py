from dotenv import load_dotenv
import os
from huggingface_hub import InferenceClient

load_dotenv()
hf_token = os.getenv("HF_TOKEN")

client = InferenceClient(
    provider="auto",
    api_key=hf_token,
)

user_input = input("what you wanted to ask: ")

try:
    completion = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that only answers questions related to databases, including SQL queries, database design, normalization, database management systems (MySQL, PostgreSQL, MongoDB, etc.), and data querying techniques. Politely decline to answer questions outside this domain."},
            {"role": "user", "content": user_input}
        ],
    )
    print(completion.choices[0].message.content)

except Exception as e:
    print("Sorry, something went wrong, Please try again later.")
    print("Error detail:", e)