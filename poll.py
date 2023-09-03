import discord
import graphics


# defines buttons to use in the poll
class PollButton(discord.ui.Button):
    message = ''
    count = 0

    def __init__(self, message):
        super().__init__(label=message, style=discord.ButtonStyle.primary)
        self.message = message

    # defines the behavior after a user clicks a poll button (returns user choice and increments poll)
    async def callback(self, interaction: discord.Interaction):
        # Use the interaction object to send a response message containing
        # the user's choice and increment the poll
        # self.style = discord.ButtonStyle.grey
        self.count += 1
        # user = interaction.user.id
        # await user.send(f'Your choice is {self.message}')
        await interaction.response.send_message(f'Your choice is {self.message}')


class Poll(discord.ui.View):

    def __init__(self, ctx, question: str, args: list, timeout):
        super().__init__(timeout=timeout)
        self.question = question
        self.ctx = ctx
        for choice in args:
            self.add_item(PollButton(choice))

    async def on_timeout(self):
        await self.ctx.send(self.question)
        for item in self.children:
            await self.ctx.send(f'{item.message}: {item.count} votes')
