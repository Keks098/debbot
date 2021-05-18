import discord
from discord.ext import commands
import datetime
import requests
from PIL import Image, ImageFont, ImageDraw
import io
import random
from discord import webhook, AsyncWebhookAdapter 
import aiohttp


PREFIX = '?'

client = commands.Bot( command_prefix = PREFIX )
client.remove_command( 'help' )


hello_words = [ 'деб', 'деб?' ]
awnswer_words = [ 'команды на сервере', 'какие команды есть на сервере', ]

goodbye_words = [ 'пока', 'пока деб', 'покеда', 'покеда деб', 'спасибо деб', 'спс деб' ]
bad_words = [ 'хуй', 'пизда', 'пиздец', 'бля', 'блять', 'нихуя', 'сука', 'та блять', 'ебать', 'эбать', 'ебать вас в рот', 'эбать вас в рот', 'ахуеть' ]

toxic_words = ['иди нах', 'иди нахуй', 'дибильный бот', 'дебильный бот', 'идите нахуй', 'иди в жопу', 'деб иди в жопу', 'деб иди нахуй', 'деб иди нах', 'деб ты дебил', 'деб ты дибил', 'сыш ты ахуел?', 'слыш ты ахуел', 'сыш ты ахуел', 'слыш ты ахуел?']
sas_words = [ 'как жизнь деб?' ]
dyrka_words = [ 'деб иди в дурку' ]

emoji_words = [ ':wave: ' ]
help_words = [ 'деб помоги' ]
otvet_words = ['сам ты токсик', 'деб блять заебал сам ты токсик', 'та блять сам ты токсик', 'деб заебал сам ты токсик', 'та сам ты токсик блять', 'иди ты нахуй токсик вонючий']

rassist_words = [ 'негр','еврей', 'эврей', 'жид', 'жидяра', 'жид сука', 'жидяра сука', 'черно мазый', ]
school_words = ['деб ты любишь школу?', 'деб как ты относишся к школе?']
politik_words = ['деб как ты относишся к политике?']
president_words = ['какой президент самый лучший?', 'какой президент лучший?', 'какой президент в мире лучший?', 'какой президент в мире самый лучший?', 'какой президент в стране лучший?']
deb_words = ['разве ты президент', 'деб разве ты президент?', 'какой президент нах', 'какой ты нах президент',]

awnswer2_words = ['деб ты кто?', 'деб кто ты такой', 'деб что ты такое', 'деб расскажи историю своего создания']
world_words = ['деб ты хочешь захватить мир?', 'деб ты хочешь истребить человечество?', 'деб ты хочешь уничтожить человечество?']

bestgame_words = ['деб какая компьютерная игра твоя любимая?', 'деб какая игра компьютерная самая лучшая?', 'деб назови лучшую по твоему мнению компьютерную игру в мире']
vera_words = ['деб как ты относишся к вере?', 'деб ты веришь в бога?', 'деб как ты относишся к вере?']
nelza_words = ['уууу еблан', 'нельзя так деб', 'нельзя так']

giza_words = ['устал', 'устал пиздец', 'хууух устал', 'как же я устал']
aboba_words = ['aboba']
karman_words = ['karman']

clear_words = ['Е', 'Вы шо ахуели?', 'Че так тихо', 'Вам клоун что ли персональный нужен?']
znak_words = ['.']

yes_words = ['да', 'походу да', 'походу да деб', 'походу да, им нужен персональный клоун', 'походу да деб, им нужен персональный клоун', 'да нам нужен персональный клоун', 'да нам нужен клоун']

ez_words = ['деб лох']
eblan_words = ['я еблан']
dancer_words = ['https://tenor.com/view/dancing-excited-dance-dance-move-smile-gif-16099354']

no_words = ['нет', 'нет не могу', 'нет немогу', 'не', 'не не могу', 'не немогу', 'неа', 'неа немогу', 'неа не могу']
aboba2_words = ['Тебе сломала шею scp 173 🍪', 'тебя scp 106 забрал в карманное измерение 🗿🗿🗿', 'Тебя сожрал scp 939 🗿🗿🗿', 'Ты посмотрел на лицо scp 096 👍']


@client.event


async def on_ready():
    print( 'BOT connected' )

    await client.change_presence( status = discord.Status.online, activity = discord.Game ( 'хуйню' ) )



@client.command( pass_context = True )
@commands.has_permissions( administrator = True )
async def clear( ctx, amount = 100 ):
    await ctx.channel.purge( limit = amount )

    await ctx.send(f'Я очистил {amount} сообщений!')

@client.command( pass_context = True )
@commands.has_permissions( administrator = True )

