print ("Welcome to the amazing.. and mediocre.. online clothing retailer!")
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

question = input ("Since you're here, do you want to return or exchange items? Answer BUY or RETURN: ")

if question == "RETURN":
   
    print ("Great. Here's what you can return. Type First, Second, Third, or X-it.")
Menu = ['First: Shirts', 'Second: Shoes', 'Third: TVs', 'X-it: Exit']
for i in sorted(Menu):
    print(i)
    
options = input ("Choose an option: ")

if options == "First":

    shirts = input ("How many do you want to return?: ")
    brand1 = input ("What's the brand of the shirts?: ")
    type = input ("What's the type of shirt you're returning?: ")
    print ("Thank you for returning " + shirts, brand1, type + " shirts!")

elif options == "Second":

    shoes = input ("How many do you want to return?: ")
    brand2 = input ("What's the brand of the shoes?: ")
    type2 = input("What is the type of shoe you're returning?: ")
    print ("Thank you for returning " + shoes, brand2, type2 + " shoes!")

elif options == "Third":

    TVs = input ("How many do you want to return?: ")
    brand3 = input ("What's the brand of the TVs?: ")
    type3 = input ("What's the type of TV you're returning?: ")

    print ("Thank you for returning " + TVs, brand3, type3 + " TVs!")

elif options =="X-it":
    print ("Bye!")




elif question == "BUY":
    
    print ("Great. Here's what you can buy. Type First, Second, Third, or X-it.")
Menu = ['First: Shirts', 'Second: Shoes', 'Third: TVs', 'X-it: Exit']
for i in sorted(Menu):
    print(i)
    
options2 = input ("Choose an option: ")

if options2 == "First":


    shirts2 = input ("How many do you want to buy?: ")
    brand4 = input ("What's the brand of the shirts?: ")
    type4 = input ("What's the type of shirt you're buying?: ")

    print ("Shirts cost 36 dollars each.")

    cost = shirts2 * 36

    print ("Thanks for buying " + shirts2, brand4, type4 + " shirts for " + cost + " dollars!")

elif options2 == "Second":

    shoes2 = input ("How many do you want to buy?: ")
    brand5 = input ("What's the brand of the shoes?: ")
    type5 = input("What is the type of shoe you're buying?: ")
   
    print ("A pair of shoes costs 50 dollars each")

    cost2 = shoes2 * 50
   
    print ("Thanks for buying " + shoes2, brand5, type5 + " shoes for " + cost2 + " dollars!")

elif options2 == "Third":

    TVs2 = input ("How many do you want to buy?: ")
    brand6 = input ("What's the brand of the TVs?: ")
    type6 = input ("What's the type of TV you're buying?: ")
    
    print ("A TV costs 500 dollars.")

    cost3 = TVs2 * 500

    print ("Thanks for buying " + TVs2, brand6, type6 + " TVs for " + cost3 + " dollars!")

elif options2 == "X-it":
    print ("Bye!")

   
     
