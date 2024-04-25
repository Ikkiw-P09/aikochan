import discord
import os
import keep_alive

from discord.ext import commands

import discord
from discord.ext import commands
import datetime
from discord.app_commands import command
from discord import app_commands

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

TOKEN=os.getenv(TOKEN)

def get_thai_date():
  today = datetime.date.today()
  day = today.strftime('%d')
  month_th = {1: "มกราคม", 2: "กุมภาพันธ์", 3: "มีนาคม", 4: "เมษายน", 5: "พฤษภาคม", 6: "มิถุนายน",
              7: "กรกฎาคม", 8: "สิงหาคม", 9: "กันยายน", 10: "ตุลาคม", 11: "พฤศจิกายน", 12: "ธันวาคม"}
  month_th_name = month_th[today.month]
  year = today.year
  return f"{day} {month_th_name} {year}"

@bot.event
async def on_ready():
    activity = discord.Game(name="Hi! I'm AikoChan!", type=3)
    await bot.change_presence(status=discord.Status.dnd, activity=activity)
    print("Active")
    await bot.tree.sync()

@bot.command()
async def ping(ctx):
    await ctx.send(f"Hi!")

@bot.tree.command(name="announce", description="Create new announcement")
async def announcecmd(interaction, title : str, author : str, msg : str):
    thai_date = get_thai_date()
    channel = bot.get_channel(1231985038401343519)
    await channel.send(f"@everyone\n————————————\n**ประกาศ**\n\nหัวข้อ : {title}\n\nวันที่ : {thai_date}\n\nผู้ประกาศ : {author}\n\nเนื้อความ : {msg}\n————————————")

keep_alive.keep_alive()
bot.run(TOKEN)

## <!-- 🚀 Please follow on GitHub to stay tuned with us for more Exciting future Updates like this. | © 2022 — Made By Your's Jarvis #2431 with ♥ -->
