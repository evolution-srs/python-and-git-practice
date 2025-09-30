x = 5 
while x != 2: 
    print(x) 
    x = x - 1 # output: 5, 4, 3

items = ["Vase", "Statue", "Mask"]
for index, item in enumerate(items, start=1):
    print(f"Exhibit {index}: {item} - Ancient Greece")
# output: Exhibit 1: Vase - Ancient Greece
#         Exhibit 2: Statue - Ancient Greece
#         Exhibit 3: Mask - Ancient Greece

class Points(object): 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 
    def print_point(self): 
        print('x=', self.x, ' y=', self.y) 
p2 = Points(1, 2) 
p2.x = 'A' 
p2.print_point() # output: x= A  y= 2



def validate_temperature(reading): 
    if 20 <= reading <= 40: 
        result = "Valid" 
    else: 
        result = "Invalid" 
    return result
print(validate_temperature(32)) # output: Valid

total_budget = 1000 
def calculate_remaining(spent): 
    total_budget = 500 
    return total_budget - spent 
print(calculate_remaining(200)) # output: 300