import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import random

FUNNY = ['.\\Sounds\\mixkit-big-crowd-laughing-460.wav',
         '.\\Sounds\\mixkit-light-applause-with-laughter-audience-512.wav',
         '.\\Sounds\\mixkit-medium-size-group-applause-and-laugh-516.wav']
SAD = ['.\\Sounds\\30fbe621c218335.mp3',
       '.\\Sounds\\49dfdef97d65e09-1.mp3']


class Sounds(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def joke(self, ctx):
        if ctx.author.voice:
            if ctx.voice_client:
                voice = discord.utils.get(
                    self.bot.voice_clients, guild=ctx.guild)
                if voice.is_playing():
                    voice.stop()
                await ctx.send(':joy:')
                source = FFmpegPCMAudio(random.choice(FUNNY))
                player = ctx.voice_client.play(source)
            else:
                await ctx.send(':joy:')
                channel = ctx.message.author.voice.channel
                voice = await channel.connect()
                source = FFmpegPCMAudio(random.choice(FUNNY))
                player = voice.play(source)
        else:
            await ctx.send('Ты не в голосовому каналі. Потрібно бути в голосовом каналі, щоб активувати цю команду')

    @commands.command()
    async def sad(self, ctx):
        if ctx.author.voice:
            if ctx.voice_client:
                voice = discord.utils.get(
                    self.bot.voice_clients, guild=ctx.guild)
                if voice.is_playing():
                    voice.stop()
                await ctx.send(':weary:')
                source = FFmpegPCMAudio(random.choice(SAD))
                player = ctx.voice_client.play(source)
            else:
                await ctx.send(':weary:')
                channel = ctx.message.author.voice.channel
                voice = await channel.connect()
                source = FFmpegPCMAudio(random.choice(SAD))
                player = voice.play(source)
        else:
            await ctx.send('Ты не в голосовому каналі. Потрібно бути в голосовом каналі, щоб активувати цю команду')


async def setup(bot):
    await bot.add_cog(Sounds(bot))

