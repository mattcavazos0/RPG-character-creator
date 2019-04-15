class Wizard():
	def __init__(self):
		self.title = "Wizard"
		self.strength = 2
		self.wisdom = 8

class Warrior():
	def __init__(self):
		self.strength = 8
		self.wisdom = 2

class Player():
	def __init__(self, name):
		self.name = input("What is your name: ")
		self.char_class = ""

player = Player("")

while player.name == "":
	print("You need to enter a name")
	player = Player("")

print("Your name is " + player.name)

while player.char_class == "":
	print("You be a Wizard of a Warrior?")
	player.char_class = input("What are you? ")
		
if player.char_class.lower() == "wizard":
	player.char_class = Wizard()


print("You are a " +player.char_class.title)

print("Strength: " +str(player.char_class.strength))
print("Wisdom: " +str(player.char_class.wisdom))

