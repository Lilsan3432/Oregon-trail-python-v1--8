import random
import sys
import time

# ASCII art for Oregon Trail
ox_wagon_art = '''
                                                                         ,----,                                     
    ,----..                                                           ,/   .`|                                     
   /   /   \\                                                        ,`   .'  :                             ,--,    
  /   .     :                                                     ;    ;     /                    ,--,   ,--.'|    
 .   /   ;.  \\  __  ,-.                      ,---.        ,---, .'___,/    ,' __  ,-.           ,--.'|   |  | :    
.   ;   /  ` ;,' ,'/ /|          ,----._,.  '   ,'\   ,-+-. /  ||    :     |,' ,'/ /|           |  |,    :  : '    
;   |  ; \\ ; |'  | |' | ,---.   /   /  ' / /   /   | ,--.'|'   |;    |.';  ;'  | |' | ,--.--.   `--'_    |  ' |    
|   :  | ; | '|  |   ,'/     \\ |   :     |.   ; ,. :|   |  ,"' |`----'  |  ||  |   ,'/       \\  ,' ,'|   '  | |    
.   |  ' ' ' :'  :  / /    /  ||   | .\\  .'   | |: :|   | /  | |    '   :  ;'  :  / .--.  .-. | '  | |   |  | :    
'   ;  \\; /  ||  | ' .    ' / |.   ; ';  |'   | .; :|   | |  | |    |   |  '|  | '   \\__\\/\\. . | |  | :   '  : |__  
 \\   \\  ',  / ;  : | '   ;   /|'   .   . ||   :    ||   | |  |/     '   :  |;  : |   ," .--.; | '  : |__ |  | '.'| 
  ;   :    /  |  , ; '   |  / | `---`-'| | \\   \\  / |   | |--'      ;   |.' |  , ;  /  /  ,.  | |  | '.'|;  :    ; 
   \\   \\ .'    ---'  |   :    | .'__/\_: |  `----'  |   |/          '---'    ---'  ;  :   .'   \\;  :    ;|  ,   /  
    `---`             \\   \\  /  |   :    :          '---'                          |  ,     .-./|  ,   /  ---`-'   
                                  `--`-'                                                                           
'''

