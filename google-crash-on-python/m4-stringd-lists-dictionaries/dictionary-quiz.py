# Question 1
# The email_list function receives a dictionary, which contains domain names as keys, and a list of users
#  as values.Fill in the blanks to generate a list that contains complete email addresses 
# (e.g. diana.prince@gmail.com).
def email_list(domains):
    # itrate over the domains dictionary to create a list of emails
    emails = []
    # iterate over the domains dictionary
    for domain, users in domains.items():
        # iterate over the users list for each domain
        for user in users:
            # concatenate the user name with the domain name using an f-string
            emails.append(f"{user}@{domain}")
    return emails

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))

# Question 2
# The groups_per_user function receives a dictionary, which contains group names with the list of users. 
# Users can belong to multiple groups. Fill in the blanks to return a dictionary with the users as keys
#  and a list of their groups as values. 
def groups_per_user(group_dictionary):
    # create a dictionary to hold the users as keys and a list of their groups as values
    user_groups = {}
    # iterate over the group_dictionary
    for group, users in group_dictionary.items():
        # iterate over the users list for each group
        for user in users:
            # if the user is already in the user_groups dictionary, append the group to their list
            if user in user_groups:
                user_groups[user].append(group)
            # if the user is not in the user_groups dictionary, add them with the current group as their first entry
            else:
                user_groups[user] = [group]
    return user_groups

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))

# Question 3
#The dict.update method updates one dictionary with the items coming from the other dictionary, 
# so that existing entries are replaced and new entries are added. What is the content of the
#  dictionary “wardrobe“ at the end of the following code?
wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
wardrobe.update(new_items)
print(wardrobe)
# Answer: {'shirt': ['red', 'blue', 'white'], 'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}

# Question 4
# The add_prices function returns the total price of all of the groceries in the  dictionary.
#  Fill in the blanks to complete this function.
def add_prices(basket):
    # initialize the total to 0
    total = 0
    # iterate over the dictionary items
    for item in basket.values():
        # add each price to the total
        total += item
    return round(total, 2)

groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59, 
	"coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

print(add_prices(groceries)) # Should print 28.44

#