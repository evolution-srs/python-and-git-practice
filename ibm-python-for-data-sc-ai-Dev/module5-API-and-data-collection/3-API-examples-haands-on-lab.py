# API Examles 
# Random User and Fruityvice API Example

# 1-Load and use RandomUser API, using RandomUser() Python library
# 2-Load and use Fruityvice API, using requests Python library
# 3-Load and use Open-Joke-API, using requests Python library

# The advantages of using APIs:

# 1-Automation. Less human effort is required and workflows can be easily updated to become faster 
# and more productive.
# 2-Efficiency. It allows to use the capabilities of one of the already developed APIs than to try 
# to independently implement some functionality from scratch.

# The disadvantage of using APIs:

# Security. If the API is poorly integrated, it means it will be vulnerable to attacks, resulting in 
# data breeches or losses having financial or reputation implications.

#Example 1: RandomUser API
# After install randomuser library will load the nessesary livraries
from randomuser import RandomUser
import pandas as pd

# First, we will create a random user object, r.
r=RandomUser()

#Then, using generate_users() function, we get a list of random 10 users.
some_list=r.generate_users(10)
some_list

# The "Get Methods" functions can generate the required parameters to construct a dataset.
# For example, to get full name, we call get_full_name() function.
name=r.get_full_name()
# Let's say we only need 10 users with full names and their email addresses.
#  We can write a "for-loop" to print these 10 users.
for user in some_list:
    print (user.get_full_name()," ",user.get_email())

# generate photo for the 10 users
for user in some_list:
    print (user.get_picture())

# To generate a table with information about the users, we can write a function containing all desirable
# parameters. For example, name, gender, city, etc. The parameters will depend on the requirements of
# the test to be performed. We call the Get Methods, listed at the beginning of this notebook.
# Then, we return pandas dataframe with the users.
def get_users():
    users =[]
     
    for user in RandomUser.generate_users(10):
        users.append({"Name":user.get_full_name(),"Gender":user.get_gender(),"City":user.get_city(),"State":user.get_state(),"Email":user.get_email(), "DOB":user.get_dob(),"Picture":user.get_picture()})
      
    return pd.DataFrame(users)         
get_users()
df1 = pd.DataFrame(get_users())  
print(df1)

# Example 2: Fruityvice API
# well import the libraries
import requests
import json

#We will obtain the fruityvice API data using requests.get("url") function. The data is in a json format
data = requests.get("https://web.archive.org/web/20240929211114/https://fruityvice.com/api/fruit/all")

# We will retrieve results using json.loads() function.
results = json.loads(data.text)

# We will convert our json data into pandas data frame.
pd.DataFrame(results)

# The result is in a nested json format. The 'nutrition' column contains multiple subcolumns, 
# so the data needs to be 'flattened' or normalized.
df2 = pd.json_normalize(results)
print(df2)
# Let's see if we can extract some information from this dataframe.
#  Perhaps, we need to know the family and genus of a cherry.
cherry = df2.loc[df2["name"] == 'Cherry']
(cherry.iloc[0]['family']) , (cherry.iloc[0]['genus'])
# find out how many calories are contained in a banana.
cal_banana = df2.loc[df2["name"] == 'Banana']
cal_banana.iloc[0]['nutritions.calories']


# Exersice 3 This page url='https://mixedanalytics.com/blog/list-actually-free-open-no-auth-needed-apis/'contains a list of free public APIs for you to practice.
#  Let us deal with the following example.
# Official Joke API
# This API returns random jokes from a database. 
# The following URL can be used to retrieve 10 random jokes. https://official-joke-api.appspot.com/jokes/ten
data2 = requests.get("https://official-joke-api.appspot.com/jokes/ten")

# Import the library json: JavaScript Object Notation
import simplejson
import django
# Retrieve results using json.loads() function
results2 = simplejson.loads(data2.text)

# Convert json data into pandas data frame. Drop the type and id columns.
df3 = pd.DataFrame(results2)
df3.drop(columns=["type","id"],inplace=True)
print(df3)
