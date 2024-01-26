import os


async def is_creator(ctx):
    return bool(str(ctx.author.id) in [os.getenv("CREATOR_ID"), os.getenv("EMPTYCUPS_ID")])
