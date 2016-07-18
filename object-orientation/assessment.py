"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

       1. Encapsulation: Data lives close to its functionality. Keeping everything
          together.

       2. Abstraction: Hiding with the intent to reduce complexity. You abstract 
          complexity of how it works so you have a well defined interface. Don't
          need to know info a method uses internally. Hiding details we don't need. 

       3. Polymorphisim: To make different, interchagable types. Flexibility of 
          types without conditionals. Exploiting the similarity. Interchangeability 
          of components.

2. What is a class?
        A class is the core of object-oriented programming. 
        "Type" of thing, like string or File

3. What is an instance attribute?
        The sticky note to the instance
        i.e. 
            instance attribute: fido.name = "Fido"

4. What is a method?
        A function defined within a class 

5. What is an instance in object orientation?
        An individual instance of a class (a particular string of file)
        i.e.:
            fido = Pet ()

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.
        A class attribute belongs to the class, and anytime an instance is created 
        in that class it is given the class attributes. While an instance attribute 
        is specific to that instance and only applies to that instance. 

        The process of finding an attribute is first it looks on itself, then it 
        looks in the class. 

        Say you create a class called Pizza, and you know all your pizza will have 
        white dough. You can create a dough = white rather then specifiying for each 
        instance created. In this same class once you created a instance. You get a 
        plain white pizza but on this specific pizza you want to put mushrooms so you 
        do npizza.toppings = mushrooms

class Pizza (object):
    dough = "white"
    sauce = "tomato"
    cheese = "mozzarella"
    topping = None
    # lines 51 - 54 are class attritbute, each time an instance is created it is 
    given these attritbutes

    
npizza = Pizza() #creating an instance
npizza.dough #checking for the class attribute 
'white'
npizza.topping = "mushrooms" #giving it a instance attribute, specific to npizza
npizza.topping  #checking instance attribute 
'mushrooms'

"""


#Part 2:

#Part 2 - Question 1:
class Student(object):

    def __init__(self, f_name, l_name, address):

        self.f_name = f_name
        self.l_name = l_name
        self.address = address


#Part 2 - Question 2:
class Question(object):

    def __init__(self, question, correct_answer):

        self.question = question
        self.correct_answer = correct_answer

#Part 3 - Question 2:
    def ask_and_evaluate(self):

        self.answer = raw_input(self.question + " > ")

        if self.answer == self.correct_answer:
       
            self.answer_right = True
            print self.answer_right

        else:

            self.answer_right = False
            print self.answer_right


#Part 2 - Question 3:
class Exam(object):

    def __init__(self, name):
        self.name = name
        self.questions = []

#Part 3 - Question 1:
    def add_questions(self, question, correct_answer):
        added_question = Question(question, correct_answer)
        self.questions.append(added_question)

#Part 3 - Question 3:
    def administer(self):
        score = 0

        for question in self.questions: 

        self.question = raw_input(self.questions)

        if self.question == self.correct_answer:
            print "Your answer is correct"
            score += 1 
        else:
            print "Answer is Incorrect"
