
map = {"bank": 3000,       #dictionary made to include values to the key
             "jewelry": 2750,
             "museum": 3000,
             "donut shop": 750,
             "gas station": 750,
             "cargo plane": 4000}

map2 = {"casino": 4000,     # second dictionary
        "bank2": 3000,
        "rig": 4000,
        "lab": 4500}

def rob(map):        #function that lets user choose what to rob and totals the amount
    moneyBag = []    #stores the values of the keys when user enters input
    total = 0         #adds the total amount of values from what user chose

    print("--------MAP---------")
    for key, value in map.items():             #prints the value in key, value form 
        print(f"{key}: ${value:.2f}")
    print("--------------------")

    while True:                        
        location = input("Select an item(x to quit): ").lower()   #lets the user pick the locations from the dictionary as many times as they want
        if location == "x":     #when user input is x, the loop will break 
            break
        elif map.get(location) is not None:     #if user has location input, it will add the value to moneyBag
            moneyBag.append(location)
    print(moneyBag)

    print("-----YOUR ROBBERIES-----")
    for location in moneyBag:           #prints the keys that the user chose 
        total += map.get(location)      #adds the total from all the key values 
        print(location, end=" ")   

    print()
    print(f"Total amount of money robbed: ${total:.2f}")     #prints the total amount of money robbed


rob(map)   #calls the function
rob(map2)











