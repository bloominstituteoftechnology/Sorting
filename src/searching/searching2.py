# Title: binary search experiment 2020.03.15 v2 11:41ET GGA
# note...the number division system here probably runs into too many edge cases
# is better to change frame of reference to the region of search
# rather than referring to the fraction of the whole original data set

# setting variables:

# what you are searching for
# set by user
search_target = int(input("What number do you want to search for? Your Answer: "))

# the list_to_search
list_to_search = []

# in this case: setting list to a random sorted list made above
list_to_search = numbers

# relative boundaries on size of dataset
# lower boundary starting at the beginning
lower_bound = 0
# upper boundary starting at the end
upper_bound = len(list_to_search)

# we will also use:
# location_observed

step_counter = 1

# Print starting data
# print("Step 1")
print("Total number of locations: ", len(list_to_search))
# print(f"The first searching location (counting from zero) was: [{location_observed}], value: {list_to_search[location_observed]}")

# location_observed = lower_bound + (upper_bound - lower_bound) // 2

# 1. half the list: start in the middle of the list
# location_observed =
while lower_bound != upper_bound:

    # incriment step counter
    step_counter += 1
    # print step counter
    print("Step ", step_counter)

    # increment the search counter
    location_observed = lower_bound + (upper_bound - lower_bound) // 2

    # testing and inspection
    # print("lower", lower_bound)
    # print("upper", upper_bound)
    # print("location_observed", location_observed)
    # print(f"The next searching location (counting from zero) was: [{location_observed}], value: {list_to_search[location_observed]}")

    # check to see if the answer is correct: if so print and finish
    if list_to_search[location_observed] == search_target:

        # 2. if the item equals the target: print the location of the target
        # here the list-item is used to display the search target as a kind of error check
        print(f"Finished: Search performed in {step_counter} steps.")
        print(
            f"Search result: [{location_observed}] is the list location of your target: {list_to_search[location_observed]}"
        )

        if list_to_search[location_observed] != search_target:
            print("Error: result does not match search target")
        break

    if step_counter > 100:
        print("Your search result may not exist.")
        break

    # 3. if search_target is higher, go to middle of half of 'above that point' section
    # e.g. from .5 to .75
    # which is the current location
    if search_target > list_to_search[location_observed]:

        # This can be triggered when the number doesn't exit.
        # protecting against an edge case:
        # exit this innter loop if you hit the lower bound
        if lower_bound == location_observed:
            print("Your search result may not exist.")
            break

        # otherwise, set the lower_bound to your current_search_location
        lower_bound = location_observed

        # inspection/testing
        print("Target is >")
        print(
            f"The next searching location (counting from zero) was: [{location_observed}], value: {list_to_search[location_observed]}"
        )

    # 4. if search_target is lower, got to middle of half of 'above that point' section
    # e.g. from .5 to .25
    if search_target < list_to_search[location_observed]:

        # then the current search location becomes the new upper bound.
        upper_bound = location_observed

        # inspection/testing
        print("Target is <")
        print(
            f"The next searching location (counting from zero) was: [{location_observed}], value: {list_to_search[location_observed]}"
        )

    # if search goes on more than 50 steps, manually check to see if number exists:
    if step_counter > 50:
        break

    # 5. repeat (goes back to top of while loop)
    # continue looking until the the search target matches the location observed
    # in the target sorted list
