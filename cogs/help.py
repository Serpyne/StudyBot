import json
import discord
from discord.ext import commands
from typing import Optional
from functions.get_settings import load_settings_dict
from functions.embed import SpecialEmbed


class HelpCog(commands.Cog):
    @commands.slash_command(name="help", description=f"All commands.")
    async def help_command(self, ctx, command: Optional[str]):
        settings_info = load_settings_dict("basic")

        embed = SpecialEmbed()
        if command:
            for key in settings_info.keys():
                if "/"+command in key:
                    embed.title = key
                    embed.description = settings_info[key]
                    break
            if embed.description:
                await ctx.respond(embed=embed, ephemeral=True)
                return

        embed.title = "Commands"
        for key, value in settings_info.items():
            embed.add_field(name=key, value=value)

        await ctx.respond(embed=embed, ephemeral=True)

    @help_command.error
    async def help_error(self, ctx, error):
        print("Error in HelpCog:", error)


def setup(bot):
    bot.add_cog(HelpCog(bot))