# Function to print ASCII art with a slight delay for effect
def print_with_delay(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

# Game initialization
def start_game():
    print_with_delay(ox_wagon_art)
    print_with_delay('''
-------------------------------------------------
Welcome to the Oregon Trail Adventure Game!
-------------------------------------------------
You are about to embark on a journey from the East
Coast to Oregon. Your goal is to travel 2000 miles
by the end of the year, while managing your food
supplies, health, and encountering various challenges
along the way.
-------------------------------------------------
''')

    # Difficulty selection menu
    print('''
Select Difficulty:
1. Easy   (More food, slower health decrease)
2. Normal (Standard game settings)
3. Hard   (Less food, faster health decrease)
''')

    difficulty_choice = input('Enter the number of your chosen difficulty: ')
    if difficulty_choice == '1':
        food_num = 1500  # More starting food
        health_decrease_chance = 0.2  # Lower health decrease chance
    elif difficulty_choice == '2':
        food_num = 1000  # Standard starting food
        health_decrease_chance = 0.3  # Standard health decrease chance
    elif difficulty_choice == '3':
        food_num = 800  # Less starting food
        health_decrease_chance = 0.4  # Higher health decrease chance
    else:
        print("Invalid choice, setting to Normal difficulty...")
        food_num = 1000
        health_decrease_chance = 0.3

    print('\nStarting game...\n')
    return food_num, health_decrease_chance

# Main game loop
def main_game_loop(food_num, health_decrease_chance):
    # Asking for player's name
    while True:
        player_name = input('What is your name: ')
        if len(player_name) > 1:
            print(f"{player_name}? That's a good name.")
            break
        elif len(player_name) == 1:
            player_name_choice = input(f"{player_name}? Are you kidding me? Only one letter? (y/n): ")
            if player_name_choice.lower() == 'y':
                print("Okay...")
                break
        else:
            print("You did not type anything, try again.")

    # Initial setup
    player_move_distance = 0
    month_num = 3
    days_pass = 1
    total_days = 0
    health_num = 10  # default starting values
    MONTHS_WITH_31_DAYS = [1, 3, 5, 7, 8, 10, 12]

    # Function to add days and handle random events
    def add_days(min_days, max_days):
        nonlocal days_pass, month_num, total_days, food_num, health_num

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

    # Game instructions
    print_with_delay('''
Instructions:
Your goal is to travel from the East to Oregon (2000 miles) by Dec 31st.
Each day costs you food and there are random events that may impact your health.
You can travel, rest to recover health, hunt for food, check status, or quit.
-------------------------------------------------
''')

    # Main game loop
    while player_move_distance < 2000 and food_num > 0 and health_num > 0 and month_num < 13:
        print(f'Date: {month_num}/{days_pass}')
        print(f'Food: {food_num} lbs | Health: {health_num} | Distance Traveled: {player_move_distance} miles')

        if food_num <= 50:
            print('Warning! Low on food.')
        if health_num <= 2:
            print('Warning! Low on health.')

        choice = input('Your choice (travel, rest, hunt, status, help, quit): ').lower()

        if choice == 'travel':
            miles_traveled = random.randint(30, 60)
            player_move_distance += miles_traveled
            add_days(3, 7)
            print_with_delay('Traveling...\n')
            time.sleep(1)
            print_with_delay(ox_wagon_art)
            print(f'You traveled {miles_traveled} miles.')
        elif choice == 'rest':
            if health_num < 10:
                health_num += 1
                print_with_delay('Resting...\n')
                time.sleep(1)
                print_with_delay(ox_wagon_art)
                print('You rested and recovered 1 health.')
            else:
                print('Your health is already full.')
            add_days(2, 5)
        elif choice == 'hunt':
            food_gained = random.randint(50, 200)
            food_num += food_gained
            print_with_delay('Hunting for food...\n')
            time.sleep(1)
            print_with_delay(ox_wagon_art)
            print(f'You went hunting and gained {food_gained} lbs of food.')
            add_days(2, 5)
        elif choice == 'status':
            print_with_delay('Checking status...\n')
            time.sleep(1)
            print_with_delay(ox_wagon_art)
            print(f'Current Status: Food - {food_num} lbs, Health - {health_num}, Distance Traveled - {player_move_distance} miles')
        elif choice == 'help':
            print('''
        Instructions:
        [travel]: moves you randomly between 30-60 miles and takes 3-7 days (random).
        [rest]: increases health by 1 level (up to 10 maximum) and takes 2-5 days (random).
        [hunt]: adds between 50-200 lbs of food and takes 2-5 days (random).
        [status]: displays current game status.
        [quit]: ends the game.
            ''')
        elif choice == 'quit':
            confirm = input('Are you sure you want to quit? (y/n): ')
            if confirm.lower() == 'y':
                break
        else:
            print('Invalid choice. Please try again.')

        print('-------------------------------------------------')

    # Game result
    print('-------------------------------------------------')
    if player_move_distance >= 2000:
        print_with_delay(f'Congratulations, {player_name}! You have successfully arrived in Oregon and started a new life!')
    elif food_num <= 0:
        print_with_delay('Game over! You ran out of food and did not survive the journey.')
    elif health_num <= 0:
        print_with_delay('Game over! Your health reached zero and you did not survive the journey.')
    elif month_num >= 13:
        print_with_delay('Game over! You ran out of time and did not make it to Oregon.')

    print(f'Traveled {player_move_distance} miles in {total_days} days.')
    print('Thank you for playing Oregon Trail!')
    print('-------------------------------------------------')

# Main program entry point
if __name__ == "__main__":
    food_num, health_decrease_chance = start_game()
    main_game_loop(food_num, health_decrease_chance)
