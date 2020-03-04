import discord
# import rethinkdb
import typing as t
from models import panels
import peewee

class Panel():
    """Represents a panel channel in @rcade."""
    
    def __init__(self, channel: discord.TextChannel):
        self.channel = channel

    def add_settings(self, plug):
        """Adds setting to panel and channel."""
        # TODO This stuff lol
        ...

    async def delete(self):
        """Deletes panel and relevant rethinkdb entries."""
        await self.channel.delete()
