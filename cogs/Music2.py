import discord
from discord import FFmpegPCMAudio
from discord.ext import commands
from youtube_dl import YoutubeDL


class Music2(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
        self.FFMPEG_OPTIONS = {
            'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

    def search_yt(self, item):
        with YoutubeDL(self.YDL_OPTIONS) as ydl:
            try:
                info = ydl.extract_info('ytsearch:%s' %
                                        item, download=False)['entries'][0]
            except Exception:
                return False
        return {'source': info['formats'][0]['url'], 'title': info['title']}

    @commands.command()
    async def play(self, ctx, *args):
        if ctx.author.voice:
            if ctx.voice_client:
                voice = discord.utils.get(
                    self.bot.voice_clients, guild=ctx.guild)
                print(ctx.guild)
                if voice.is_playing():
                    voice.stop()
                query = ''.join(args)
                song = self.search_yt(query)
                if type(song) == type(True):
                    await ctx.send('Не вдалося завантажити пісню. Неправильний формат, спробуйте інше ключове слово. Причиною може бути плейліст або формат прямої трансляції.')
                else:
                    source = FFmpegPCMAudio(
                        song['source'], **self.FFMPEG_OPTIONS)
                    player = voice.play(source)
            else:
                channel = ctx.message.author.voice.channel
                query = ''.join(args)
                song = self.search_yt(query)
                if type(song) == type(True):
                    await ctx.send('Не вдалося завантажити пісню. Неправильний формат, спробуйте інше ключове слово. Причиною може бути плейліст або формат прямої трансляції.')
                else:
                    voice = await channel.connect()
                    source = FFmpegPCMAudio(
                        song['source'], **self.FFMPEG_OPTIONS)
                    player = voice.play(source)
        else:
            await ctx.send('Ви не у голосовому каналі!')

    @commands.command()
    async def pause(self, ctx):
        if ctx.author.voice:
            if ctx.voice_client:
                voice = discord.utils.get(
                    self.bot.voice_clients, guild=ctx.guild)
                if voice.is_playing():
                    voice.pause()
                    await ctx.send('Трек призупинено.')
                else:
                    await ctx.send('В даний момент нічого не програється!')
            else:
                await ctx.send('Бот не в голосовому каналі')
        else:
            await ctx.send('Ви не в голосовому каналі!')

    @commands.command()
    async def resume(self, ctx):
        if ctx.author.voice:
            if ctx.voice_client:
                voice = discord.utils.get(
                    self.bot.voice_clients, guild=ctx.guild)
                if voice.is_paused():
                    voice.resume()
                    await ctx.send('Продовження програвання')
                else:
                    await ctx.send('В даний момент нічого не призупинено!')
            else:
                await ctx.send('Бот не в голосовому каналі')
        else:
            await ctx.send('Ви не в голосовому каналі!')

    @commands.command()
    async def stop(self, ctx):
        if ctx.author.voice:
            if ctx.voice_client:
                voice = discord.utils.get(
                    self.bot.voice_clients, guild=ctx.guild)
                await ctx.send('Програвання завершено')
                voice.stop()
                await voice.disconnect()
            else:
                await ctx.send('Бот не в голосовому каналі!')
        else:
            await ctx.send('Ви не в голосовому каналі!')


async def setup(bot):
    await bot.add_cog(Music2(bot))
