# Introduction to APIs

# Objective create and use API in Python.

# An API (Application Programming Interface) is a set of rules and protocols that allows different 
# software applications to communicate with each other. 
# APIs enable developers to access specific features or data from another application, service, or 
# platform without needing to understand the underlying code or infrastructure.

# APIs are commonly used in web development to allow different web services to interact with each 
# other. For example, a weather application might use an API to retrieve weather data from a third-party
# service, or a social media platform might provide an API to allow developers to access user data
# and post content on behalf of users.

# APIs can be categorized into different types, including:
# 1. REST (Representational State Transfer) APIs: These are the most common type of APIs, which use
#    HTTP requests to access and manipulate resources.
# 2. SOAP (Simple Object Access Protocol) APIs: These are more complex APIs that use XML messages to
#    exchange data between applications.
# 3. GraphQL APIs: These are a newer type of API that allow clients to specify exactly what data they
#    need, reducing the amount of data transferred over the network.
# 4. WebSocket APIs: These APIs enable real-time communication between clients and servers using
#    persistent connections.

# To use an API, developers typically need to obtain an API key or access token, which is used to
# authenticate requests and track usage. APIs often have documentation that provides information on
# how to use the API, including available endpoints, request parameters, and response formats.
# Popular APIs include the Twitter API, Google Maps API, and Facebook Graph API, among many others.
# In Python, APIs can be accessed using libraries such as requests, which makes it easy to send HTTP
# requests and handle responses.

# Pandas also has built-in support for working with APIs, allowing users to easily retrieve and manipulate
# data from web services. The pandas.read_json() function can be used to read JSON data from an API endpoint
# and convert it into a pandas DataFrame for further analysis.

# Pandas is actually set of software components , much of which is not even written in Python.
import pandas as pd
import matplotlib.pyplot as plt
# When create a dataframe from a Dictionary, Pandas is actually using a C library called NumPy to handle the underlying data
# structures and operations. NumPy is a powerful library for numerical computing in Python, and it provides the foundation for many of the data manipulation and analysis capabilities in Pandas.
# Pandas also uses other libraries such as Matplotlib for data visualization and SciPy for scientific computing.
# Pandas is designed to work seamlessly with these libraries, allowing users to easily integrate data analysis
# and visualization into their workflows.
dict_={'a':[11,21,31],'b':[12,22,32]}
df=pd.DataFrame(dict_)
df
# When you create a Pandas object with the dataframe constructor, in API lingo this is an "instance". 
# The data in the dictionary is passed along to the pandas API. You then use the dataframe to communicate
# with the API.
# The API then calls the NumPy library to create the underlying data structures and perform operations 
# on the data.

# When you call the method head the dataframe communicates with the API displaying the first few rows 
# of the dataframe.
df.head() # output is a dataframe
# When you call the method mean, the API will calculate the mean and return the value.
df.mean() # output is a series

#  REST APIs:
# REST (Representational State Transfer) APIs are a type of web API that use HTTP requests to access
#  and manipulate resources.
# REST APIs are designed to be simple, scalable, and flexible, making them a popular choice for building
# web services and applications.
# REST APIs typically use standard HTTP methods such as GET, POST, PUT, DELETE, and PATCH to perform
# operations on resources.
# Resources are typically represented as URLs, and each resource can have multiple representations, such as JSON or XML.
# REST APIs are stateless, meaning that each request is independent and does not rely on any previous requests.
# REST APIs often use standard HTTP status codes to indicate the success or failure of a request.
# REST APIs can be secured using various authentication and authorization mechanisms, such as API keys,
# OAuth, or JWT (JSON Web Tokens).
# REST APIs are commonly used in web development to allow different web services to interact with each other
# and to provide access to data and functionality from third-party services.

# In this lab, we will use the NBA API to determine how well the Golden State Warriors performed against
# the Toronto Raptors. We will use the API to determine the number of points the Golden State Warriors 
# won or lost by for each game. So if the value is three, the Golden State Warriors won by three points.
# Similarly it the Golden State Warriors lost by two points the result will be negative two. 
# The API will handle a lot of the details, such a Endpoints and Authentication.

