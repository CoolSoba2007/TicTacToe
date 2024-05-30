
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.voice_states = True
bot = commands.Bot(
    command_prefix='?',
    intents = intents
)
symbols = ["X", "O"]
symbol = " "
@bot.event
async def on_message(message: discord.Message) -> None:
    if message.author == bot.user:  # Make sure the bot doesn't answer to itself
        return
    if message.content == '?tictactoe user':
        board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        players = []
        await message.channel.send("it's tictactoe game\n"
               "two players are playing with X's or O's\n"
               "Who get a row of a same symbol wins.")
        await message.channel.send("If you're playing type 'me'. If everyone's ready type 'play'")

        while True:

            response = await bot.wait_for('message')
            if response.author == bot.user:  # Make sure the bot doesn't answer to itself
               continue
            if response.content.lower() == 'stop':  # When the player types Stop the game stops.
                await message.channel.send('Thanks for playing.')
                return
            elif response.content.lower() == 'play':
                if len(players) != 2 : 
                     await message.channel.send("There must be 2 players dude.")
                     continue
                break
            elif response.content.lower() == 'me':
                is_same = False
                author = response.author
            # The same player can't 'register' twice.
                for player in players:
                    if player == author:
                        is_same = True
                        await message.channel.send("You're playing dude.")
                if not is_same:
                    players.append(author)
                    
        while True:
            
            
            for player in players:
                if player == players[0]:
                    symbol = symbols[0]
                elif player == players[1]:
                    symbol = symbols[1]
                await message.channel.send(f"It is {player}'s turn.")
                msg = await bot.wait_for('message')
                if msg.author == bot.user:  # Make sure the bot doesn't answer to itself
                    continue
                if msg.content.lower() == 'stop':  # When the player types Stop the game stops.
                    await message.channel.send('Thanks for playing.')
                    return
                if msg.author != player:  # You can't play when it's not your turn.
                    await message.channel.send("Not your turn!")
                    continue
                a = response.content
                await message.channel.send(type(a))
                if a == "10":
                    restart()
                elif a  in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    await message.channel.send("Invalid input. Please enter a number between 1 and 9.")
                    continue
                else:
                    if check_position(a):
                       global symbol 
                       board[int(a)] = symbol
                       
                    else:
                       
                       while not check_position(a):
                               await message.channel.send("It is already played.")
                               await message.channel.send("Make your play bro")
                               a = response.content
                               board[a] = symbol
                           
                    if Game == Win:
                       break
# Create a bot instance

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
# Win Flag
Win = 1
Draw = -1
Running = 0


Game = Running
Mark = 'X'
Mark0 = 'O'


  #Function to check the position , if its played or not
def check_position(x):
    return board[x] == ' '

  #checking all variaties of wins and draws
def check_win():
    global Game

    if board[1] == board[2] and board[2] == board[3] and board[1] != ' ':
       Game = Win
       if board[1] == Mark:
          ans = "O's is a loser"
       else:
          ans = "X's is a loser"
    elif board[4] == board[5] and board[5] == board[6] and board[4] != ' ':
       Game = Win
       if board[4] == Mark:
          ans = "O's is a loser"
       else:
          ans = "X's is a loser"
    elif board[7] == board[8] and board[8] == board[9] and board[7] != ' ':
         Game = Win
         if board[7] == Mark:
            ans = "O's is a loser"
         else:
            ans = "X's is a loser"
    elif board[1] == board[4] and board[4] == board[7] and board[1] != ' ':
         Game = Win
         if board[1] == Mark:
            ans = "O's is a loser"
         else:
            ans = "X's is a loser"
    elif board[2] == board[5] and board[5] == board[8] and board[2] != ' ':
         Game = Win
         if board[2] == Mark:
            ans = "O's is a loser"
         else:
            ans = "X's is a loser"
    elif board[3] == board[6] and board[6] == board[9] and board[3] != ' ':
         Game = Win
         if board[3] == Mark:
            ans = "O's is a loser"
         else:
            ans = "X's is a loser"
    elif (board[1] == board[5] and board[5] == board[9] and board[5] != ' ') or \
         (board[3] == board[5] and board[5] == board[7] and board[5] != ' '):
         Game = Win
         if board[5] == Mark:
            ans = "O's is a loser"
         else:
            ans = "X's is a loser"
    elif board[1] != ' ' and board[2] != ' ' and board[3] != ' ' and \
            board[4] != ' ' and board[5] != ' ' and board[6] != ' ' and \
            board[7] != ' ' and board[8] != ' ' and board[9] != ' ':
        Game = Draw
        ans = "Draw"
    else:
        Game = Running
        ans = "Game is still running"
    return ans

  #in case something went wrong there is a function to restart the game
def restart():
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

  #The game loop, while it is running the players can continue
with open('token.txt', 'r') as f:
    token = f.read()
bot.run(token)


