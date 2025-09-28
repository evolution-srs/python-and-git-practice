# Project Scenario:
# You are tasked with creating a daily report to track machine usage in a company by processing 
# event data.
# 1- Input and Event class:
# •	The input for the script is a list of event objects, each containing attributes: 
# date, user name, machine name, and event type .
# •	The relevant event types for this task are login and logout.
# 2- Output requirements:
# •	The output should be a report listing all machine names, with current users logged in to each machine.
# •	The report can be formatted in various ways, but a simple approach is to print the machine name
#  followed by the users' names separated by commas.
# 3- Proplem Statement:
# •	The main goal is to process the event objects to generate a report that shows
#  which users are currently logged into which machines.

def get_event_date(event):
    return event.date

def current_users(events):
    # Sort events by date to process them in chronological order
    events.sort(key=get_event_date)
    # Create a dictionary to track users logged into each machine 
    machines = {}
    # iterate through each event
    for event in events:
        # Check if the machine is already in the dictionary, if not, add it with an empty set
        if event.machine not in machines:
            machines[event.machine] = set()
        # Check the event type and update the machine's user list accordingly
        if event.type == 'login':
            machines[event.machine].add(event.user)
        elif event.type == 'logout':
            machines[event.machine].discard(event.user)
    return machines

# Generate the report
def generate_report(machines):
    # Itirate through each event and update the machine's user list accordingly
    for machine, users in machines.items():
        # check if there are users logged in to the machine
        if len(users) > 0:
            # Join the user names into a single string separated by commas
            user_list = ', '.join(users)
            # Print the machine name and the list of users
            print("{}: {}".format(machine, user_list))

# No output should be generated from running the custom function definitions above. 
# To check that our code is doing everything it's supposed to do, we need an Event class. 
# The code in the next cell below initializes our Event class. Go ahead and run this cell next.
class Event:
    def __init__(self, event_date, event_type, machine_name, user):
        self.date = event_date
        self.type = event_type
        self.machine = machine_name
        self.user = user
# we have an Event class that has a constructor and sets the necessary attributes.
# Next let's create some events and add them to a list by running the following cell.
events = [
  Event('2020-01-21 12:45:46', 'login', 'myworkstation.local', 'jordan'),
  Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
  Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
  Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
  Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
  Event('2020-01-23 11:24:35', 'login', 'mailserver.local', 'chris'),
]

users = current_users(events)
print(users)

generate_report(users)
 