# It's quite simple to use the nba api to make a request for a specific team. We don't require a JSON,
#  all we require is an id. This information is stored locally in the API. We import the module teams.

import nba_api # this imports the entire nba_api package
from nba_api.stats.static import teams # this imports the teams module from the nba_api.stats.static package
# We can then use the teams module to get a list of all the teams in the NBA

def one_dict(list_dict):
    keys=list_dict[0].keys()
    out_dict={key:[] for key in keys}
    for dict_ in list_dict:
        for key, value in dict_.items():
            out_dict[key].append(value)
    return out_dict

def one_dict(list_dict):
    keys=list_dict[0].keys()
    out_dict={key:[] for key in keys}
    for dict_ in list_dict:
        for key, value in dict_.items():
            out_dict[key].append(value)
    return out_dict

# Get all teams
nba_teams=teams.get_teams()
#the first three item in the list
nba_teams[:3] # output is a list of dictionaries

# Convert list of dictionaries to a single dictionary of lists
nba_teams_dict=one_dict(nba_teams)
# Convert dictionary of lists to a dataframe
nba_teams_df=pd.DataFrame(nba_teams_dict)
nba_teams_df.head() # output is a dataframe

# Will use the team's nickname to find the unique id, we can see the row that contains the warriors
#  by using the column nickname as follows:
nba_teams_df[nba_teams_df['nickname']=='Warriors']

# The unique id for the Golden State Warriors is 1610612744. We will use this id to get the
#  game log for the Golden State Warriors.
from nba_api.stats.endpoints import teamgamelog, leaguegamefinder

# We can use the following line of code to access the first column of the DataFrame:
warriors_id=nba_teams_df[nba_teams_df['nickname']=='Warriors']['id'].values[0]

# The function "League Game Finder " will make an API call, it's in the module stats.endpoints.
warriors_games=teamgamelog.TeamGameLog(team_id=warriors_id)

# The output is an object of the class TeamGameLog. We can use the method get_data_frames to get the data
#  as a list of dataframes.
# The parameter team_id_nullable is the unique ID for the warriors. Under the hood, the NBA API is making
#  a HTTP request.
# The information requested is provided and is transmitted via an HTTP response this is assigned to the
#  object game finder
gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=warriors_id)

# The data is stored in a list of dataframes. In this case, there is only
gamefinder.get_data_frames()

# one dataframe in the list. We can access the dataframe using the index 0.
# The game finder object has a method 'get_data_frames()', that returns a dataframe. 
# If we view the dataframe, we can see it contains information about all the games the Warriors played.
# The PLUS_MINUS column contains information on the score, if the value is negative, the Warriors lost
# by that many points, if the value is positive, the warriors won by that amount of points.
# The column MATCHUP has the team the Warriors were playing, GSW stands for Golden State Warriors 
# and TOR means Toronto Raptors. vs signifies it was a home game and the @ symbol means an away game

games = gamefinder.get_data_frames()[0]
games.head()

# You can download the dataframe from the API call for Golden State and run the rest like a video.
import requests

filename = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%205/Labs/Golden_State.pkl"

def download(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)

download(filename, "Golden_State.pkl")
file_name = "Golden_State.pkl"
games = pd.read_pickle(file_name)
games.head()

# We can create two dataframes, one for the games that the Warriors faced the raptors at home, and 
# the second for away games.
home_games = games[games['MATCHUP'] == 'GSW vs. TOR']
away_games = games[games['MATCHUP'] == 'GSW @ TOR']

# We can calculate the mean for the column PLUS_MINUS for the dataframes games_home and  games_away:
home_mean = home_games['PLUS_MINUS'].mean()
away_mean = away_games['PLUS_MINUS'].mean()

# We can plot out the PLUS MINUS column for the dataframes games_home and  games_away. 
# We see the warriors played better at home.
fig, ax = plt.subplots()

away_games.plot(x='GAME_DATE',y='PLUS_MINUS', ax=ax)
home_games.plot(x='GAME_DATE',y='PLUS_MINUS', ax=ax)
ax.legend(["away", "home"])
plt.show()

# Calculate the mean for the column PTS for the dataframes games_home and  away_games:
home_points = home_games['PTS'].mean()
away_points = away_games['PTS'].mean()


