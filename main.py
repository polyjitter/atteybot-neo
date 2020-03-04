# -*- coding: utf-8 -*-

# tacibase - a discord.py bot base with many goodies.
# All original work by taciturasa, with some code by ry00001.
# Used and modified with permission.
# See LICENSE for license information.

'''Main File'''

import discord
from discord.ext import commands
import traceback
import json
import os
import asyncio
import aiohttp
import random


class Bot(commands.Bot):
    """Custom Bot Class that subclasses the commands.ext one"""

    def __init__(self, **options):
        """Initializes the main parts of the bot."""

        super().__init__(self._get_prefix_new, **options)
        print('Performing initialization...\n')

        # Get Config Values
        with open('config.json') as f:
            self.config = json.load(f)
            self.prefix = self.config.get('PREFIX')
            self.version = self.config.get('VERSION')
            self.maintenance = self.config.get('MAINTENANCE')
            self.description = self.config.get('DESCRIPTION')

        # Get Instances
        with open('searxes.txt') as f:
            self.instances = f.read().split('\n')

        print('Initialization complete.\n\n')

    async def _get_prefix_new(self, bot, msg):
        """Full flexible check for prefix."""

        if isinstance(msg.channel, discord.DMChannel) and self.config['PREFIXLESS_DMS']:
            # Adds empty prefix if in DMs
            plus_none = self.prefix.copy()
            plus_none.append('')
            return commands.when_mentioned_or(*plus_none)(bot, msg)
        else:
            # Keeps regular if not
            return commands.when_mentioned_or(*self.prefix)(bot, msg)

    async def on_ready(self):
        """Initializes the main portion of the bot once it has connected."""

        # Prerequisites
        self.request = aiohttp.ClientSession()
        self.appinfo = await self.application_info()
        if self.description == '':
            self.description = self.appinfo.description

        # EXTENSION ENTRY POINT
        self.load_extension('extensions.core')

        # Logging
        msg = "CONNECTED!\n"
        msg += "-----------------------------\n"
        msg += f"ACCOUNT: {bot.user}\n"
        msg += f"OWNER: {self.appinfo.owner}\n"
        msg += "-----------------------------\n"
        print(msg)

    async def on_message(self, message):

        # Prerequisites
        mentions = commands.when_mentioned(bot, message)
        ctx = await self.get_context(message)

        # Handling
        if message.author.bot:
            # Turn away bots
            return
        elif message.author.id in self.config.get('BLOCKED'):
            # Ignore blocked users
            return
        elif self.maintenance and not message.author.is_owner():
            # Maintenance mode
            return
        elif message.content in mentions and self.config['MENTION_ASSIST']:
            # Empty ping for assistance
            assist_msg = (
                "**Hi there! How can I help?**\n\n"
                # Two New Lines Here
                f"You may use **{self.user.mention} `help`** for assistance.")
            await ctx.send(assist_msg)
        else:
            # Move on to command handling
            await self.process_commands(message)


bot = Bot(
    case_insensitive=True)


@bot.listen()
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        # Lets other cogs handle this.
        # Change this if you want command not found handling.
        return

    elif isinstance(error, commands.CommandInvokeError):
        # Provides a very pretty embed if something's actually a dev's fault.

        # Prerequisites
        error = error.original
        _traceback = traceback.format_tb(error.__traceback__)
        _traceback = ''.join(_traceback)
        appinfo = await bot.application_info()

        # Main Message
        embed_fallback = f"**An error occured: {type(error).__name__}. Please contact {appinfo.owner}.**"

        # Embed Building
        error_embed = discord.Embed(
            title=f"{type(error).__name__}",
            color=0xFF0000,
            description=(  # TODO Change if has logging
                "This is (probably) a bug. This has not been automatically "
                f"reported, so please give **{appinfo.owner}** a heads-up in DMs.")
        )

        # Formats Traceback
        trace_content = (
            "```py\n\nTraceback (most recent call last):"
            "\n{}{}: {}```").format(
                _traceback,
                type(error).__name__,
                error)

        # Adds Traceback
        error_embed.add_field(
            name="`{}` in command `{}`".format(
                type(error).__name__, ctx.command.qualified_name),
            value=(trace_content[:1018] + '...```')
            if len(trace_content) > 1024
            else trace_content)

        await ctx.send(embed_fallback, embed=error_embed)

    else:
        # If anything else goes wrong, just go ahead and send it in chat.
        await ctx.send(error)

bot.run(bot.config['TOKEN'])
