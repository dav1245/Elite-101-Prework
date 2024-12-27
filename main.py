print ("Welcome to the amazing.. and mediocre.. Chatbot!")
name = input ("First, what's your name? ")
age = input ("Second, what's your age? ")
if int(age) < 18:
    print ("Huh? " + name + ", you're a kid.")
if int(age) >= 18:
    print ("Oooh! " + name + ", you're an adult!")
if int(age) >= 45:
    print ("Nice, " + name + ", you're a middle aged adult." ) 
if int(age) >= 65:
    print ("Hello, sir " + name + ". You're pretty old.")

question = input ("Since you're here, do you wanna chat? I'm a CHATbot for a reason. Answer Yes or No: ")

if question == "Yes":
   
    print ("Great. Here are the options:")
Menu = ['First: Food?', 'Second: Movies?', 'Third: TV Shows?', 'X-it: Exit?']
for i in sorted(Menu):
    print(i)

options = input ("Choose one, but there's a twist: if you choose a word, you can never go back to that word or any words before it. Choose wisely.. (The words are: First, Second, Third or X-it): ")

if options == "First":
    print ("I'm gonna give you a fact and then redirect you to the menu. I might be a CHATbot but I'm not that chatty! Let's talk about pizza.")
    print ("Did you know that Pizza originated in Naples, Italy, the word pizza means pie in Italian, and the first recorded use of the word pizza was in a Latin text from Gaeta, Italy in 997 AD? The more you know!")
Menu = ['First: Food?', 'Second: Movies?', 'Third: TV Shows?', 'X-it: Exit?']
for i in sorted(Menu):
    print(i)
first_options = input ("Choose again, but this time you can only type words Second, Third and X-it: ")

if first_options == "Second":
    print ("Let's talk about movies. I'll talk about my favorite one, and then redirect you back to the menu.")
    print ("The Wild Robot. It just came out this year, but it gives deep messages about the mistakes we make and the lessons we learn. It’s a heartwarming story about chosen families and about taking responsibility. I love those kinds of movies.")
Menu = ['First: Food?', 'Second: Movies?', 'Third: TV Shows?', 'X-it: Exit?']
for i in sorted(Menu):
    print(i)


if first_options == "Third":
    print ("TV Shows. Everyone loves 'em. I'll talk about my favorite, and then redirect you to the menu.")
    print ("Doctor Who. One of the greatest of all time. My most favorite quote is from the 12th Doctor, who says that Human progress isn’t measured by industry. It’s measured by the value you place on a life. An unimportant life. A life without privilege. The boy who died on the river, that boy's value is your value. That's what defines an age. That's what defines a species.")
Menu = ['First: Food?', 'Second: Movies?', 'Third: TV Shows?', 'X-it: Exit?']
for i in sorted(Menu):
    print(i)


if first_options == "X-it":
    print ("Nice meeting you. See ya next time, if ever.")

elif options == "Second":
    print ("Let's talk about movies. I'll talk about my favorite one, and then redirect you back to the menu.")
    print ("The Wild Robot. It just came out this year, but it gives deep messages about the mistakes we make and the lessons we learn. It’s a heartwarming story about chosen families and about taking responsibility. I love those kinds of movies.")
Menu = ['First: Food?', 'Second: Movies?', 'Third: TV Shows?', 'X-it: Exit?']
for i in sorted(Menu):
    print(i)
second_options = input ("Choose again, but this time you can only choose between the words Third and X-it: ")

if second_options == "Third":
    print ("TV Shows. Everyone loves 'em. I'll talk about my favorite, and then redirect you to the menu.")
    print ("Doctor Who. One of the greatest of all time. My most favorite quote is from the 12th Doctor, who says that Human progress isn’t measured by industry. It’s measured by the value you place on a life. An unimportant life. A life without privilege. The boy who died on the river, that boy's value is your value. That's what defines an age. That's what defines a species.")
Menu = ['First: Food?', 'Second: Movies?', 'Third: TV Shows?', 'X-it: Exit?']
for i in sorted(Menu):
    print(i)

if second_options == "X-it":
    print ("Nice meeting you. See ya next time, if ever.")

elif options == "Third":
    print ("TV Shows. Everyone loves 'em. I'll talk about my favorite, and then redirect you to the menu.")
    print ("Doctor Who. One of the greatest of all time. My most favorite quote is from the 12th Doctor, who says that Human progress isn’t measured by industry. It’s measured by the value you place on a life. An unimportant life. A life without privilege. The boy who died on the river, that boy's value is your value. That's what defines an age. That's what defines a species.")
Menu = ['First: Food?', 'Second: Movies?', 'Third: TV Shows?', 'X-it: Exit?']
for i in sorted(Menu):
    print(i)
third_options = input ("Choose again, but you can only, well, leave. Your last option is to type the word X-it: ")

if third_options == "X-it":
    print ("Nice meeting you. See ya next time, if ever.")

elif options == "X-it":
    print ("Nice meeting you. See ya next time, if ever.")

elif question == "No":
    print ("Alright, " + name + ". Bye.")
