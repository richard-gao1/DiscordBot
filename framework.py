import discord
import random

from discord.ext import commands
import graphics


def run_discord_bot():
    TOKEN = '[INSERT YOUR BOT TOKEN HERE]'
    # you can change your intents here if you want to customize them
    intent = discord.Intents.default()
    intent.message_content = True

    description = 'Discord Bot Framework code made by Richard Gao and Albert Zhu'
    bot = commands.Bot(command_prefix='?', description=description, intents=intent)

    @bot.event
    async def on_ready(): # command will run once bot turns on
        print(f'{bot.user} is now running')

        # note that auto syncing is bad (you get ratelimited to twice per minute
        await bot.tree.sync(guild=discord.Object(id=847141350847545415))
        # remove guild specification if you want to sync globally
        print(f'Synced commands for {bot.user}.')

    @bot.command()
    async def sync(ctx): # used to sync commands while bot is running
        # note that auto syncing is bad (you get ratelimited to twice per minute
        await bot.tree.sync(guild=discord.Object(id=847141350847545415))
        # remove guild specification if you want to sync globally
        # note that syncing may take a couple of minutes
        print(f'Synced commands for {bot.user}.')

    @bot.command()
    async def function(ctx): # basic framework
        # TODO: function body
        pass

    ### UI STUFF ###

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

    @bot.command()
    async def button(ctx, message):

        # Define a simple View that gives us a counter button
        class Counter(discord.ui.View):

            # Define the actual button
            # When pressed, this increments the number displayed until it hits 5.
            # When it hits 5, the counter button is disabled and it turns green.
            # note: The name of the function does not matter to the library
            @discord.ui.button(label='0', style=discord.ButtonStyle.red)
            async def count(self, interaction: discord.Interaction, button: discord.ui.Button):
                number = int(button.label) if button.label else 0
                if number + 1 >= 5:
                    button.style = discord.ButtonStyle.green
                    button.disabled = True
                button.label = str(number + 1)

                # Make sure to update the message with our updated selves
                await interaction.response.edit_message(view=self)

        # Define a View that will give us our own personal counter button
        class EphemeralCounter(discord.ui.View):
            # When this button is pressed, it will respond with a Counter view that will
            # give the button presser their own personal button they can press 5 times.
            @discord.ui.button(label='Click', style=discord.ButtonStyle.blurple)
            async def receive(self, interaction: discord.Interaction, button: discord.ui.Button):
                # ephemeral=True makes the message hidden from everyone except the button presser
                await interaction.response.send_message('Enjoy!', view=Counter(), ephemeral=True)

        await ctx.send('Press!', view=EphemeralCounter())

    # actually runs the bot
    bot.run(TOKEN)
