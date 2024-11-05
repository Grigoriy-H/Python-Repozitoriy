from smartphone import Smartphone

catalog = []
phone1 = Smartphone("Apple", "iPhone 11 Pro", "+79041238527")
phone2 = Smartphone("Apple", "iPhone 15 Pro Max", "+79055869271")
phone3 = Smartphone("Samsung", "Samsung Galaxy A15", "+79831452568")
phone4 = Smartphone("Samsung", "Samsung Galaxy S24 Ultra", "+79067834527")
phone5 = Smartphone("Huawei", "Huawei P30 Lite", "+79633571698")
phone6 = Smartphone("Honor", "Honor Magic V2", "+79171546837")

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)
catalog.append(phone6)

for phone in catalog:
    print(f"{phone.brand} - {phone.model} - {phone.number}") 