async def kick( ctx, member: discord.Member, *, reason = None ):
    await ctx.channel.purge( limit = 1 )

    await member.kick( reason = reason )
    await ctx.send( f'Выгнан пользователь { member.mantion }' )

@client.command( pass_context = True )
@commands.has_permissions( administrator = True )

async def ban( ctx, member: discord.Member, *, reason = None ):
    emb = discord.Embed( title = 'Бан', colour = discord.Color.red() )
    await ctx.channel.purge( limit = 1 )
    
    await member.ban( reason = reason )
    
    emb.set_author( name = member.name, icon_url = member.avatar_url )
    emb.add_field( name = 'Бан епта', value = 'Забанен пользователь : {}'.format( member.mention ) )
    emb.set_footer( text = 'Был забанен администратором {}'.format( ctx.author.name ), icon_url = ctx.author.avatar_url )
    
    await ctx.send( embed = emb )

@client.command( pass_context = True )
@commands.has_permissions( administrator = True )

async def help( ctx ):
    emb = discord.Embed( title = '❓ Команды на сервере:', colour = discord.Color.green() )
    await ctx.channel.purge( limit = 1 )
    
    emb.add_field( name = '{}clear 🧹'.format( PREFIX ), value = 'Очистка чата от ненужных сообщений (доступно только админам!)' )
    emb.add_field( name = '{}деб?'.format( PREFIX ), value = 'позвать меня если я пропал' )
    emb.add_field( name = '{}kick 🚫'.format( PREFIX ), value = 'Удаление пользователя с сервера (доступно только админам!)' )
    emb.add_field( name = '{}ban 🛑'.format( PREFIX ), value = 'бан пользователя на этом сервере (доступно только админам!)' )
    emb.add_field( name = '{}help ❓'.format( PREFIX ), value = 'Команды на этом сервере' )
    emb.add_field( name = '{}hello 👋'.format( PREFIX ), value = 'Если нехер делать поздоровайся с ботом' )
    emb.add_field( name = '{}yt 🎥'.format( PREFIX ), value = 'Ссылка на ютуб канал моего создателя' )
    emb.add_field( name = '{}send_z @имя пользователя'.format( PREFIX ), value = 'Если хотите пранконуть кого то пропишите эту команду с упоминанием имени пользователя и я отправлю ему любое сообщение(только без спама)' )
    emb.add_field( name = '{}aboba '.format( PREFIX ), value = 'Если хочешь испытать свою удачу, можешь сдохнуть, а можешь выиграть монету за которые на нашем сервере можно купить разные плюшки' )
    emb.add_field( name = '{}karman '.format( PREFIX ), value = 'Если тебя забрал scp 106 в карманное измерение, используй эту команду в канале карманное измерение если хочешь сбежать, или сдохнуть' )

    await ctx.send( embed = emb )



@client.command( pass_context = True )

async def hello( ctx, amount = 1 ):
    await ctx.channel.purge( limit = amount )

    author = ctx.message.author
    await ctx.send( f'Здарова епта { author.mention }' )

@client.event

