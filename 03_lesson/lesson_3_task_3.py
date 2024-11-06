from address_page import Address
from mailing_page import Mailing

to_address = Address("404137", "Волжский", "Горького", "1г", "14")
from_addres = Address("404360", "Котельниково", "Цимлянская", "24", "1") 
mailing = Mailing(to_address, from_addres, 350, 123)


print(f"""Отправление {mailing.track} из {mailing.from_address.index},
     {mailing.from_address.city}, {mailing.from_address.street},
     {mailing.from_address.house} - {mailing.from_address.apartment}
     в {mailing.to_address.index},{mailing.to_address.city},
     {mailing.to_address.street}, {mailing.to_address.house}
     {mailing.to_address.apartment}. стоимость {mailing.cost} рублей.""")