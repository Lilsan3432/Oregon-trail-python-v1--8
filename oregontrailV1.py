import random
import time

# Welcome message
print('Welcome to the game Oregon Trail')

# Asking for player's name
while True:
    player_name = input('What is your name: ')
    if len(player_name) > 1:
        print(player_name + "? That's a good name.")
        break
    elif len(player_name) == 1:
        player_name_choice = input(player_name + "? Are you kidding me? Only one letter? (y/n): ")
        if player_name_choice.lower() == 'y':
            print("Ok...")
            break
    else:
        print("You did not type anything, try again.")

# Easter egg for special player names
if player_name.lower() == 'meriwether lewis':
    year_set = 1803
    mode_choice = 'impossible'
else:
    while True:
        year_set = input('Enter a year of your choice: ')
        if year_set.isdigit():
            year_set = int(year_set)
            break
        else:
            print('Error, please enter a valid year.')

    # Asking for game mode
    while True:
        mode_choice = input('Which mode do you want to play? (easy, normal, hard, impossible, customize): ').lower()
        if mode_choice in ['easy', 'normal', 'hard', 'impossible', 'customize']:
            break
        else:
            print('Bad input, try again.')

# Setting initial values based on game mode
if mode_choice == 'easy':
    food_num = 1000
    health_num = 10
elif mode_choice == 'normal':
    food_num = 500
    health_num = 5
elif mode_choice == 'hard':
    food_num = 300
    health_num = 4
elif mode_choice == 'impossible':
    food_num = 150
    health_num = 3
elif mode_choice == 'customize':
    while True:
        food_num = input('How much food do you want: ')
        if food_num.isdigit():
            food_num = int(food_num)
            break
        else:
            print('Error, please enter a valid number.')

    while True:
        health_num = input('How much health do you want: ')
        if health_num.isdigit():
            health_num = int(health_num)
            break
        else:
            print('Error, please enter a valid number.')

# Initial setup
player_move_distance = 0
month_num = 3
days_pass = 1
total_days = 0
MONTHS_WITH_31_DAYS = [1, 3, 5, 7, 8, 10, 12]
health_decrease_chance = 0.3  # 30% chance of health decrease each day

# Function to add days and handle random events
def add_days(min_days, max_days):
    global days_pass, month_num, total_days, food_num, health_num
    
    random_days = random.randint(min_days, max_days)
    days_pass += random_days
    total_days += random_days
    
    # Decrease food based on days passed
    food_num -= random_days * 5
    
    # Check for random events
    if random.random() < health_decrease_chance:
        health_num -= 1
        print('Unfortunately, you lose 1 health due to a random event.')

    # Handle end of month
    if days_pass > 30:
        days_pass -= 30
        month_num += 1
        if month_num > 12:
            month_num = 1

# Game introduction and instructions
print('--------------------------------------')
print('Game is ready!')
print('--------------------------------------')
print('Instructions:')
print('Your goal is to travel from NYC to Oregon (2000 miles) by Dec 31st.')
print('Each day costs you food and there are random events.')
print('You can travel, rest to recover health, hunt for food, check status, or quit/suicide.')
print('--------------------------------------')

# Main game loop
while player_move_distance < 2000 and food_num > 0 and health_num > 0 and month_num < 13:
    print(f'Date: {month_num}/{days_pass}/{year_set}')
    print(f'Food: {food_num} lbs | Health: {health_num} | Distance Traveled: {player_move_distance} miles')

    if food_num <= 50:
        print('Warning! Low on food.')
    if health_num <= 2:
        print('Warning! Low on health.')

    choice = input('Your choice (travel, rest, hunt, status, help, quit, suicide, easter egg): ').lower()

    if choice == 'travel':
        player_move_distance += random.randint(30, 60)
        add_days(3, 7)
    elif choice == 'rest':
        if health_num < 5:
            health_num += 1
        else:
            print('Your health is already full.')
        add_days(2, 5)
    elif choice == 'hunt':
        food_num += 100
        print('You gained 100 lbs of food.')
        add_days(2, 5)
    elif choice == 'status':
        print(f'Current Status: Food - {food_num} lbs, Health - {health_num}, Distance Traveled - {player_move_distance} miles')
    elif choice == 'help':
        print('Instructions:')
        print('[travel]: moves you randomly between 30-60 miles and takes 3-7 days (random).')
        print('[rest]: increases health by 1 level (up to 5 maximum) and takes 2-5 days (random).')
        print('[hunt]: adds 100 lbs of food and takes 2-5 days (random).')
        print('[status]: displays current game status.')
        print('[quit]: ends the game.')
        print('[suicide]: ends the game.')
    elif choice == 'quit':
        confirm = input('Are you sure you want to quit? (y/n): ')
        if confirm.lower() == 'y':
            break
    elif choice == 'suicide':
        confirm = input('Are you sure you want to end your journey? (y/n): ')
        if confirm.lower() == 'y':
            break
    elif choice == 'easter egg':
        print('Easter egg content here.')
    else:
        print('Invalid choice. Please try again.')

    print('--------------------------------------')

# Game result
if player_move_distance >= 2000:
    print('Congratulations! You have arrived in Oregon.')

if food_num <= 0:
    print('Game over! You ran out of food.')

if health_num <= 0:
    print('Game over! Your health reached zero.')

if month_num >= 13:
    print('Game over! You ran out of time.')

print(f'Traveled {player_move_distance} miles in {total_days} days.')
