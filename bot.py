import asyncio
import datetime
import random
import time
from datetime import datetime
import discord
import json
import discord
from discord.ext import commands

##########################################
client = commands.Bot(command_prefix=commands.when_mentioned_or('.'))
TOKEN = ''

client.remove_command('help')

################################################################

@client.event
async def on_ready():
    print(f"Logged in! - User-ID: {client.user.id}")
    await status_task()


async def status_task():
    await client.change_presence(
        activity=discord.Activity(name='02#2000', type=discord.ActivityType.playing))

@client.event
async def on_member_join(member):
    days = 7
    channel_id = 123
    server_id = 123
    server = member.guild
    user = list(member1.bot for member1 in home.members if member1.bot is False)
    member_days = (datetime.now() - member.created_at).days
    if days >= member_days:
        member_passed1 = (datetime.now() - member.joined_at).days
        member_created1 = (datetime.now() - member.created_at).days
        embed = discord.Embed(title="{}'s info".format(member.name),
                                  description="Recognized a new account",
                                  color=0x7289DA)
        embed.add_field(name="Name", value=f"{member}|{member.id}", inline=True)
        embed.add_field(name="Server:", value=server, inline=True)
        embed.add_field(name="Joined at:", value=(
                "{} ({} days ago!)".format(member.joined_at.strftime("%d %b %Y %H:%M"), member_passed1)), inline=False)
        embed.add_field(name="Created at:", value=(
                "{} ({} days ago!)".format(member.created_at.strftime("%d %b %Y %H:%M"), member_created1)),
                            inline=False)
        embed.set_thumbnail(url=member.avatar_url)
        channel = client.get_channel(channel_id)
        await channel.send(embed=embed)
        if server.id == server_id: 
                role1 = server.get_role(734732831409963149)
                await member.add_roles(role1)
                embed = discord.Embed(title=f"Hi {member}!",
                                          description="Your account is new to discord! You have been added in a security control.",color=discord.Color.red())
                try:
                    await member.send(embed=embed)
                except discord.Forbidden:
                    pass
bot.run(TOKEN)
