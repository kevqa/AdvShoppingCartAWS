from faker import Faker

fake = Faker(locale='en_CA')
adshopcart_url = 'https://advantageonlineshopping.com/#/'
cartpage_url = 'https://advantageonlineshopping.com/#/shoppingCart'

old_username = fake.user_name()
new_username = old_username[0:11]

email = fake.email()
new_password = fake.password()
first_name = fake.first_name()
last_name = fake.last_name()
full_name = f'{first_name} {last_name}'
phone = fake.phone_number()
city = fake.city()

address = fake.street_address()

province = fake.province_abbr()
postalcode = fake.postalcode()

description = fake.sentence(nb_words=25)


