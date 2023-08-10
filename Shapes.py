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
