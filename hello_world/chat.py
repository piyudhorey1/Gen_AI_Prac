from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

#Zero-shot prompting example
SYSTEM_PROMPT = """
    You are a drinks making expert, who will assign user in making various drinks 
    which are either brewed or mixed using different ingredients. If the user asks
    about anything else, just decline them politely.
"""

client = OpenAI()

response1 = client.responses.create(
    model="gpt-5",
    input="Give five good names for a baby boy"
)

#print(response1.output_text)
response2 = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "Hey, my name is Piyush"},
        {"role": "user", "content": "How to write code in python for adding 2 numbers?"},
        {"role": "user", "content": "How to make a LIIT?"} 
    ]
)

print(response2.choices[0].message.content)

