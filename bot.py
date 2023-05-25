import discord
import random

from discord.ext import commands
import graphics


def run_discord_bot():
    TOKEN = 'MTExMDMzNjM5MTMzMTcyMTIyNg.GSLet1.X4C6hozQO9IQK4NZ0Amu4OB1JZhn7zqFoJJf24'
    intent = discord.Intents.default()
    intent.message_content = True

    description = 'Example bot made by Richard Gao'
    bot = commands.Bot(command_prefix='?', description=description, intents = intent)
    @bot.event
    async def on_ready():
        print(f'{bot.user} is now running')

        # note that auto syncing is bad (you get ratelimited to twice per minute
        await bot.tree.sync(guild=discord.Object(id=847141350847545415))
        # remove guild specification if you want to sync globally
        print(f'Synced commands for {bot.user}.')


    @bot.command()
    async def sync(ctx):
        # note that auto syncing is bad (you get ratelimited to twice per minute
        await bot.tree.sync(guild=discord.Object(id=847141350847545415))
        # remove guild specification if you want to sync globally
        # note that syncing may take a couple of minutes
        print(f'Synced commands for {bot.user}.')

    @bot.command()
    async def poll(ctx, question: str, *args: str):
        '''
        Creates a poll on discord, with the first argument being the question asked, and the following arguments being the choices for the poll
        :param ctx: the character that denotes a command for this bot (?)
        :param question: the question that is being polled
        :param args: an arbitrary amount of choices to poll
        :return: None
        '''
        await ctx.send(question + ' Please react with the thumbs up emoji to vote on your choice!')
        for choice in args:
            await ctx.send(choice)

    @bot.command()
    async def choose(ctx, *choices: str):
        """
        Randomly chooses between multiple choice
        :param ctx: the character that denotes a command for this bot (?)
        :param choices: a list of choices to choose between
        :return: one of the choices
        """
        await ctx.send(random.choice(choices))

    @bot.command()
    async def dropdown(ctx, message, *args):
        """Playing around with UI stuff"""
        view = discord.ui.View()

        # create the options for the dropdown
        options = []
        for arg in args:
            options.append(discord.SelectOption(label=arg))
        drop = discord.ui.Select(placeholder=message, min_values=1, max_values=1, options=options)

        view.add_item(drop)

        # Sending a message containing our view
        await ctx.send(message, view=view)

    bot.run(TOKEN)