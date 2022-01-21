import phonenumbers
from numberFile import number
from phonenumbers import carrier
service_providor=phonenumbers.parse(number,'RO')
print(carrier.name_for_number(service_providor,'en'))
from phonenumbers import geocoder
location=phonenumbers.parse(number,'CH')
print(geocoder.description_for_number(location,'en'))
