# -*- coding: utf-8 -*-

# attey plugging util
# Provides utils for dealing with plugs and entries inside panels.

'''Plugging File'''

import discord
from discord.ext import commands
import rethinkdb
from extensions.utils import logging

def entry():
    def inner():
        ...
    return inner

def selection():
    def inner():
        ...
    return inner

def deselection():
    def inner():
        ...
    return inner

class Plugging():
    """Deals with plugs and entries inside panels."""

    def __init__(self, bot):
        self.bot = bot
        self.conn = bot.conn

    async def add_plug(self, 
                       panel_channel: discord.TextChannel, 
                       plug_name: str):
        """Adds a plug to a panel."""
        ...

    async def remove_plug(self, 
                          panel_channel: discord.TextChannel, 
                          plug_name: str):
        """Removes a plug from a panel."""
        ...
    
    async def parse_reaction(self, reaction):
        """Parses a reaction on an entry."""
        ...

def setup(bot):
    bot.plugging = Plugging(bot)