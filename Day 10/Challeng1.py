def format_name(f_name , l_name):
    #objective is to return the given name wtv case it is given in , the returned name must be in title case
    """" Returns the given name in Camel Case , if valid inputs are provided"""
    if f_name == "" or l_name == "":
        return
    # this will return None , coz the user would not have provided a valid input
    first = f_name.title()
    last = l_name.title()
    return first + " " + last

formatted_name = format_name(input("Enter your first name? ") , input("Enter your last name? "))
print(formatted_name)