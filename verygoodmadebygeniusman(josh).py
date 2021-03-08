userActive = {}

@client.event
async def on_message(message):

    messages = []
    isActive = 0

    if str(message.author) not in userActive:
        userActive.update({str(message.author): 0})
        
    if str(message.author) in userActive:
        if message.content == "!activate":

            userActive.update({str(message.author): 1})
        elif userActive[str(message.author)] == 1:
            await message.channel.send('Here')
            userActive[str(message.author)] = 2
        elif userActive[str(message.author)] == 2:
            await message.channel.send('Here2')
            userActive[str(message.author)] = 3
        else:
            print("Nothing")

    print(userActive)