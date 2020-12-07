def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    # M
    expected_balls_occurences = 0

    # List and dictionary to keepp the current random draw
    drawn_balls_dict = dict()
    drawn_balls_list = list()

    # Do N experiments
    for N in range(num_experiments):
        # Create da list of randomly drawn balls and turn into dictionary
        drawn_balls_list = hat.draw(num_balls_drawn)
        for current_drawn_ball in drawn_balls_list:
            # If ball exists, just add 1
            if current_drawn_ball in drawn_balls_dict:
                drawn_balls_dict[current_drawn_ball] += 1
            # If ball doesnt exist, create key and set value 1
            else:
                drawn_balls_dict[current_drawn_ball] = 1

        # Check if keys match and drawn balls values are >= expected balls values
        key_occurences = 0
        for key, value in drawn_balls_dict.items():
            if key in expected_balls and value >= expected_balls[key]:
                key_occurences += 1
        
        # If expected balls is a subset of drawn balls
        if key_occurences == len(expected_balls):
            expected_balls_occurences += 1
        
        # Empty dictionary
        drawn_balls_dict.clear()
   
    # Return probability 
    return expected_balls_occurences / num_experiments
