# Part 1: Discussion
# What are the three main design advantages that object orientation can provide?

# 1. Abstraction, as long as the program works we don't need to know about the details.
#2. Encapsulation because the data (attributes) related to the object can be kept near the  object.
#3. Polymorphism can have the same names and methods calls. Therefore, don't need to use conditionals for each different scenerio.

# Explain each concept.

# 1. What is a class?
    # Class is similar to a dictionary; however, it is more powerful because:
        # Stores data
        # kinda flexible
        # has structure
        # has its own smarts because it has attributes, subclasses, and methods.

# 2. What is an instance attribute?

    #The instance attribute is different from a class attribute. Instance attribute is an attribute that is specific to that specific instance. On the other hand, class attribute is applicable for all instances. However, if a instance has its own instance attribute, that instance will be bound to its attribute instead of the class attribute. For example, For dog, age = 9 as a class attribute. For Morfy, which is a kind of dog (instance), has an age of 3. In this case, age = 3 is an attribute (instance attribute) specifically for Morfy.

# 3. What is a method?

    # A method is a function that has been defined on a class.

# 4. What is an instance in object orientation?

    # An instance is an individual instance of a class. Instances are particular files or string. Instance is the equivalent of object.


# 5. How is a class attribute different than an instance attribute? Give an example of when you might use each.

    # See question 2 for explanation.

# Parts 2 through 5:
# Create your classes and class methods


class Student(object):

    def __init__(self, first_name, last_name, address):
        """Initialize student attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question(object):

    def __init__(self, question, correct_answer):
        """Initialize question attributes"""
        self.question = question
        self.correct_answer = correct_answer
