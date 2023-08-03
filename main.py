import Shapes
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

