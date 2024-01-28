import os
import json
import datetime
import asyncio
import discord
from discord.ext import tasks, commands
from functions.get_settings import get_settings
from functions.delete_message import delete_message_in_channel


class StudyBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setup()

    def setup(self):
        @self.event
        async def on_ready():
            print("Scholar ready.")

    def load_extensions(self, path):
        for filename in os.listdir(path):
            if filename.endswith(".py"):
                self.load_extension(f"cogs.{filename[:-3]}")

    def begin(self):
        asyncio.run(self.start(os.getenv("TOKEN")))
