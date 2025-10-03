# HTTP and Requests

# Objective: 
# 1- Understand HTTP
# 2- Handle HTTP Requests

# Uniform Resource Locator:URL
# Uniform resource locator (URL) is the most popular way to find resources on the web.
#  We can break the URL into three parts.
# 1-Scheme: This is this protocol, for this lab it will always be http://
# 2-Internet address  This will be used to find the location here are some examples: www.ibm.com and  www.gitlab.com 
# 3-Route:- Location on the web server for example: /images/IDSNlogo.png

# Request in Python
# Requests is a Python Library that allows you to send HTTP/1.1 requests easily.
#  We can import the library as follows:
import requests

# We will also use the following libraries:
import os
from PIL import Image
from IPython.display import IFrame

# You can make a GET request via the method get to www.ibm.com:
url='https://www.ibm.com/'
r=requests.get(url)

# We have the response object r, this has information about the request, like the status of the request.
# We can view the status code using the attribute status_code
r.status_code

# You can view the request headers:
print(r.request.headers)

# You can view the request body, in the following line, 
# as there is no body for a get request we get a None:
print("request body:", r.request.body)

# You can view the HTTP response header using the attribute headers. 
# This returns a python dictionary of HTTP response headers

header=r.headers
print(r.headers)

# We can obtain the date the request was sent using the key Date.
header['Date']
# Content-Type indicates the type of data
header['content-Type']

#You can also check the encoding:
r.encoding

# As the Content-Type is text/html we can use the attribute text to display the HTML in the body. 
# We can review the first 100 characters:
r.text[0:100]

# You can load other types of data for non-text requests, like images. Consider the URL of the following image:
url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/IDSNlogo.png'

# we can make a get request
r_img=requests.get(url)

# An image is a response object that contains the image as a bytes-like object. As a result, we must save it using a file object. 
# First, we specify the file path and name
path=os.path.join(os.getcwd(),'image.png')

# We save the file, in order to access the body of the response we use the attribute content 
# then save it using the open function and write method:
# Save image to disk

with open (path,'wb') as f:
    f.write(r.content)
Image.open(path)    

# Download a file 
# make a GET request for the image
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt'
path = os.path.join(os.getcwd(),'example1.txt')
r=requests.get(url)
with open(path,'wb') as f:
    f.write(r.content)
    