async def on_message( message ):
    msg = message.content.lower()
    await client.process_commands( message )

    if msg in hello_words:
        await message.channel.send( 'Я тут' )

    if msg in awnswer_words:
        await message.channel.send( 'В команде ?help вся инфа' )

    if msg in goodbye_words:
        await message.channel.send( 'Покеда епта' ) 

    if msg in bad_words:
        await message.channel.send(random.choice(('не матерись', 'ты вообще без матов жить можешь?', 'та блять не матерись', 'не матерись блять, будь культурным человеком')))

    if msg in toxic_words:
        await message.channel.send(random.choice(('ты шо ахуел токсик ебучий', 'вот блядина а?', 'ты шо ахуел бычара?', 'сам такой')))

    if msg in sas_words:
        await message.channel.send( 'У меня все заебись' ) 

    if msg in dyrka_words:
        await message.channel.send( 'Тебе бы давно пора' )

    if msg in emoji_words:
        await message.channel.send( ' 👋 ' )

    if msg in help_words:
        await message.channel.send( 'Та блять не будет он смотреть' )

    if msg in rassist_words:
        await message.delete()
        await message.channel.send( 'Ты шо сука рассист?' )

    if msg in school_words:
        await message.channel.send('Сама школа нормас, но образование там ненужная х@йня которая по жизни человеку не нужна ваще')

    if msg in politik_words:
        await message.channel.send('одним словом: пи@здец')
    
    if msg in president_words:
        await message.channel.send('Я')

    if msg in deb_words:
        await message.channel.send('Ну я президент этого сервера ты шо не в курсе')

    if msg in awnswer2_words:
        await message.channel.send('Вообще я мем, но мой создатель дибил который из мема решил сделать искусственный интеллект')

    if msg in world_words:
        await message.channel.send('А нахуя мне это надо')

    if msg in bestgame_words:
        await message.channel.send('Змейка на нокии ебать, графика 11/10, сюжет 100/10, геймплей 10/10, какие тебе еще аргументы то нужны?')

    if msg in otvet_words:
        await message.channel.send('Та иди ты блять нахуй, у меня создатель дебильный токсик что я могу сделать то')

    if msg in vera_words:
        await message.channel.send('Я атеист')

    if msg in nelza_words:
        await message.channel.send('мне н@ср@ь))))))))))))))))')

    if msg in giza_words:
        await message.channel.send('Так отдохни, сидит базарит дичь б"ть')

    if msg in aboba_words:
        await message.channel.send(random.choice(('Тебе сломала шею scp 173 🍪', 'тебя scp 106 забрал в карманное измерение 🗿🗿🗿', 'Ты выиграл одну монету! 💰', 'Тебя сожрал scp 939 🗿🗿🗿', ' тебя украли одну монету! 🗿', 'Тебе отгрыз руки scp 939 🗿🗿🗿', 'Тебя "вылечил"" scp 049 🗿🗿', 'Ты посмотрел на лицо scp 096 👍')))
        
    if msg in karman_words:
        await message.channel.send(random.choice(('Ты сдох в карманном измерении 🗿🗿', 'Ты сдох в карманном измерении 🗿🗿', 'Ты сдох в карманном измерении 🗿🗿', 'Ты сдох в карманном измерении 🗿🗿', 'Ты сдох в карманном измерении 🗿🗿', 'Ты выбрался из карманного измерения... но потерял монету 🗿🗿🗿🗿🗿', 'Ты выбрался из карманного измерения!! 🥳🥳🥳', 'ты выбрался из карманного изсерения и нашел одну монету!! 🥳🥳🥳🥳')))

    if msg in znak_words:
        await message.channel.send(clear_words[3])

    if msg in yes_words:
        await message.channel.send('https://tenor.com/view/umm-confused-blinking-okay-white-guy-blinking-gif-7513882')

    if msg in ez_words:
        await message.channel.send('https://tenor.com/view/serega-pirat-dota2-streamer-%D1%81%D0%B5%D1%80%D0%B5%D0%B3%D0%B0%D0%BF%D0%B8%D1%80%D0%B0%D1%82-%D0%B0%D1%85%D1%83%D0%B5%D0%BB-gif-20360153')

    if msg in eblan_words:
        await message.channel.send('https://tenor.com/view/nice-awesome-good-amazing-like-gif-11035268')

    if msg in emoji_words:
        await message.channel.send(':wave:')

    if msg in dancer_words:
        await message.channel.send('https://tenor.com/view/quby-dance-cute-pentol-gif-18406660')

    if msg in no_words:
        await message.channel.send('https://tenor.com/view/nice-awesome-good-amazing-like-gif-11035268')
    
    if msg in aboba2_words:
        async def give_roles(member):
            role = discord.utils.get(member.guild.roles, id = 834698018354888704)

            await member.add_roles(role)
            await channel.send(embed = discord.Embed(description = f'{author.name} умер', color = 0xf1c40f))

            



   
@client.command( pass_context = True )

