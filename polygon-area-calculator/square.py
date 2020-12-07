from rectangle import Rectangle

class Square(Rectangle):
    # Print class
    def __str__(self):
        return f"Square(side={self.width})"
    
    # Constructor
    def __init__(self, side_length):
        super().__init__(side_length, side_length)
    
    # Set side
    def set_side(self, new_side_length):
        super().set_width(new_side_length)
        super().set_height(new_side_length)

    def set_width(self, new_width):
       super().set_width(new_width)
    
    def set_height(self, new_height):
        super().set_height(new_height)
