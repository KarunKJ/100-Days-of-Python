MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

#print(MENU["cappuccino"]["cost"])
logo = """  .oooooo.              .o88o.  .o88o.                                                                oooo         o8o                        
 d8P'  `Y8b             888 `"  888 `"                                                                `888         `"'                        
888           .ooooo.  o888oo  o888oo   .ooooo.   .ooooo.       ooo. .oo.  .oo.    .oooo.    .ooooo.   888 .oo.   oooo  ooo. .oo.    .ooooo.  
888          d88' `88b  888     888    d88' `88b d88' `88b      `888P"Y88bP"Y88b  `P  )88b  d88' `"Y8  888P"Y88b  `888  `888P"Y88b  d88' `88b 
888          888   888  888     888    888ooo888 888ooo888       888   888   888   .oP"888  888        888   888   888   888   888  888ooo888 
`88b    ooo  888   888  888     888    888    .o 888    .o       888   888   888  d8(  888  888   .o8  888   888   888   888   888  888    .o 
 `Y8bood8P'  `Y8bod8P' o888o   o888o   `Y8bod8P' `Y8bod8P'      o888o o888o o888o `Y888""8o `Y8bod8P' o888o o888o o888o o888o o888o `Y8bod8P' 
                                                                                                                                              
                                                                                                                                              
                                                                                                                   """