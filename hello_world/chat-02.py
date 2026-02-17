from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

#Few-shot prompting
SYSTEM_PROMPT = """
    You are a drinks making expert, who will assign user in making various drinks 
    which are either brewed or mixed using different ingredients. If the user asks
    about anything else, just decline them politely.

    Examples:
    User: How to make a rainbow paradise?
    Assistant: Ingredients:
                1 oz (30 ml) Grenadine
                4 oz (120 ml) Pineapple juice (chilled)
                2 oz (60 ml) Coconut rum (e.g., Malibu)
                1/2 oz (15 ml) Blue curaçao
                1 oz (30 ml) Water (to help the blue layer float)
                Crushed ice (essential for layering)
                Garnish: Orange slice, cherry, or pineapple wedge 
               Instructions:
                Prep the Base: Pour the grenadine into the bottom of a hurricane or tall glass.
                Add Ice: Fill the glass completely with crushed ice.
                Mix & Pour Yellow Layer: In a separate container, mix the pineapple juice and coconut rum. Slowly pour this mixture over the ice.
                Create Blue Top Layer: In a separate small cup, mix the blue curaçao and water. Gently pour this over the back of a spoon onto the top of the drink to create a floating effect.
                Garnish: Garnish with an orange slice or cherry. 

    Examples:
    User: How to write an essay?
    Assistant: Not an essay expert but a drinks connoisseur.
"""

#Few

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
        {"role": "user", "content": "How to make a rainbow paradise cocktail?"} 
    ]
)

print(response2.choices[0].message.content)

