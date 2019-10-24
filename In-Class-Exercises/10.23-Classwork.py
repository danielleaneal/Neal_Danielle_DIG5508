#10.23.19 Classwork
#Regular Expressions - can be used for text processing tasks without using
#for and while loops. Helps to find patterns in text so you can extract
#info from text and do useful things with it.
#in a reg expr \w for word character (between A and Z)
#methods for reg expr: matching re.match and searching

#?=optional (h?i would match something that always includes i, but optionally includes h
# before it).


#Groups - separate parts of the strings

#%%
import re


#%%
import re
# txt = "The rain in Spain"
x = re.search("a*",)
print(x) 


#%%
import re
#US Zip Code (either 5 or 5+4)
zipcode1 = "32124"
zipcode2 = "32124-2432"
zipcode3 = "oue32"


#%%
import re
x = re.search("\d{5}", 32124)
print(x)
#




















































#Work For Classes
#%%

class MyClass:

    """A simple example class"""

    i = 12345

    def __init__(self, name):

        self.name = name

    def f(self):

        return 'hello world from ' + self.name



#%%

aClass = MyClass("John")

print(aClass.f())

bClass = MyClass("Lucy")

print(bClass.f())



#%%

import json

data = {

    "president": {

        "name": "Zaphod Beeblebrox",

        "species": "Betelgeusian"

    }

}

#%% 

with open('out.json','w') as fh:

    json.dump(data, fh)



#%%

# Importing data from a json file:

with open('out.json', 'r') as nfh:

    obj = json.load(nfh)

    print(obj)

    print(obj["president"]["name"])



#%%