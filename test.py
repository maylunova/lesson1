my_dict = {'John' : {'city': 'Moscow', 'temp': '0', 'wind': 'north'}, 'Mary' : {'city': 'Boston', 'temp': '15', 'wind': 'south'}, 'Matt' : {'city': 'Paris', 'temp': '10', 'wind': 'west'}}
enter = input("Enter your name: ")
for key in my_dict:
    if key == enter:
    	print(my_dict[key])

