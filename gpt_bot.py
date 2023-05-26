# Discord API
from dotenv import load_dotenv
import discord
import os
import openai

load_dotenv()

# discord_token = os.getenv('DISCORD_TOKEN')
discord_token = ""


class MyClient(discord.Client):
    async def on_ready(self):
        print("Successfully logged in as ", self.user)

    async def on_message(self, message):
        print("Message Content: ", message.content)
        if message.author == self.user:
        # if self.user:
            return
        command, user_message = None, None

        # for text in ['/ai', '/bot', '/chatgpt']:
        for text in ['/', '/ ', '/ai', '/bot', '/chatgpt']:
            if message.content.startswith(text):
                command = message.content.split(' ')[0]
                user_message = message.content.replace(text, '')
                print('command, user message: ', command, user_message)

        if command == '/' or command == '/ ' or command == '/ai' or command == '/bot' or command == '/chatgpt':
            bot_response = chatgpt_response(prompt=user_message)
            await message.channel.send(f"Answer: {bot_response}")


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)

# chatgpt_response function

# from dotenv import load_dotenv
# import openai
# import os

# load_dotenv()

# openai.api_key = os.getenv('CHATGPT_API_KEY')
openai.api_key = ""


def chatgpt_response(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=300
    )

    response_dict = response.get("choices")
    if response_dict and len(response_dict) > 0:
        prompt_response = response_dict[0]["text"]
    return prompt_response
