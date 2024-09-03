import openai
import os

openai.api_key = "sk-proj-"

def load_text(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def split_text(text):
    max_chunk_size = 2048
    chunks = []
    current_chunk = ""
    for sentence in text.split("."):
        if len(current_chunk) + len(sentence) < max_chunk_size:
            current_chunk += sentence + "."
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence + "."
    if current_chunk:
        chunks.append(current_chunk.strip())
    return chunks  

def generate_summary(text):
    input_chunks = split_text(text)
    #input_chunks = input_chunks[1:2]
    output_chunks = []
    for chunk in input_chunks:
        response = 	openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages = 
                [
                    # {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": f"summarize the following text and create a title  in Turkish:\n{chunk}\n\n  Summary: "},
                ],

            #prompt=(f"summarize the following text and create a title  in Turkish:\n{chunk}\n\n  Summary: "),
            temperature=0.2,
            max_tokens=2048,
            n = 1,
            stop=None
        )
        summary = response.choices[0].message.content.strip()
        print(f"chunk:-->{chunk},summary: --> {summary}")
        output_chunks.append(summary)
    return " ".join(output_chunks)