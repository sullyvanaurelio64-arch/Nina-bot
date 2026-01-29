print("Iniciando bot...")

import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = bot = commands.Bot(
    command_prefix="!",
    intents=intents,
    help_command=None
)

@bot.event
async def on_ready():
    print("Mini Loritta online 😎")

@bot.command()
async def ping(ctx):
    await ctx.send("pong 🏓")




@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content.lower() == "oi":
        await message.channel.send("oi acordei papo de estampa de camisa 😎")

    await bot.process_commands(message)
@bot.command()
async def ajuda(ctx):
    await ctx.send(
        "**🤖 Mini Loritta – Comandos**\n"
        "• `!ping` – ver se tô viva 🏓\n"
        "• diga `oi` – resposta aleatória 😎\n"
        "• `!acorda` – acordar o bot 🔥"
    )
@bot.command()
async def acorda(ctx):
    await ctx.send("ACORDEI PAPO DE ESTAMPA DE CAMISA 🔥😎")
@bot.command()
async def avatar(ctx, membro: discord.Member = None):
    if membro is None:
        membro = ctx.author

    embed = discord.Embed(
        title=f"Avatar de {membro.name}",
        color=discord.Color.purple()
    )
    embed.set_image(url=membro.display_avatar.url)

    await ctx.send(embed=embed)

bot.run("MTQ2NjQ0ODczMjM1MzQ2MjUxNw.GN2H5z.GZ85Ukkbd7s-pPdnmxp7JCP4ssGVX6YfJ-dFcE")
import random

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    respostas_oi = [
        "oi acordei papo de estampa de camisa 😎",
        "bom dia dorminhoco 😴",
        "fala tu 😏",
        "salveee 🔥",
        "cheguei agora e já tô online 🤖"
    ]

    if message.content.lower() == "oi":
        await message.channel.send(random.choice(respostas_oi))

    await bot.process_commands(message)
