from discord.ext import commands


async def delete_message_in_channel(bot: commands.Bot, guild_id: int, channel_id: int, *message_ids: int):
    """
    Pass in discord.ext.commands.Bot object, guild id and channel id, and message ids. All of the message ids must be in the same channel.
    """
    guild = await bot.fetch_guild(guild_id)
    channel = await guild.fetch_channel(channel_id)
    for message_id in message_ids:
        message = await channel.fetch_message(message_id)
        await message.delete()
