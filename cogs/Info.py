import discord
from discord.ext import commands


class Info(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot started!')

    @commands.command()
    async def info(self, ctx, arg = None):
        author = ctx.message.author
        if arg == None:
            await ctx.send(f'{author.mention} Привіт!, я музикальний бот.\n.info all - загальна інформація.\n.info commands - список команд.\n')
        elif arg == 'all':
            await ctx.send(f'''{author.mention}!
Моє основне завдання - програвання відео з YouTube у голосових каналах.
Також, я маю команди для сумних та веселих звуків, які будуть програватися у голосовому чаті.
Загалом це весь мій функціонал. Щоб дізнатись більше - .info commands
Нажаль, функцій черги в мене немає((
''')
        elif arg == 'commands':
            await ctx.send(f'''{author.mention}
.play (link) - програвання відео з ютуб.
.pause - пауза.
.resume - продовжити програвання.
.stop - завершити програвання.
.leave - покинути канал.
.joke - сміх за кадром.
.sad - сумний звук.
''')
        else:
            await ctx.send(f'{author.mention} такої команди немає.')

async def setup(bot):
    await bot.add_cog(Info(bot))
