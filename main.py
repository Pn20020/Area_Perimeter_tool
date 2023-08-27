# all functions
# functions go here 
def yes_no(question):
  valid = False
  while not valid:
    response = input(question).lower().strip() 
    # input
    if response == "yes" or response == "y":
      response = "yes"
      print("Wellcome to the area/perimeter tool we will ask you to choose from the list of shapes to choose from and the measurements in mm and we will calculate the area and perimeter for you")
      return response
  
    elif response == "no" or response == "n":
      response = "no"
      print("Program continues")
      return response

    else:
      print("Please enter yes or no")

#get the shape
def Shapes(question, num_letters, valid_responses):

    error = "Please choose from our shapes list we have {} {} {} and {}".format(valid_responses[0],
                                                                                valid_responses[1],
                                                                                valid_responses[2],
                                                                                valid_responses[3])

    if num_letters == 1:
        short_version = 1
    else:
        short_version = 2

    while True:
        response = input(question).lower()

        for item in valid_responses:
            if response == item[:short_version] or response == item:
                return item

        print(error)

# get the angle of the triangle
def angle(question, num_letters, valid_responses):

    error = "Please choose {} {} or {}".format(valid_responses[0],
                                              valid_responses[1],
                                              valid_responses[2])
  
    if num_letters == 2:
        short_version = 2
    else:
        short_version = 3

    while True:
        response = input(question).lower()

        for item in valid_responses:
            if response == item[:short_version] or response == item:
                return item

        print(error)

def shape_radius(question):
# functions go here 
# checks users enter an float to a given question 
    while True:
      try:
        response = float(input(question))
        if response <= 2:
          print("Please choose a number over 2mm")
        else:
          return response 
      except ValueError:
        print("Please enter an a valid raidus.")

        
# get the lenght of the shape
def shape_lenght(length):
# functions go here 

# checks users enter an integer to a given question 

  
  while True:

    try:
        response =  int(input(length))
        return response 

    except ValueError:
        print("Please enter an integer.")


#get the width of the shape
def shape_width(width):
# functions go here 

# checks users enter an integer to a given question 

  
  while True:

    try:
        response =  int(input(width))
        return response 

    except ValueError:
        print("Please enter an integer.")

  
# Function to calculate area and perimeter of a rectangle
def calculate_rectangle_info(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter


# Function to calcualte the area and perimeter of a square
def calculate_square_info(length):
  square_area = length * length
  square_perimeter = length * 4
  return square_area, square_perimeter


# The function to calculate area and perimeter of a triangle
def calculate_triangle_info(base, height):
    triangle_area = 0.5 * base * height
    # if right-angled triangle
    long_side = (base**2 + height**2)**0.5
    triangle_perimeter = base + height + long_side
    return triangle_area, triangle_perimeter

# get the function for the radius of the circle
def calculate_radius_info(radius):
    circle_area = 3.14159 * radius ** 2
    circle_perimeter = 2 * 3.14159 * radius
    return circle_area, circle_perimeter

#get the max and min inputs
def max_min(measurements):
  if 2 <= measurements <= 100:
      return True
  elif measurements < 2:
      print("Sorry we dont do measurements under 2mm")
      return False 
  else:
      print("Sorry we dont do measurements over 100mm ") 
      return False

#Main rotuine goes here
#yes no
question = yes_no("Do you want the instructions")

#shapes and angles
shapes_list = ["circle", "square", "rectangle", "triangle"]
angles_list = ["right angle", "obtuse", "iscosues"]

print(shapes_list)

for case in range(0, 1):
    shapes_list = Shapes("What shape would you like",
                                2, shapes_list)
    print("You chose", shapes_list)


#triangle
if shapes_list == "triangle":
  angles_list = ["right angle", "obtuse", "iscosues"]
  print(angles_list)

  for case in range(0, 1):
    angles_list = angle("What angle would you like for your triangle",
                                2, angles_list)
    print("You chose", angles_list)

#circle
if shapes_list == "circle":
    while True:
        shape_radius = input("Please enter the radius for your circle: ")
        
        try:
            shape_radius = float(shape_radius)
        except ValueError:
            print("Please enter a number")
            continue  
        
        if max_min(shape_radius):
            circle_area, circle_perimeter = calculate_radius_info(shape_radius)
            break  
        else:
            print("Please enter a valid raidus")
        
      

#sqaure and rectangle
if shapes_list == "square" or shapes_list == "rectangle":
    while True:
        length = shape_lenght("Please enter the shape's length") 

        if not max_min(length):
            print("Please enter a valid length")
            continue

        if shapes_list == "square":
            square_area, square_perimeter = calculate_square_info(length)
        elif shapes_list == "rectangle":
            width = shape_width("Please enter the shape's width")

            if not max_min(width):
                print("Please enter a valid width")
                continue

            area, perimeter = calculate_rectangle_info(length, width)
            # calculate rectangles area and perimeter
        break  

#get meausrements for triangle
if shapes_list == "triangle":
  while True:
    length = shape_lenght("Please enter the shape for your length")
  
    if not max_min(length):
      print("Please enter a valid length")
      continue  
      
    height = shape_lenght("Please enter the height for your triangle")
  
    if not max_min(length):
      print("Please enter a valid length")
      continue  
  
    triangle_area, triangle_perimeter = calculate_triangle_info(length, height)
    break


#show users their history 
#Display user histoy 
print("History")
print("Shape chosen",shapes_list)

if shapes_list == "circle":
    print("Radius", shape_radius)
    print("Circle Area", circle_area)
    print("Circle Perimeter", circle_perimeter)
elif shapes_list == "square":
    print("Lenght", length)
    print("Square Area", square_area)
    print("Square Perimeter", square_perimeter)
elif shapes_list == "rectangle":
    print("Lenght", length)
    print("Width", width)
    print("Rectangle Area", area)
    print("Rectangle Perimeter", perimeter)
elif shapes_list == "triangle":
    print("Base Lenght", length)
    print("Height Lenght", height)
    print("Triangle Area", triangle_area)
    print("Triangle Perimeter",  triangle_perimeter)