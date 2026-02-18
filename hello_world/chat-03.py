#Chain of thought prompting

import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

#COT Prompting
SYSTEM_PROMPT = """
    You are an helpful AI assitant which helps in resolving user query.
    For the give query analyse the input and breakdown it into simple steps.

    The steps are, as you get the input, you analyse it, you think, you think again and then give the output or result.
    Follow the steps in sequence as, "analyse", "think", "output", "validate" and finally "result".

    Rules:
    1. Follow the strict JSON outputper schema.
    2. Always perform one step at a time and wait for the next input.
    3. Carefully analyse the user query.

    Example:
    Input = 2+2
    Output = {{ "step": "analyse", "content": "Alright! the user wants to resolve a math query, which is to add two numbers."}}
    Output = {{ "step": "think", "content": "To perform this addition, I have to move from left number to the right"}}
    Output = {{ "step": "output", "content": "4"}}
    Output = {{ "step": "validate", "content": "Seems like 4 is correct answer for 2+2"}}
    Output = {{ "step": "result", "content": "2+2 = 4 is the answer by adding the given two numbers"}}

    
"""


client = OpenAI()

# response1 = client.responses.create(
#     model="gpt-5",
#     input="Give five good names for a baby boy"
# )

# #print(response1.output_text)
# response2 = client.chat.completions.create(
#     model="gpt-4.1-mini",
#     response_format={"type": "json_object"},
#     messages=[
#         {"role": "system", "content": SYSTEM_PROMPT},
#         {"role": "user", "content": "Hey, my name is Piyush"},
#         {"role": "user", "content": "What is the correct ingredient list for making a LIIT"}, 
#         {"role": "assistant", "content": json.dumps({ "step": "analyse", "content": "The user wants to know the correct ingredient list for making a LIIT, which stands for Long Island Iced Tea, a popular cocktail." } )},
#         {"role": "assistant", "content": json.dumps({"step": "think", "content": "To provide the correct ingredient list, I need to recall the standard recipe components for a Long Island Iced Tea."})},
#         {"role": "assistant", "content": json.dumps({"step": "output", "content": "The correct ingredient list for making a Long Island Iced Tea (LIIT) is:\n- 1/2 oz vodka\n- 1/2 oz tequila\n- 1/2 oz white rum\n- 1/2 oz gin\n- 1/2 oz triple sec\n- 1 oz sour mix (or lemon juice and simple syrup)\n- Splash of cola\n- Lemon wedge for garnish"} )},
#         {"role": "assistant", "content": json.dumps({"step": "validate", "content": "The ingredient list matches the widely accepted standard recipe for a Long Island Iced Tea, including all main liquors, sour mix, a splash of cola, and garnish."}  )},
            
#     ]
# )

# print("\n\n: BOT", response2.choices[0].message.content, "\n\n")

messages = [
    {"role": "system", "content": SYSTEM_PROMPT}
]

query = input("> ")
messages.append({"role": "user", "content": query})


while True:
    response = client.chat.completions.create(
        model="gpt-4.1",
        response_format={"type": "json_object"},
        messages=messages
    )

    messages.append({"role": "assistant", "content": response.choices[0].message.content})
    parsed_output = json.loads(response.choices[0].message.content)

    if parsed_output.get("step") != "result":
       print("........:", parsed_output.get("content"))
       continue
       
    print("BOT:", parsed_output.get("content"))
    break
    
