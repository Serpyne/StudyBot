import json
import discord
from discord.ext import commands
from typing import Optional
from functions.get_settings import load_settings_dict, get_path
from functions.embed import SpecialEmbed
from functions.checks import is_creator


class SettingsCog(commands.Cog):
    @commands.slash_command(name="settings", description="Change settings.")
    @commands.check(is_creator)
    async def settings(self, ctx, setting: Optional[str], value: Optional[str]):
        settings_info = load_settings_dict("admin")
        settings_json = json.load(open(get_path("settings"), "r"))

        if not setting or not value or not value.isdigit() or setting not in settings_json.keys():

            embed = SpecialEmbed(title="How to change settings")
            for key, value in settings_info.items():
                embed.add_field(name=key, value=value, inline=True)

            await ctx.respond(embed=embed, ephemeral=True)
            return

        settings = json.load(open(get_path("settings"), "r"))
        settings[setting] = int(value)

        json.dump(settings, open(get_path("settings"), "w"),
                  indent=4, sort_keys=True)
        await ctx.respond(f"Set {setting} to {value}", ephemeral=True)

    @settings.error
    async def settings_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.respond("You don't have permission to use this command.", ephemeral=True)
            return

        print("Error in SettingsCog:", error)

    @commands.slash_command(name="log", description="Download logs of user activity.")
    @commands.check(is_creator)
    async def log_command(self, ctx):
        file = discord.File(get_path("log"))
        await ctx.respond(file=file, ephemeral=True)


def setup(bot):
    bot.add_cog(SettingsCog(bot))
