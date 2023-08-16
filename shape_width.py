def shape_width(question):
# functions go here 

# checks users enter an integer to a given question 

  
  while True:

    try:
        response =  int(input(question))
        return response 

    except ValueError:
        print("Please enter an integer.")


# Main routine goes here 
max_width = 1
width_asked = 0



# ensures that there is a minimum and maximum 


while True: 
  width = shape_width("Please enter the width for your shape ")

  if max_width == width_asked:
    break

  if 2 <= width <= 100:
      pass
  elif width < 2:
      print("Sorry we dont do measurements under 2mm")
      continue 
  else:
      print("Sorry we dont do measurements over 100mm ") 
      continue

  width_asked += 1