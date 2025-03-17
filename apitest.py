from openai import OpenAI
client = OpenAI(api_key="")

response = client.images.generate(
    model="dall-e-2",
    prompt="An album cover, with no text that has the following themes: Scary, Metal, Dark",
    size="1024x1024",
    quality="standard",
    n=1,
)

print(response.data[0].url)