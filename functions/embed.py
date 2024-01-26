
import discord
from random import choice
from functions.get_settings import get_settings
from functions.format import format_seconds


class SpecialEmbed(discord.Embed):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.set_footer(text=self.random_note())

    def random_note(self):
        notes = f"""/help shows you all of my commands!
        /leaderboard shows the people with the most hours.
        /add <hours> adds hours to your user.
        You can only add hours every {format_seconds(get_settings("ADD_COOLDOWN"), verbose=True)}"""
        notes = notes.split("\n")

        note = choice(notes)
        note = " ".join(note.split())

        return "Note: " + note
