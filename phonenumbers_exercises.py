import phonenumbers

# Sprawdzenie poprawności numeru telefonu
def is_valid_phone_number(phone_str):
    try:
        phone_number = phonenumbers.parse(phone_str, "PL")
        return phonenumbers.is_valid_number(phone_number)
    except phonenumbers.phonenumberutil.NumberParseException:
        return False

print(is_valid_phone_number("452985418"))
print(is_valid_phone_number("452478"))

# Formatowanie numeru telefonu do formatu E.164 - międzynarodowy
def format_to_e164(phone_str):
    try:
        phone_number = phonenumbers.parse(phone_str, None)
        return phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.E164)
    except phonenumbers.phonenumberutil.NumberParseException:
        return None

    # Przykłady użycia:


print(format_to_e164("+45 650-323-0000"))
print(format_to_e164("12345"))
