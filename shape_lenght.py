def shape_lenght(question):
# functions go here 

# checks users enter an integer to a given question 

  
  while True:

    try:
        response =  int(input(question))
        return response 

    except ValueError:
        print("Please enter an integer.")


# Main routine goes here 
max_lenght = 1
lenght_asked = 0 

while True:

  lenght = shape_lenght("Please enter the lenght for your shape ")
  
  if max_lenght == lenght_asked:
    break


  lenght_asked += 1 