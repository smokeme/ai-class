import os
import PyPDF2
import re
import requests

openai_api_key = 'sk-proj-'

# Function to generate text using OpenAI GPT
def generate_summary(prompt):
    url = "https://api.openai.com/v1/chat/completions"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai_api_key}"
    }

    data = {
        "model": "gpt-4o",
        "messages": [
            {
                "role": "system",
                "content": "Your name is Skynet, you are a helpful research assistant."
            },
            {
                "role": "user",
                "content": f"Summarize this: {prompt}"
            }
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    return response.json()['choices'][0]['message']['content']


pdf_summary_text = ""
pdf_file_path = "paper.pdf"

pdf_file = open(pdf_file_path,'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)

for page_num in range(len(pdf_reader.pages)):
    page_text = pdf_reader.pages[page_num].extract_text().lower()
    
    page_summary = generate_summary(page_text)
    print(f"Finished page number {page_num}...")
    pdf_summary_text += page_summary + "\n"

pdf_summary_file = pdf_file_path.replace(os.path.splitext(pdf_file_path)[1], "_summary.txt")
with open(pdf_summary_file, "w+") as file:
    file.write(pdf_summary_text)
pdf_file.close()


# pip install pypdf2
