import random
from experiment import experiment

class Hat:

    # Constructor
    def __init__(self, **kwargs):
        self.contents = list()
        # Balls are received as an object
        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(key)

    # Draw random balls
    def draw(self, amount_to_draw:int):
        # If amount exceeds the available quantity, return all the balls
        if amount_to_draw > len(self.contents):
            return self.contents
        
        # Create list and fill with randomly drawn balls
        drawn_balls = list()
        for i in range(amount_to_draw):
            random_index = random.randint(0, len(self.contents) - 1)
            drawn_balls.append(self.contents[random_index])
            del self.contents[random_index]

        # Put balls back in hat
        for ball in drawn_balls:
            self.contents.append(ball)
        
        return drawn_balls
