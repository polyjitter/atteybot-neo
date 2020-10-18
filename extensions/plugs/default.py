# -*- coding: utf-8 -*-

# attey default plug
# Default entries in any room panel.

'''Plugging File'''

import discord
from discord.ext import commands
import rethinkdb
from extensions.utils import plugging


class DefaultPlug():
    """Default entries in any room panel."""

    def __init__(self, bot):
        self.bot = bot
        self.conn = bot.conn

    @plugging.entry()
    def members(self, ctx):
        return "Add or remove members."

    @members.selection(emoji="plus", type="entry")
    def add_members(self, ctx, message, reaction):
        ...

    @members.selection(emoji="minus", type="entry")
    def remove_members(self, ctx, message, reaction):
        ...

    @plugging.entry()
    def access(self, ctx):
        return "Set the access level of this room."

    @access.selection(emoji="open_lock", type="exclusive")
    def open_room(self, ctx, message, reaction):
        ...

    @access.selection(emoji="closed_lock", type="exclusive")
    def locked_room(self, ctx, message, reaction):
        ...

    @access.selection(emoji="no_view", type="exclusive")
    def unlisted_room(self, ctx, message, reaction):
        ...