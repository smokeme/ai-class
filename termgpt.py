import os
import requests
import pprint

openai_api_key = "sk-proj-"

# Function to generate text using OpenAI GPT
def generate_commands(prompt):
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
                "content": "Your name is Skynet, you are a helpful terminal assistant, you will only respond in Windows terminal (cmd) commands to achieve the results the user wants either by creating files, removing etc... do not wrap them with markdown as anything you return will be treated as a command, Also make everything into a single line of command, if you need to create a new file for something else or execute some other command that you can't in one line add a new line seperator '\n'"
            },
            {
                "role": "user",
                "content": f"Do the following: {prompt}"
            }
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    return response.json()['choices'][0]['message']['content']

task = input("What commands do you want to run?: ")
commands = generate_commands(task)
for single_cmd in commands.split("\n"):
    print(single_cmd)
    os.system(single_cmd)
