#imports multiple libraries; The private token located in the .env file and EC2 metadata
import discord 
import os 
import random 
from ec2_metadata import ec2_metadata 

print(ec2_metadata.region)
print(ec2_metadata.instance_id)

#Uses the discord library to create an instance of the bot class which can be called upon
client = discord.Bot() 

#uses the os library to retrieve the bot's private token enabling connection to Discord servers
token = str(os.getenv('TOKEN'))

#Creates an event that prints a message to indicate when the bot is logged in and ready.
@client.event 
async def on_ready(): 
	print("Logged in as a bot {0.user}".format(client))

""" Creates an event that listens for user messages and converts the user & channel name to a string format
for future use """
@client.event 
async def on_message(message): 
	username = str(message.author).split("#")[0] 
	channel = str(message.channel.name) 
	user_message = str(message.content) 

#Uses an f-string to format future messages which the bot will send in response to user messages.
	print(f'Message {user_message} by {username} on {channel}') 

#prevents bot from responding to itself
	if message.author == client.user: 
		return
	
#This if statement declares that it requires the channel to be set to random for it to activate. 
	if channel == "random": 

#If the user types "hello" or "hi" in the random server with bot active it will respond accordingly.
		if user_message.lower() == "hello" or user_message.lower() == "hi": 
			await message.channel.send(f'Hello {username} Your EC2 Data: {ec2_metadata.region}') 
			return
		
#If the user types "bye" or "goodbye" in the random server with bot active it will respond in-kind.
		elif user_message.lower() == "bye" or user_message.lower() == "goodbye": 
			await message.channel.send(f'Bye {username} - be well!  Your EC2 Data: {ec2_metadata.region}') 

#If the user types "tell me a joke" in the random server with bot active it will respond with a joke.
		elif user_message.lower() == "tell me a joke" or user_message.lower() == "got any jokes?": 

#creates a list of jokes and sets the choice to random
			jokes = [" Can someone please shed more light\
			 ...on how my lamp got stolen?", 
					"Why is she called llene?\
					---Because she stands on equal legs.", 
					"What do you call a gazelle in a lions territory?\
					 ---A Denzel."] 
			await message.channel.send(random.choice(jokes)) 

#This silly else if statement will trigger the user types "ayyyy" whilst the bot is active
		elif user_message.lower() == "ayyyy":
			await message.channel.send(f'AYYYYYYYYYYyyyyy {username} Your EC2 Data: {ec2_metadata.region}')

#Establishes the connection between the bot and the Discord API via token authentication.
client.run(token)



