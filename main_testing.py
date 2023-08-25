# functions go here 
def yes_no(question):
  valid = False
  while not valid:
    response = input(question).lower().strip() 
    # input
    if response == "yes" or response == "y":
      response = "yes"
      print("Display insturctions")
      return response
  
    elif response == "no" or response == "n":
      response = "no"
      print("Program continues")
      return response

    else:
      print("Please enter yes or no")


question = yes_no("Do you want the instructions")

# Ask user for their shape
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


# main routine starts here
shapes_list = ["circle", "square", "retangle", "triangle"]
angles_list = ["right angle", "obtuse", "iscosues"]

print(shapes_list)

for case in range(0, 1):
    shapes_list = Shapes("What shape would you like",
                                2, shapes_list)
    print("You chose", shapes_list)

if shapes_list == "triangle":
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


  # main routine starts here
  angles_list = ["right angle", "obtuse", "iscosues"]
  print(angles_list)
  
  for case in range(0, 1):
      angles_list = angle("What angle would you like for your triangle",
                                  2, angles_list)
      print("You chose", angles_list)

if shapes_list == "circle":
  def radius(question):
    # checks users enter an integer to a given question 

  
    while True:

      try:
        response =  float(input(question))
        return response 

      except ValueError:
        print("Please enter an number.")


  # Main routine goes here 
  shape_raidus = 1
  raidus_asked = 0



  # ensures that there is a minimum and maximum 


  while True: 
    shape_raidus = radius("Please enter the radius for your circle ")
  
    if shape_raidus == raidus_asked:
      break
  
      if 2 <= shape_raidus <= 100:
        pass
      elif shape_raidus < 2:
        print("Sorry we dont do measurements under 2mm")
        continue 
      else:
        print("Sorry we dont do measurements over 100mm ") 
        continue
  
    raidus_asked += 1

if shapes_list == "square" "retangle":
  def shape_lenght(lenght):
  # functions go here 
  
  # checks users enter an integer to a given question 
  
    
    while True:
  
      try:
          response =  int(input(question))
          return response 
  
      except ValueError:
          print("Please enter an integer.")
  
  
  # Main routine goes here 
  # ensures that there is a minimum and maximum 
  
  
  while True: 
    lenght = shape_lenght("Please enter the lenght for your shape ")
  
  
    if 2 <= lenght <= 100:
        pass
    elif lenght < 2:
        print("Sorry we dont do measurements under 2mm")
        continue 
    else:
        print("Sorry we dont do measurements over 100mm ") 
        continue
  

