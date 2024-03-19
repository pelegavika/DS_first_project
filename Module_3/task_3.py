# "    +38(050)123-32-34"
# "     0503451234"
# "(050)8889900"
# "38050-111-22-22"
# "38050 111 22 11   "

import re

def correct_phone_number (number):
    cleaned_number = re.sub(r'[^0-9+]', '', number)
    if not cleaned_number.startswith('+'):
        if cleaned_number.startswith('380'):
            cleaned_number = "+" + cleaned_number
        else:
            cleaned_number = "+38" + cleaned_number
    return cleaned_number


phone_number_1=correct_phone_number ("    +38(050)123-32-34")
print("1. Коректний номер телефону такий:", phone_number_1)

phone_number_2=correct_phone_number ("     0503451234")
print("2. Коректний номер телефону такий:", phone_number_2)

phone_number_3=correct_phone_number ("(050)8889900")
print("3. Коректний номер телефону такий:", phone_number_3)

phone_number_4=correct_phone_number ("38050-111-22-22")
print("4. Коректний номер телефону такий:", phone_number_4)

phone_number_5=correct_phone_number ("38050 111 22 11   ")
print("5. Коректний номер телефону такий:", phone_number_5)