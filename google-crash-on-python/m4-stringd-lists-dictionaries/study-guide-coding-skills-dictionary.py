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

# Skill Group 3 

# Use the dictionary[key] = value operation to associate a value with a key in a dictionary.   

# Iterate over keys with multiple values from a dictionary, using nested for loops and an if-statement,
#  and the dictionary.items() method.

# Use the dictionary[key].append(value) method to add the key, a string, and the key for each item in 
# the dictionary.
# This function receives a dictionary, which contains resource 
# categories (keys) with a list of available resources (values) for a 
# company’s IT Department. The resources belong to multiple categories.
# The function should reverse the keys and values to show which 
# categories (values) each resource (key) belongs to.

def invert_resource_dictionary(resource_dictionary):
    # Initialize a "new_dictionary" variable as a dict data type.
    new_dictionary = {}
    # The outer for loop iterates through each "category" key and 
    # associated "resources" values, in the "resource_dictionary" items.
    for category, resources in resource_dictionary.items():
        # The inner for loop iterates through each "resource" in the
        # list of "resources" for the current "category".
        for resource in resources:
            # The if-statement checks if the current "resource" value
            # is not already a key in the "new_dictionary".
            if resource in new_dictionary:
                # If True, then append the current "category" value to
                # the existing list of categories for the current 
                # "resource" key.
                new_dictionary[resource].append(category)
            else:
                # If False,then add the "resource" value (as a key) to the
                # "new_dictionary" and assign the associated value as a 
                # new list with the current "category" value as the first
                # item in the list.
                new_dictionary[resource] = [category]
    # Return the new "new_dictionary" once the outer for loop has 
    # completed all iterations.
    return(new_dictionary)

print(invert_resource_dictionary({"Hard Drives": ["IDE HDDs", "SCSI HDDs"],
        "PC Parts":  ["IDE HDDs", "SCSI HDDs", "High-end video cards", "Basic video cards"], "Video Cards": ["High-end video cards", "Basic video cards"]}))
# Should print {'IDE HDDs': ['Hard Drives', 'PC Parts'], 'SCSI HDDs': ['Hard Drives', 'PC Parts'], 'High-end video cards': ['PC Parts', 'Video Cards'], 'Basic video cards': ['PC Parts', 'Video Cards']}
my_dictionary = {"keyA": ["value1", "value2"], "keyB": ["value3", "value4"]}