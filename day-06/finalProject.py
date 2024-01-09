"""
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while not at_goal():
    if front_is_clear():
        move()        
    elif right_is_clear():        
        turn_right()
        move()        
    else:
        turn_left()

    OTHER SOLUTION
    if right_is_clear():
        turn_right()
        move()        
    elif front_is_clear():        
        move()                        
    elif wall_in_front():
        turn_left()
    elif wall_on_right():
        turn_left()

    if right_is_clear():
        turn_right()
        move()      
    elif front_is_clear():        
        move()                        
    elif wall_in_front():
        turn_left()
    elif wall_on_right():
        turn_left()
    if right_is_clear() and front_is_clear():           
        move()
    if wall_on_right() and front_is_clear():
        move() 
    
    O QUE VAI DAR BOM EM QUALQUER SITU
while front_is_clear():
    move()
turn_left()
while not at_goal():
    if right_is_clear():
        turn_right()
        move()      
    elif front_is_clear():        
        move()                        
    else:
        turn_left()


################################################################
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
################################################################
"""