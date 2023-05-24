import discord
import random

from discord import app_commands
from discord.ext import commands
import responses

async def send_message(message, user_message):
    try:
        response = responses.handle_responses(user_message)
    except Exception as e:
        print(e)

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

    bot.run(TOKEN)