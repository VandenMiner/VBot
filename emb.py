
import discord
from discord.ext import commands


ds = commands.Bot(command_prefix='V')
@ds.event
async def on_ready():
    print('We have logged in as {0.user}'.format(ds))
@ds.command(pass_context = True)
async def Информация( ctx ):
	emb = discord.Embed(title = "Сервер", colour = discord.Color.blue(), description = "Информация")
	name_emba = "Выполнил: " + str(ctx.message.author)
	emb.set_author(name = name_emba)
	emb.set_footer(icon_url = ctx.author.avatar_url)
	emb.add_field( name = "***Айпи***", value = "***87.98.142.238:25786***")
	emb.add_field( name = ":Навмгация по коммандам:", value = """
***_Префикс - V_***
Информация - ну... вы поняли
Спамнуть <Пользователь> (Кидать только в #other-poeben, не карается мутом)
Вы можете замутить только этот канал, и вас не будут спамить
***Бот кликер***
cl - клик
sv - Сохранить
upgrade - Прокачать силу клика
price - узнать текущую цену на апгрейд
***Рп команды***
Пиздануть <Пользователь>
Выебать <Пользователь>
Поцеловать <Пользователь>
Укусить <Пользователь>
Пнуть <Пользователь>
Ударить <Пользователь>""")


	await ctx.send(embed = emb)
@ds.command(pass_context = True)
async def Спамнуть( ctx, arg ):
	await ctx.send(arg)
	await ctx.send(arg)
	await ctx.send(arg)
	await ctx.send(arg)
	await ctx.send(arg)
@ds.command(pass_context = True)
async def Пиздануть( ctx, arg ):
	emb = discord.Embed(title = "VandenSRV", colour = discord.Color.blue())
	author = "@" + str(ctx.message.author)
	emb.add_field(name = "Действие", value = author + " :fist: пизданул(a) " + str(arg))
	await ctx.send(embed = emb)
######################################
@ds.command(pass_context = True)
async def Выебать( ctx, arg ):
	emb = discord.Embed(title = "VandenSRV", colour = discord.Color.blue())
	author = "@" + str(ctx.message.author)
	emb.add_field(name = "Действие", value = author + " :pinching_hand: :point_left: Произвёл(а) жёсткую бдсм сессию " + str(arg))
	await ctx.send(embed = emb)
######################################
@ds.command(pass_context = True)
async def Ударить( ctx, arg ):
	emb = discord.Embed(title = "VandenSRV", colour = discord.Color.blue())
	author = "@" + str(ctx.message.author)
	emb.add_field(name = "Действие", value = author + " :right_facing_fist: Ударил(а) " + str(arg))
	await ctx.send(embed = emb)
######################################
@ds.command(pass_context = True)
async def Укусить( ctx, arg ):
	emb = discord.Embed(title = "VandenSRV", colour = discord.Color.blue())
	author = "@" + str(ctx.message.author)
	emb.add_field(name = "Действие", value = author + " :lips: Укусил(а) " + str(arg))
	await ctx.send(embed = emb)
######################################
@ds.command(pass_context = True)
async def Пнуть( ctx, arg ):
	emb = discord.Embed(title = "VandenSRV", colour = discord.Color.blue())
	author = "@" + str(ctx.message.author)
	emb.add_field(name = "Действие", value = author + " :foot: Пнул(а) " + str(arg))
	await ctx.send(embed = emb)
######################################
@ds.command(pass_context = True)
async def Поцеловать( ctx, arg ):
	emb = discord.Embed(title = "VandenSRV", colour = discord.Color.blue())
	author = "@" + str(ctx.message.author)
	emb.add_field(name = "Действие", value = author + " :kissing_heart: Поцеловал(а) " + str(arg))
	await ctx.send(embed = emb)


@ds.command(pass_context = True)
async def Предложка( ctx, arg ):
	load = open("Предложка.txt", "r")
	load0 = str(load.read())
	save_to_pr = load0 + " " + arg
	load1 = open("Предложка.txt", "w")
	load1.write(str(save_to_pr))

	await ctx.send("Хорошо")
#################################################
#												#
#					Кликер						#
#												#
#												#
#################################################
i_n = open("save_ds_bot.txt", "r")
i_ns = open("save_s_ds_bot.txt", "r")
i_np = open("save_price_ds_bot.txt", "r")
count = int(i_n.read())
streight = int(i_ns.read())
aprice = int(i_np.read())
#	#	#
def save():
	inn = open("save_ds_bot.txt", "w")
	inns = open("save_s_ds_bot.txt", "w")
	innp = open("save_price_ds_bot.txt", "w")
	global count
	global streight
	global aprice
	inn.write(str(count))
	inns.write(str(streight))
	innp.write(str(price))
def change():
	global count
	count = int(count) + int(streight) 
@ds.command(pass_context=True)
async def cl(ctx):
	global count
	change()
	await ctx.send('Общий баланс - ' + str(count) + ' монеток ')
@ds.command(pass_context=True)
async def sv(ctx):
	global count
	global streight
	global aprice
	await ctx.send('Сохранено ' + str(count) + ' монеток ')
	save()
@ds.command(pass_context=True)
async def price(ctx):
	global aprice
	await ctx.send(aprice)
@ds.command(pass_context=True)
async def upgrade( ctx ):
	global count, streight, aprice
	if count >= aprice:
		streight = streight + 1
		aprice += 300
		count = count - aprice
		await ctx.send('Успешно! Теперь вы кликайте по ' + str(streight) + ' монеток за раз')
	if count <= aprice:
		await ctx.send("Недостаточно монет")

token = os.environ.get('BOT_TOKEN')
ds.run(str(token))
