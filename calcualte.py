# Function to calculate area and perimeter of a rectangle
def calculate_rectangle_info(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

# Function to calculate area and perimeter of a triangle
def calculate_triangle_info(base, height):
    area = 0.5 * base * height
    # Assuming this is a right-angled triangle
    long_side = (base**2 + height**2)**0.5
    perimeter = base + height + long_side
    return area, perimeter


# for circle
 cirlce_area = 3.14159 * raidus ** 2
  circle_perimeter = 2 * 3.14159 * raidus

# Function to calcualte the area and perimeter of a square
def calculate_square_info(length):
  square_area = length * length
  square_perimeter = length * 4
  return square_area, square_perimeter

def calculate_radius_info(radius):
    circle_area = 3.14159 * radius ** 2
    circle_perimeter = 2 * 3.14159 * radius
    return circle_area, circle_perimeter