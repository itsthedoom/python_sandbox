#cars
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
        
#toppings
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")

#magic_number

answer = 17

if answer !=42:
    print("That is not the correct answer. Please try again!")
    

#banned_users

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(user.title() +", you can post a response if you wish.")


#voting
age = 19
if age >=18:
    print("You are old enough to vote!")
    
#amusement_park
age = 12

if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5")
else:
    print("Your admission cost is $10.")

#amusement_park_2
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10
print("Your admission cost is $" +str(price) + ".")
    






