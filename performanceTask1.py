
map = {"bank": 3000,      
             "jewelry": 2750,
             "museum": 3000,
             "donut shop": 750,
             "gas station": 750,
             "cargo plane": 4000}

map2 = {"casino": 4000,     
        "bank2": 3000,
        "rig": 4000,
        "lab": 4500}

def rob(map):        
    moneyBag = []    
    total = 0         

    print("--------MAP---------")
    for key, value in map.items():              
        print(f"{key}: ${value:.2f}")
    print("--------------------")

    while True:                        
        location = input("Select an item(x to quit): ").lower()  
        if location == "x":     
            break
        elif map.get(location) is not None:     
            moneyBag.append(location)
    print(moneyBag)

    print("-----YOUR ROBBERIES-----")
    for location in moneyBag:            
        total += map.get(location)       
        print(location, end=" ")   

    print()
    print(f"Total amount of money robbed: ${total:.2f}")     


rob(map)   
rob(map2)
