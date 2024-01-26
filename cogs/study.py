import json
import discord
from discord.ext import commands
from functions.get_settings import get_settings, get_path
from functions.encryption import encode_id, decode_id
from functions.log import log_message
from functions.embed import SpecialEmbed
from functions.checks import is_creator


class StudyCog(commands.Cog):

    def set_study_hours(self, user_id, value):
        db = json.load(open(get_path("db"), "r"))

        key = encode_id(user_id)
        if key in db:
            db[key]["study_hours"] = value
        else:
            db[key] = {"study_hours": value, "add_cooldown": 0}

        json.dump(db, open(get_path("db"), "w"), indent=4, sort_keys=True)

    def get_add_cooldown(self, user_id):
        db = json.load(open(get_path("db"), "r"))

        key = encode_id(user_id)
        if key not in db:
            return None
        else:
            return db[key]["add_cooldown"]

    def set_add_cooldown(self, user_id, value):
        db = json.load(open(get_path("db"), "r"))

        key = encode_id(user_id)
        if key in db:
            db[key]["add_cooldown"] = value
        else:
            db[key] = {"study_hours": value, "add_cooldown": 0}

        json.dump(db, open(get_path("db"), "w"), indent=4, sort_keys=True)

    def get_study_hours(self, user_id):
        db = json.load(open(get_path("db"), "r"))

        key = encode_id(user_id)
        if key not in db:
            return None
        else:
            return db[key]["study_hours"]

    @commands.slash_command(description=f"Gives yourself study hours.")
    async def add(self, ctx, value):
        settings = get_settings()
        ADD_LIMIT = settings["ADD_LIMIT"]
        ADD_COOLDOWN = settings["ADD_COOLDOWN"]

        embed = SpecialEmbed()

        user_id = ctx.author.id
        if not value:
            embed.title = "No value provided."
            await ctx.respond(embed=embed, ephemeral=True)
            return

        elif not value.isdigit():
            embed.title = "Invalid value provided."
            await ctx.respond(embed=embed, ephemeral=True)
            return

        value = int(value)
        if value > ADD_LIMIT:
            embed.title = f"That's too many hours (Limit is {ADD_LIMIT})."
            await ctx.respond(embed=embed, ephemeral=True)
            return

        cooldown = self.get_add_cooldown(user_id)
        if cooldown is not None:
            if cooldown > 0:
                embed.title = f"You can add study hours in {cooldown} seconds"
                await ctx.respond(embed=embed, ephemeral=True)
                return

        if value < 1:
            embed.title = "Provide a positive number."
            await ctx.respond(embed=embed, ephemeral=True)
            return

        hours = self.get_study_hours(user_id)
        if not hours:
            self.set_study_hours(user_id, int(value))
        else:
            self.set_study_hours(user_id, int(hours) + int(value))

        self.set_add_cooldown(user_id, ADD_COOLDOWN)

        log_message(f"[{ctx.author.name}] added {value} hours")

        embed.title = f"Added {value} hour to {ctx.author.name}"
        await ctx.respond(embed=embed)

    @add.error
    async def add_error(self, ctx, error):
        print("Error in StudyCog:", error)

    @commands.slash_command(name="set", description="Set hours.")
    @commands.check(is_creator)
    async def set_hours(self, ctx, user: discord.Member, value):
        embed = SpecialEmbed()
        if not value.isdigit():
            embed.title = "Invalid value provided."
            await ctx.respond(embed=embed, ephemeral=True)
            return

        self.set_study_hours(user.id, int(value))
        log_message(f"[{ctx.author.name}] set {user.name} to {value} hours")

        embed.title = f"Set {user.name} to {value} hours"
        await ctx.respond(embed=embed)

    @set_hours.error
    async def set_error(self, ctx, error):
        await ctx.respond("You don't have permission to use this command.", ephemeral=True)


def setup(bot):
    bot.add_cog(StudyCog(bot))
