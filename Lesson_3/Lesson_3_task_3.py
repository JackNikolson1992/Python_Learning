from address import Address
from mailing import Mailing

to_addr = Address("101000", "Москва", "Тверская", "10", "25")
from_addr = Address("190000", "Санкт-Петербург", "Невский пр.", "15", "7")

mailing = Mailing(to_addr, from_addr, 350.50, "RU123456789CN")
print(mailing)
