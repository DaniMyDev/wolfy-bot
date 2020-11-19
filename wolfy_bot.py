import discord
from discord.ext import commands
import wolframalpha_controller
import matplotlib_controller
import os
from os import environ

bot = commands.Bot(command_prefix='!', description='wolframalpha bot')

# config
wolfy_channel_id = environ['WOLFY_CHANNEL_ID']
bot_token = environ['BOT_TOKEN']

# messages
error_message = 'oops!, looks that there was an error :(\ntry typing !wolfyhelp'

# Events
@bot.event
async def on_ready():
    game = discord.Game('Wolfram Alpha')
    await bot.change_presence(status=discord.Status.online, activity=game)
    wolfy_channel = bot.get_channel(wolfy_channel_id)
    await wolfy_channel.send('Hey! i am ready to rock! \n https://www.wolframalpha.com')


# Commands
@bot.command(aliases=['wolfy -h', 'wolfy -help'])
async def wolfyhelp(ctx):
    embed = discord.Embed(title='HELP')
    embed.add_field(name="Commands",
                    value='Hey, type !wolfy to use me')
    embed.add_field(name="wolfy(1)",
                    value='!wolfy 2+2 => 4')
    embed.add_field(name="wolfy(2)",
                    value='!wolfy sin(pi) => 0')
    embed.add_field(name="wolfyplot",
                    value='!wolfyplot [1,2,3,4] [2,4,9,16] => plot using coordenates')
    embed.add_field(name="wolfyplotf",
                    value='!wolfyplotf x**2 => plot using symbolic function')
    embed.set_author(name=bot.user.name)
    embed.set_footer(text="Developed with python",
                     icon_url='http://www.k-techlabo.org/www_python/python_icon.png')
    await ctx.send(embed=embed)


@bot.command(aliases=['wolfy -i', 'wolfy -info'])
async def wolfyinfo(ctx):
    embed = discord.Embed(title='INFORMATION')
    embed.add_field(name="Description",
                    value='Hey, I am wolfy, I am connected\n to WolframAlpha API!')
    embed.set_author(name=bot.user.name)
    embed.set_footer(text="Developed with python",
                     icon_url='http://www.k-techlabo.org/www_python/python_icon.png')
    await ctx.send(embed=embed)



@bot.command()
async def wolfy(ctx, *, query):
    try:
        response = wolframalpha_controller.fetchWolframAlpha(query)
        if response:
            return await ctx.send(response)
    except:
        return await ctx.send(error_message)

@bot.command(aliases=['wolfyp','plot'])
async def wolfyplot(ctx, x, y):
    try:
        response = matplotlib_controller.matplotlibPlot(x,y)
        if response:
            await ctx.send(file = discord.File("wolfy_plot.png"))
            os.remove('wolfy_plot.png')
        else:
            await ctx.send('There was a error with your input')
    except:
        await ctx.send(error_message)
        print('something went wrong')

@bot.command()
async def wolfyplotf(ctx, f):
    try:
        response = matplotlib_controller.sympyPlot(f)
        if response:
            await ctx.send(file = discord.File("wolfy_plotf.png"))
            os.remove('wolfy_plotf.png')
        else:
            await ctx.send('There was a error with your input')
    except:
        await ctx.send(error_message)
        print('something went wrong')


# run wolfy bot
bot.run(bot_token)
