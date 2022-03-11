import phonenumbers
from phonenumbers import timezone,geocoder,carrier

number = input("Enter your number with +__:  ")

phone = phonenumbers.parse(number)

time = timezone.time_zones_for_number(phone)

car = carrier.name_for_number(phone,"en")

reg = geocoder.description_for_number(phone,"en")
print("Phone number: ",phone)
print("Timezone: ",time)
print("Carrier: ",car)
print("Geocoder location: ",reg)
