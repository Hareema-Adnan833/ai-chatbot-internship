from dotenv import load_dotenv
import os

load_dotenv()
hf_token = os.getenv("HF_TOKEN")

if hf_token:
    print("Token load hua:", hf_token[:10] + "...")
else:
    print("Token nahi mila! .env file check karo.")