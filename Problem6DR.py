# David Ramirez
# 11/12/2024

#Write a function

import resources

def func_name(num):
    print(f"{resources.David.weapons}")
    if num == 1:

        for item in ["rope","coat","first aid kit"]:
            if item in resources.David.weapons:
                print(f"Hey, you don't have item {item}")
                return False
            
        print("You have everything you need, good luck!")
        return True 
    
    elif num == 2:
        for item in ["pan","groceries"]:
            if item in resources.David.weapons:
                print(f"Hey, you don't have item {item}")
                return False
            
            print("You have everything you need, good luck!")
        return True 

        
    elif num == 3:
        for item in ["pen","paper","idea"]:
            if item in resources.David.weapons:
                print(f"Hey, you don't have item {item}")
                return False
            
            print("You have everything you need, good luck!")
        return True 
func_name (3)