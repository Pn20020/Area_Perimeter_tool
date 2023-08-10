def Lenght(question):
# functions go here 

# checks users enter an integer to a given question 

  
  while True:

    try:
        response =  int(input(question))
        return response 

    except ValueError:
        print("Please enter an integer.")


# Main routine goes here 

lenght = Lenght("Please enter the lenght for your shape ")
