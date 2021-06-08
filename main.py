#Colored text output initilization
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''

#Create Mapped Dictionary with conjoined rooms and room items
rooms = {'Candy_Kingdom':
             {'item': 'Princess Bubblegum\'s_Enchanted_Sweater', 'North': None, 'East': None, 'South': None,
              'West': 'Lumpy_Space'},
         'Ice_Kingdom':
             {'item': 'Gunter_wearing_the_Ice_King\'s_Crown', 'North': 'Tree_House', 'East': 'Tree_Trunk\'s_House',
              'South': None, 'West': None},
         'Lumpy_Space':
             {'item': 'Lumps_Antidote', 'North': None, 'East': 'Candy_Kingdom', 'South': 'Tree_House', 'West': None},
         'Mystery_Mountains':
             {'item': 'The_Enchiridion', 'North': 'The Nightosphere', 'East': None, 'South': None, 'West': 'Tree_House'},
         'Stock_Woods':
             {'item': 'Grass_Sword', 'North': None, 'East': 'Tree_House', 'South': None, 'West': None},
         #The Nightosphere may need extra parameters because this is where we fight the boss and finish the game
         'The_Nightosphere':
             {'item': 'The_Lich', 'North': None, 'East': None, 'South': None, 'West': 'Tree_House'},
         'Tree_House':
             {'item': None, 'North': 'Lumpy_Space', 'East': 'Mystery_Mountains', 'South': 'Ice_Kingdom',
              'West': 'Stock_Woods'},
         'Tree_Trunk\'s_House':
             {'item': 'Crystal_Gem_Apple', 'North': None, 'East': None, 'South': None, 'West': 'Ice_Kingdom'}

         }


#Prints a prompt that shows the players: current_location, room_item, inventory, and prompt for next move
def prompt(item, inventory):
    item = current_room_item
    print('-----------------------------------------')
    print('You are currently in the', f"{bcolors.OKGREEN}{current_location}{bcolors.ENDC}")
    if item != None:
        print('You have found', f"{bcolors.HEADER}{current_room_item}{bcolors.ENDC}", 'in the room')
    else:
        print('There is nothing here for us.')
    print('Inventory:', inventory)
    action = input(f"{bcolors.OKBLUE}Your move: {bcolors.ENDC}")
    return action

#Splits a response into a list e.g 'go Place' ->  parse[0] == 'go', parse[1] == 'Place'
def parse_response(test):
    parse = test.split()
    if len(parse) >= 3:
        parse[1] = ' '.join(parse[1:])
        del parse[2:]
    return(parse)


#Updates current_location to room.current_location[DIRECTION] and cooresponding room_items
def go(direction):
    global current_location
    global current_room_item
    if rooms[current_location][direction] == None:
        print(f"{bcolors.FAIL}There\'s nothing beyond this point. Turn around and pick a different direction.{bcolors.ENDC}")
    else:
        print('You entered the {}.'.format(rooms[current_location][direction]))
        current_location = rooms[current_location][direction]
        current_room_item = rooms[current_location]['item']
        return current_location

#Adds item to current inventory, replaces room's item in map dic. with None
def grab(item):
    global rooms
    global current_room_item
    if item == current_room_item:
        current_inventory.append(item)
        print('You have grabbed the {}!'.format(item))
        rooms[current_location]['item'] = None
        current_room_item = rooms[current_location]['item']

current_inventory = []
current_location = 'Tree_House'
current_room_item = rooms[current_location]['item']
player_alive = True


while player_alive == True:

    response = prompt(current_room_item, current_inventory)


    response = parse_response(str(response))

    if response[0] == 'go':
        go(response[1])
    elif response[0] == 'grab':
        grab(response[1])


    continue



#Define a pickup() function that allows player to pick up an item in their current_room


#Create an introduction that gives a brief description of the game and directions for /prompt


