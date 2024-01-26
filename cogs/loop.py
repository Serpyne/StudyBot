import json
import os
from datetime import datetime
from discord.ext import tasks, commands
from functions.cooldown import increment_cooldown
from functions.get_settings import get_settings, get_path


class LoopCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        @bot.listen()
        async def on_ready():
            try:
                self.mainloop.start()
            except RuntimeError:
                pass

    def cog_unload(self):
        self.printer.cancel()

    def get_ticks(self) -> float:
        return (datetime.now() - datetime(1970, 1, 1)).total_seconds()

    def backup_db(self):
        db = json.load(open(get_path("db"), "r"))
        filename = f"backup{len(os.listdir("./backups")) + 1}.json"
        with open("./backups/" + filename, "w") as f:
            json.dump(db, f, indent=4, sort_keys=True)

    @tasks.loop(seconds=1.0)
    async def mainloop(self):
        increment_cooldown(1)

        # Backup user date every x amount of seconds
        backup_interval = get_settings("BACKUP_INTERVAL")
        tick = self.get_ticks()
        if (int(tick) % backup_interval) == 0:
            self.backup_db()


def setup(bot):
    bot.add_cog(LoopCog(bot))
