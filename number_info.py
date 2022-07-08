import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder


inp = input('Enter You Phone Number : ')

phone_numner = phonenumbers.parse(inp)

print(geocoder.description_for_number (phone_numner, "en"))

print(carrier.name_for_number (phone_numner, 'en'))