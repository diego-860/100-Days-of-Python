while not at_goal():
    if right_is_clear():
        turn_right()
        move()
        turn_right()
        move()
    elif wall_in_front():
        turn_left()
    else:
        move()
