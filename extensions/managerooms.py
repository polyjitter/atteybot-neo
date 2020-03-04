import discord
from discord.ext import commands
import typing as t
import traceback
from extensions.models import rooms


class ManageRooms(commands.Cog, name="Rooms"):

    def __init__(self, bot):
        self.bot = bot
        self.conn = bot.conn

    @commands.command(name='create')
    async def create_room(self, ctx,
                          members: commands.Greedy[discord.Member] = [],
                          name: t.Optional[str] = None):
        """Create a new room."""


        message = await ctx.send(":typing: Creating room...")

        room = rooms.Room(
            owner=ctx.author, name=name, members=members)

        await room.construct(ctx.guild)

        await message.edit(content="Room created!")

    @commands.command(name='delete')
    async def delete_room(self, ctx):
        """Delete a room."""
        # TODO Call a wipe and then delete from memory
        ...

    @commands.command(name='add')
    async def add_members(self, *members: discord.Member):
        """Add members to a room."""
        ...


def setup(bot):
    bot.add_cog(ManageRooms(bot))