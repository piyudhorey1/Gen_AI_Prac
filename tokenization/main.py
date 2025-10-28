import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

text = "Hello, I am piyush dhorey"

token = enc.encode(text)
print("Token: ", token)

token = [13225, 11, 357, 939, 173566, 1776, 8523, 510, 88]

decodeText = enc.decode(token)
print("Decoded: ", decodeText)