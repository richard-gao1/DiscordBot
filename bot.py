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

        # Defines a custom Select containing colour options
        # that the user can choose. The callback function
        # of this class is called when the user changes their choice
        class Dropdown(discord.ui.Select):
            def __init__(self):
                # create the options for the dropdown
                options = []
                for arg in args:
                    options.append(discord.SelectOption(label=arg))

                # The placeholder is what will be shown when no option is chosen
                # The min and max values indicate we can only pick one of the three options
                # The options parameter defines the dropdown options. We defined this above
                super().__init__(placeholder=message, min_values=1, max_values=1,
                                 options=options)

            async def callback(self, interaction: discord.Interaction):
                # Use the interaction object to send a response message containing
                # the user's favourite colour or choice. The self object refers to the
                # Select object, and the values attribute gets a list of the user's
                # selected options. We only want the first one.
                await interaction.response.send_message(f'Your choice is {self.values[0]}')


        drop = Dropdown()
        view.add_item(drop)

        # Sending a message containing our view
        await ctx.send(message, view=view)

    bot.run(TOKEN)