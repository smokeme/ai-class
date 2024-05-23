import os
import requests

openai_api_key = ""


headers = {
    'Content-Type': 'application/json',
    'Authorization': f"Bearer {openai_api_key}"
}

json_data = {
    'model': 'dall-e-3',
    'prompt': 'a white siamese cat',
    'n': 1,
    'size': '1024x1024',
}

response = requests.post('https://api.openai.com/v1/images/generations', headers=headers, json=json_data)
image = response.json()['data'][0]['url']

def download_image(url, filename):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Ensure the request was successful
    if response.status_code == 200:
        # Open a file in write-binary mode and write the content
        with open(filename, 'wb') as file:
            file.write(response.content)
        print(f"Image successfully downloaded: {filename}")
    else:
        print(f"Failed to retrieve image. HTTP Status code: {response.status_code}")

download_image(image,"myimage.png")
