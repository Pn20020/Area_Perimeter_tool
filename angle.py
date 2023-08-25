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

