import json
import discord
from discord.ext import commands
from functions.get_settings import get_settings, get_path
from functions.encryption import encode_id, decode_id
from functions.embed import SpecialEmbed


class LeaderboardCog(commands.Cog):

    @commands.slash_command(description=f"Who has studied the most?")
    async def leaderboard(self, ctx):
        LEADERBOARD_MAX_DISPLAY = get_settings("LEADERBOARD_MAX_DISPLAY")

        data = json.load(open(get_path("db"), "r"))
        users = {decode_id(x): data[x]["study_hours"] for x in data}

        embed = SpecialEmbed(title="Study Hours")

        first_users = sorted(users, key=lambda user: users[user], reverse=True)[
            :min(LEADERBOARD_MAX_DISPLAY, len(users.items()))]

        for i, user_id in enumerate(first_users):
            embed.add_field(
                name=f"{i+1}.",
                value=f"<@{user_id}>: {users[user_id]} hours", inline=False)

        await ctx.respond(embed=embed)

    @leaderboard.error
    async def leaderboard_error(self, ctx, error):
        print("Error in LeaderboardCog:", error)


def setup(bot):
    bot.add_cog(LeaderboardCog(bot))
