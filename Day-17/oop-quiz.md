# Quiz Project

Create a quiz using OOP, I need to create the OOP files.

## Syntax of OOP
```python
# Create a Class
class User:
    # Initialize attributes
    def __init__(self, user_id, username): 
        # Create attributes
        self.id = user_id
        self.username = username
        # Create default attributes
        self.followers = 0
        self.following = 0
        
    # Create methods
    def follow(self, user):
        self.following += 1
        user.followers += 1
        

# Initialize an object from a class, add the init attributes.
user_1 = User(user_id="001", username="George")
user_2 = User(user_id="002", username="Maz")

# # Create an attribute after the class declaration
# user_2.id = "001" # Create an attribute called id with the value of "001"
# user_2.username = "George"

# Access attributes
print(user_1.id) # Prints 001
print(user_1.username) # Print George
print(user_1.followers) # Print 0

# Calling the follow method
# This will add the user 2 one follower and the user 1 one following.
user_1.follow(user_2)

```
- `self` is the object calling the method or attribute


## Modularity
I was able to change all the questions without needing to change multiple lines of code.
Disadvantage of simple procedural code.