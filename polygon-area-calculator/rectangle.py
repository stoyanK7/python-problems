class Rectangle:

    # Print class
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    # Constructor
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Set width
    def set_width(self, new_width):
        self.width = new_width
    
    # Set height
    def set_height(self, new_height):
        self.height = new_height

    # Get area
    def get_area(self):
        return self.width * self.height
    
    # Get perimeter
    def get_perimeter(self):
        return (2 * (self.width + self.height))

    # Get diagonal
    def get_diagonal(self):
        return ((self.width ** 2) + (self.height ** 2)) ** .5 

    # Get picture
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        
        asterisk = "*"
        output = ""
        for row in range(self.height):
           output += (f"{asterisk * self.width}\n")
        
        return output

    # Get amount inside
    def get_amount_inside(self, shape):
        width_capability = self.width // shape.width
        height_capability = self.height // shape.height
        return width_capability * height_capability
