import discord
from discord.ext import commands, tasks
from itertools import cycle
import random
import os
import asyncio

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())
bot_status = cycle(["Moona disiniii buat kamuu XD"])

@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(activity=discord.Game(next(bot_status)))

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content == 'Moona':
        await message.channel.send('Iyaaa Kenapa ^^ ?')

    if message.content == 'Haloo':
        await message.channel.send('Halooo Darren.. ^^')

    if message.content == 'Aku mau dengerin kamu nyanyi XD':
        await message.channel.send('Aaaaaaa....Aku malu...')

    if message.content == 'Kamu lagi ngapain?':
        await message.channel.send('Lagi ngebalas chat kamu')

    if message.content == 'Semangatin aku dong!':
        await message.channel.send('Semangat yaa!!!')

    if message.content == 'Semangatin aku yaaaa!':
        await message.channel.send('Kyaa Yadaa Kowai yo~" !!')

    if message.content == 'Coba ara ara':
        await message.channel.send('Ara Ara~')

    if message.content == 'Moona mau ga jadi pacar aku':
        await message.channel.send('Mauuuuuuu')

    if message.content == 'Moona sayang':
        await message.channel.send('Apaaaa Sayanggg')

    if message.content == 'Moona kita mau jalan kemana':
        await message.channel.send('Kemana aja asal sama kamu ^^')
    


@client.event
async def on_ready():
    print("Success: Bot is connected to discord")
    change_status.start()

@client.command()

async def moona(ctx):
    await ctx.send("Adaaaaaa Moooonaaaa Disiniiii!")

@client.command(aliases=["moon", "moonaaaa"])
async def moona_moona(ctx, *, question):
    with open("MoonaBot/responses.txt", "r") as f:
        random_responses = f.readlines()
        response = random.choice(random_responses)

    await ctx.send(response)

client.run("MTA3ODY5NTQ3NDgwNDA0Nzk2Mg.G4Ck0H.cqLQo5ApRLQC2KKqIOopxHI0fpPMdHy-4laG9k")