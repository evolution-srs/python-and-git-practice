# **Coding Skills**

# Skill Group one:

# Iterate over the key and value pairs of a dictionary using a for loop with the dictionary.items() method 
# to calculate the sum of the values in a dictionary. 

# This function returns the total time, with minutes represented as 
# decimals (example: 1 hour 30 minutes = 1.5), for all end user time
# spent accessing a server in a given day. 

def sum_server_use_time(Server):
    # Initialize the variable as a float data type, which will be used
    # to hold the sum of the total hours and minutes of server usage by
    # end users in a day.
    total_use_time = 0.0
    # Iterate through the key and value pairs of the Server dictionary using
    # the .items() method.
    for value in Server.values():
        # For each end user, add the associated time value to the
        # total sum of all end user use time.
        total_use_time += value
    # Round the return value and limit to 2 decimal places.
    return round(total_use_time, 2)
FileServer = {"EndUser1": 2.25, "EndUser2": 4.5, "EndUser3": 1, "EndUser4": 3.75, "EndUser5": 0.6, "EndUser6": 8}

print(sum_server_use_time(FileServer)) # Should print 20.1

#Skill Group Two

# Concatenate a value, a string, and the key for each item in the dictionary and append to the end of a new list[ ] using
#  the list.append(x) method.  

# Iterate over keys with multiple values from a dictionary using nested for loops with the dictionary.items() method.

# This function receives a dictionary, which contains common employee 
# last names as keys, and a list of employee first names as values. 
# The function generates a new list that contains each employees’ full
# name (First_name Last_Name). For example, the key "Garcia" with the 
# values ["Maria", "Hugo", "Lucia"] should be converted to a list 
# that contains ["Maria Garcia", "Hugo Garcia", "Lucia Garcia"].

def list_full_names(employee_dictionary):

    # Initialize the "full_names" list as an empty list.
    full_names = []

    # The outer for loop iterates through each "last_name" key and 
    # associated "first_name" values, in the "employee_dictionary" items.
    for last_name, first_names in employee_dictionary.items():

        # The inner for loop iterates through each "first_name" in the
        # list of "first_names" for the current "last_name".
        for first_name in first_names:

            # Append the new "full_names" list with the "first_name" value
            # concatenated with a space " ", and the key "last_name". 
            full_names.append(first_name + " " + last_name)

    # Return the new "full_names" list once the outer for loop has 
    # completed all iterations.             
    return(full_names)

print(list_full_names({"Ali": ["Muhammad", "Amir", "Malik"], "Devi": ["Ram", "Amaira"], "Chen": ["Feng", "Li"]}))
# Should print ['Muhammad Ali', 'Amir Ali', 'Malik Ali', 'Ram Devi', 'Amaira Devi', 'Feng Chen', 'Li Chen']