async def yt( ctx ):
    emb = discord.Embed( title = 'youtube канал моего создателя', description = 'Подпишись если не подписан', colour = discord.Color.red(), url = 'https://www.youtube.com/channel/UC-UTa0HflZn0pjoW-6s_o5A' )
    
    emb.set_author( name = client.user.name, icon_url = client.user.avatar_url )
    emb.set_footer( text = ctx.author.name, icon_url = ctx.author.avatar_url )
    emb.set_thumbnail( url = 'https://lh3.googleusercontent.com/-i6X61f5VLWg/YF-LlbSwh9I/AAAAAAAAAH8/x2e9Os6oCakb7qwOnh956sbo825K-RB0gCEwYBhgLKtQDAL1OcqwilJA_Bv16ErK5GeElbfFTOPHGD0oxMIzoZy0-lOO5khv0GhyiES8k3tsI026_nT0SYQA-ZT7PCh5NV5wPBo8uNMi-q4e43cOV2nl4VeCHtn2jiiOpO8JYS2tFMlkJKtHCvl2_8MVSMkKX_I73CxP4Edez_jeiDDnZe5YJvgOM2g_C9pWXOAt4KXjEcTLi7_GxAWFV2YJDf5Ld84M8dLr1cP-sp6NHjKfc-2TVwwjT7nzkpTB_1OdGFo2QX3zEkQ6KODp3g4HPV5a-qXK-i154V_Wlxr3vLTMMum88d4q7At1622wsXGNFJq2GAYoDDqXbqVyXLWDfbL_ahrOFhBsLN7RWxU4RlO3kINuAhN7v4155hkHbtOUeqWY3s9aALuPp7KhFCjWpZyjOkEey3nmqyuITWh8TkSAAIGNQYeZYW2-XYbxCxadgIN_Yna4TgMkmBoqKq6QTJjSvj-qyWmeA7fVVKJ7lkgJ5OkrqR9asfbfC2np-shWXkkWwmexMEZ_SiaOetQbmv3S5M4-lFAjD8PSmHuo9cZnNK_OWK4MwnDZTouWTRLqPfu0DC8bs_OTMH8bk4MjR9jpB-6sPgL4nX_ocfN4AmhYdL9ultyeIMPqP8YQG/w140-h140-p/2021-03-27.jpg' )
    #emb.set_image( url = 'https://lh3.googleusercontent.com/-i6X61f5VLWg/YF-LlbSwh9I/AAAAAAAAAH8/x2e9Os6oCakb7qwOnh956sbo825K-RB0gCEwYBhgLKtQDAL1OcqwilJA_Bv16ErK5GeElbfFTOPHGD0oxMIzoZy0-lOO5khv0GhyiES8k3tsI026_nT0SYQA-ZT7PCh5NV5wPBo8uNMi-q4e43cOV2nl4VeCHtn2jiiOpO8JYS2tFMlkJKtHCvl2_8MVSMkKX_I73CxP4Edez_jeiDDnZe5YJvgOM2g_C9pWXOAt4KXjEcTLi7_GxAWFV2YJDf5Ld84M8dLr1cP-sp6NHjKfc-2TVwwjT7nzkpTB_1OdGFo2QX3zEkQ6KODp3g4HPV5a-qXK-i154V_Wlxr3vLTMMum88d4q7At1622wsXGNFJq2GAYoDDqXbqVyXLWDfbL_ahrOFhBsLN7RWxU4RlO3kINuAhN7v4155hkHbtOUeqWY3s9aALuPp7KhFCjWpZyjOkEey3nmqyuITWh8TkSAAIGNQYeZYW2-XYbxCxadgIN_Yna4TgMkmBoqKq6QTJjSvj-qyWmeA7fVVKJ7lkgJ5OkrqR9asfbfC2np-shWXkkWwmexMEZ_SiaOetQbmv3S5M4-lFAjD8PSmHuo9cZnNK_OWK4MwnDZTouWTRLqPfu0DC8bs_OTMH8bk4MjR9jpB-6sPgL4nX_ocfN4AmhYdL9ultyeIMPqP8YQG/w140-h140-p/2021-03-27.jpg')
    
    now_date = datetime.datetime.now()
   
    emb.add_field( name = 'Time', value = 'Time : {}'.format( now_date ) )

    await ctx.send( embed = emb )

@client.command()
@commands.has_permissions( administrator = True )

async def user_mute( ctx, member: discord.Member ):
    await ctx.channel.purge( limit = 1 )

    mute_role = discord.utils.get( ctx.message.guild.roles, name = 'mute' )

    await member.add_roles( mute_role )
    await ctx.send( f'Выдал { member.mention }, мут, за анарушение прав! ')

@client.command()
async def send_a( ctx ):
    await ctx.author.send( 'Тебе привет от сникерса' )

@client.command()
async def send_z( ctx, member: discord.Member ):
    await member.send( f'ержан вставай, на роботу пора!!!!!' )

@client.command(aliases = ['Я', 'карта' ]) 
async def card_user(ctx):
    await ctx.channel.purge(limit = 1)
    
    img = Image.new('RGBA', (400, 200), '#000000')
    url = str(ctx.author.avatar_url)[:-10]

    response = requests.get(url, stream = True)
    response = Image.open(io.BytesIO(response.content))
    response = response.convert('RGBA')
    response = response.resize((100,100), Image.ANTIALIAS)

    img.paste(response, (15, 15, 115, 115))

    idraw = ImageDraw.Draw(img)
    name = ctx.author.name
    tag = ctx.author.discriminator

    headline = ImageFont.truetype('arial.ttf', size = 20)
    undertext = ImageFont.truetype('arial.ttf', size = 12)

    idraw.text((145, 15), f'{name}#{tag}', font = headline)
    idraw.text((145, 50), f'ID: {ctx.author.id}', font = undertext)

    img.save('user_card.png')

    await ctx.send(file = discord.File(fp = 'user_card.png'))




    
# Connect

token = open( 'token.txt', 'r' ).readline()

client.run( token )