# Let's create a dictionary, the functional way
 
# Create your dictionary class
class my_dictionary(dict):
 
  # __init__ function
  def __init__(self):
    self = dict()
 
  # Function to add key:value
  def add(self, key, value):
    self[key] = value
 
 
# Main Function
dict_obj = my_dictionary()
 
dict_obj.add('fname', 'Geeks')
dict_obj.add('mname', 'forGeeks')
dict_obj.add('lname', 'for for Geeks')
 
print(dict_obj)