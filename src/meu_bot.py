import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        if message.content == '§cu':
            await message.channel.send(f'Olá {message.author.name}! Aqui esta o cu')
        elif message.content == '§cantada':
            await message.author.send(f'Olá {message.author.name}! Barril!')
            await message.author.send(f'vem que vou te comer la em casa')

    async def on_member_join(self,member):
        guild = member.guild
        if guild.system_channel is not None:
            mensagem = (f'{member.mention} acabou de entrar no {guild.name}')
            await guild.system_channel.send(mensagem)
    
intents = discord.Intents.default()
intents.typing = True
intents.presences = True
intents.members = True
intents.message_content = True 

client = MyClient(intents=intents)
client.run('MTA5OTA0NjcyNDYxNTU1NzE1MA.GUNnSl.Y6BtseeSZk6i1eIDI1wfZge2bHOk1T2uURcWNo')