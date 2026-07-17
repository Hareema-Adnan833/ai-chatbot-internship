
# 🤖 Database AI Chatbot

## 📌 Project Overview

The Database AI Chatbot is an intelligent chatbot developed using **Python**, **Streamlit**, and the **Hugging Face Inference API**. It is designed to answer only database-related questions such as SQL, MySQL, PostgreSQL, MongoDB, Database Design, Normalization, and other DBMS concepts.

The chatbot uses Prompt Engineering techniques to improve the quality of responses and provides an interactive web interface through Streamlit.

---

# 🚀 Features

- Interactive chatbot interface using Streamlit
- Database-specific AI assistant
- Supports conversation history
- Uses Hugging Face GPT-OSS-120B model
- Prompt Engineering techniques
  - Zero-Shot Prompting
  - One-Shot Prompting
  - Few-Shot Prompting
  - Role-Based Prompting
  - Intrusion Detection Prompting
- Temperature control
- Response Length selection
- Explanation Level selection
- Include Real-life Example option
- Clear Chat functionality
- Error handling for API requests

---

# 🛠 Technologies Used

- Python
- Streamlit
- Hugging Face Inference API
- python-dotenv
- Git & GitHub

---

# 📂 Project Structure

AIChatbot/

│── app.py

│── test.py

│── .env

│── .gitignore

│── requirements.txt

│── README.md

└── .streamlit/

        └── config.toml

---

# ⚙ Installation Guide

## Step 1

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
```

---

## Step 2

Go to the project folder

```bash
cd YOUR_REPOSITORY
```

---

## Step 3

Create Virtual Environment

```bash
python -m venv chatbot_env
```

---

## Step 4

Activate Virtual Environment

### Windows

```bash
chatbot_env\Scripts\activate
```

### Linux / Mac

```bash
source chatbot_env/bin/activate
```

---

## Step 5

Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 6

Create a `.env` file

Add your Hugging Face API Token.

```env
HF_TOKEN=your_huggingface_api_token
```

---

## Step 7

Run the Chatbot

```bash
streamlit run app.py
```

The application will open in your browser.

---

# 💬 How the Chatbot Works

1. The user enters a database-related question in the Streamlit interface.
2. The selected Prompt Engineering technique is applied.
3. Additional response settings (Temperature, Response Length, Difficulty Level, etc.) are added to the system prompt.
4. The application sends an HTTP request to the Hugging Face Inference API.
5. The GPT-OSS-120B model processes the request.
6. The generated response is returned to the application.
7. Streamlit displays the response in the chat interface.
8. Conversation history is maintained throughout the session.

---

# 🧠 Prompt Engineering Techniques

The chatbot supports the following prompting techniques:

- Zero-Shot Prompting
- One-Shot Prompting
- Few-Shot Prompting
- Role-Based Prompting
- Intrusion Detection Prompting

Users can select any technique from the sidebar before asking a question.

---

# ⚙ Response Settings

The chatbot provides additional customization options:

- Temperature
- Response Length
- Explanation Level
- Include Real-life Example
- Clear Chat

These options help customize AI-generated responses.

---

# 📌 Example Questions

- What is SQL?
- Explain Database Normalization.
- Difference between Primary Key and Foreign Key.
- What is MongoDB?
- Explain SQL JOIN with an example.
- Write a SQL query to display all employees.

---

# ❌ Out-of-Domain Questions

The chatbot only answers questions related to databases.

If a user asks unrelated questions (e.g., sports, politics, weather), the chatbot politely refuses to answer.

---

# 📄 Future Improvements

- User Authentication
- Multiple AI Models
- Voice Input
- File Upload Support
- SQL Query Execution
- Dark/Light Theme Toggle

---

# 👩‍💻 Author

Hareema Adnan

AI Chatbot Internship Project
