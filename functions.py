#Functions

#Function containing a variable
def hello(name):
    print('Hello! ' + name)

hello('Brandon')

#Function containing two variables and one variable is converted to a
#string
def hello2(name, age):
    print('Hello ' + name + ' you are ' + str(age) + ' years old' )

hello2('Brandon', 37)

def talk(phrase):
    def say(word):
        print(word)
        
    words = phrase.split(' ')
    for word in words:
        say(word)
        
talk('I am going to buy the milk')

def count():
    count = 0
    
    def increment():
        nonlocal count
        count = count + 1
        print(count)
        
    increment()
    
count()