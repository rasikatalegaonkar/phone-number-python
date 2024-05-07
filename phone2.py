import phonenumbers as pn
from phonenumbers import geocoder as gc
from phonenumbers import carrier as cr
from phonenumbers import timezone as tz  
number = input("Enter your phone number with country code: ")
phone_number = pn.parse(number)
region = gc.description_for_number(phone_number, 'en')  
print("The region of the given phone number is: ", region)  

carrier = cr.name_for_number(phone_number, 'en')  
print("The SIM Card operator or carrier of the given phone number is: ", carrier)

timezone = tz.time_zones_for_number(phone_number)  
print("The timezone of the given phone number is: ", timezone)  






