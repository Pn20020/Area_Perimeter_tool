import shape_width
# functions go here 
def yes_no(question):
  valid = False
  while not valid:
    response = input(question).lower().strip() 
    # input
    if response == "yes" or response == "y":
      response = "yes"
      print("We will ask you to choosea shape and pick its dimensions (in mm only). We will calcuate the area and perimeter of the shape for you in mm ")
      return response
  
    elif response == "no" or response == "n":
      response = "no"
      print("Program continues")
      return response

    else:
      print("Please enter yes or no")



question = yes_no("Do you want the instructions")

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

print(shapes_list)

for case in range(0, 1):
    shapes_list = Shapes("What shape would you like",
                                2, shapes_list)
    print("You chose", shapes_list)

