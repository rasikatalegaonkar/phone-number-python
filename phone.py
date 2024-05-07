import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
number = input("Enter your phone number: ")
phone_number = phonenumbers.parse(number)  
print(geocoder.description_for_number(phone_number, 'en')) 

service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, 'en'))   