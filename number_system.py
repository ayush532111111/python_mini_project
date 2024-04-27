class Position:
    def _init_(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    
    def move_horizontal(self, distance):
        self.x += distance
    
    def move_vertical(self, distance):
        self.y += distance
    
    def move_forward(self, distance):
        self.z += distance
    
    def move_backward(self, distance):
        self.z -= distance

# Example usage:
if _name_ == "_main_":
    # Starting position
    current_position = Position()

    # Moving right by 3 units
    current_position.move_horizontal(3)
    print("Current position after moving right:", current_position.x)

    # Moving upward by 2 units
    current_position.move_vertical(2)
    print("Current position after moving up:", current_position.y)

    # Moving forward by 5 units
    current_position.move_forward(5)
    print("Current position after moving forward:", current_position.z)

    # Moving left by 2 units
    current_position.move_horizontal(-2)
    print("Current position after moving left:", current_position.x)

    # Moving downward by 4 units
    current_position.move_vertical(-4)
    print("Current position after moving down:", current_position.y)

    # Moving backward by 1 unit
    current_position.move_backward(1)
    print("Current position after moving backward:", current_position.z)