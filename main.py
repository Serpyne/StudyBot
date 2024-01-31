import discord
from src.classes import StudyBot
from src.server import Server

intents = discord.Intents.all()

app = Server(__name__)
app.start(host='0.0.0.0', port=8080)

study_bot = StudyBot(command_prefix=".",
                     case_insensitive=True, intents=intents)
study_bot.load_extensions("./cogs")
study_bot.begin()
