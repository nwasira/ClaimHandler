from datetime import datetime
import random
import time
import asyncio
import nextcord
from nextcord.ext import commands
from nextcord.ext.commands.cooldowns import BucketType
from server import keep_alive
import os
 
my_secret = os.environ['TOKEN']
class Dropdown(nextcord.ui.Select):
    def __init__(self):
        options = [
            nextcord.SelectOption(
                label="$25 Robux Giftcard", description="Redeem a $25 Robux Giftcard for 3 Invites", emoji="<:giftcard1:1197954121811120270>"
            ),
            nextcord.SelectOption(
                label="$50 Robux Giftcard", description="Redeem a $50 Robux Giftcard for 6 Invites", emoji="<:giftcard1:1197954121811120270>"
            ),
            nextcord.SelectOption(
                label="$75 Robux Giftcard", description="Redeem a $75 Robux Giftcard for 9 Invites", emoji="<:giftcard1:1197954121811120270>"
            ),
            nextcord.SelectOption(
                label="$100 Robux Giftcard", description="Redeem a $100 Robux Giftcard for 12 Invites", emoji="<:giftcard1:1197954121811120270>"
            ),
        ]
        super().__init__(
            placeholder="Select your reward!",
            min_values=1,
            max_values=1,
            options=options,
        )
 
    async def callback(self, interaction: nextcord.Interaction):
        e = nextcord.Embed(title = "Processing..", description = f"<:alert2:1019659532923850814> Our administrators are currently confirming your invites.\nPlease do not leave the DM channel, as this will only take a few seconds.", colour = 16754176,  timestamp=datetime.utcnow())
        i = nextcord.Embed(title = "Error!", description = f"<:alert:1019659505199493200> It seems some of your invites left the server.\nPlease invite `2` more users so that you are eligible to claim!", colour = 16724787,  timestamp=datetime.utcnow())
        n = nextcord.Embed(title = "Error!", description = f"<:alert:1019659505199493200> It seems some of your invites left the server.\nPlease invite `2` more users so that you are eligible to claim!", colour = 16724787,  timestamp=datetime.utcnow())
        x = random.randint(1,50)
        if x > 35:
            
            await interaction.response.send_message(embed = e)
            await asyncio.sleep(6)
            await interaction.send(embed = i)
        else:
            await interaction.response.send_message(embed = e)
            await asyncio.sleep(6)
            await interaction.send(embed = n)           
class DropdownView(nextcord.ui.View):
    def __init__(self):
        super().__init__()
 
        self.add_item(Dropdown())
 
intents = nextcord.Intents.all()
client = commands.Bot(command_prefix = '!',owner_id = 1167206036264996946, intents=intents)
client.remove_command('help')
 
@client.event
async def on_ready():
    print("======================================")
    print(f"             Logged in as {client.user}")
    print("======================================")
 
@client.command()
@commands.cooldown(1,300,commands.BucketType.user)
async def claim(ctx):
    """Sends a message with our dropdown containing colours"""
    print(f"{ctx.author} used the command")
 
    view = DropdownView()
 
    e = nextcord.Embed(title = "Hey there!", description = f"Thank you for contacting our administration team to claim your prize!\nIf you click the drop down menu below, you can select a reward! <:rbx:1197954199179243580>", colour=40191, timestamp=datetime.utcnow())
    await ctx.send(embed = e, view=view)
 
@claim.error
async def claim_error(ctx, error):
    if isinstance(error, nextcord.ext.commands.errors.CommandOnCooldown):
        prize = nextcord.Embed(title = "Woah there!", description = f"This command is currently on cooldown!\nYou're currently being ratelimited, please try again later.", colour = 40191,  timestamp=datetime.utcnow())
        await ctx.send(embed = prize)
 
keep_alive()
client.run(my_secret)