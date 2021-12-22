#from guizero import App, ButtonGroup, Text, PushButton // If I decide to add in a GUI for better interactivity
#app = App()
#text = Text(app, text="Welcome to Black Jack!")
#text2 = Text(app, text="Rules: \n\n1) If a player goes over 21 points they lose\n2) The closest to 21 points but NOT 21 points wins\n3) Players can ‘hit’ (draw a card)\n4) 1-5 players allowed")
#text3 = Text(app, text="How many players are there?")
#app.display()

#def players():
  #if player_choice.value == "1":
    #display_joke.value = "There is 1 player total!"
  #if joke_choice.value == "2":
    #display_joke.value = "What's pink and fluffy? Pink Fluff. What's Blue and Fluffy? - Pink Fluff holding it's breath."
  #if joke_choice.value == "Chicken":
    #display_joke.value = ("What does a mummy chicken say to her smart chick? - You are egg-cellent!")
  #if joke_choice.value == "Frog":
    #display_joke.value = "What do you call a 100-year-old toad? - An old croak."

#app = App(title="Blackjack")
#message = Text(app, text="Choose a joke from the list below:")
#joke_choice = ButtonGroup(app, options=["1", "2", "3", "4", "5"])
#joke_button = PushButton(app, command=jokes, text=("Start"))
#display_joke = Text(app, "Waiting for a joke...")

#app.display()

player1Total = 0
player2Total = 0
player3Total = 0
player4Total = 0
player5Total = 0

print("Welcome to Black Jack!")
print("")
print("Rules: \n\n1) If a player goes over 21 points they lose\n2) The closest to 21 points but NOT 21 points wins\n3) Players can ‘hit’ (draw a card)\n4) 1-5 players allowed")
print("")
print("How many players are there?")
totalPlayers = int(input())

def firstHit ():
    print ("Hey there")

def scoreBoard ():
  file = open("scores.csv", "r")