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

    @members.selection(emoji="plus")
    def add_members(self, ctx, message, reaction):
        ...

    @members.selection(emoji="minus")
    def remove_members(self, ctx, message, reaction):
        ...