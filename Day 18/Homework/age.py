name = input("გთხოვთ, დაწერეთ თქვენი სახელი: ")
age = int(input("გთხოვთ, დაწერეთ თქვენი ასაკი: "))

# შემოწმება, არის თუ არა სრულწლოვანი და უდრის თუ არა სახელი "ლუკა"
is_adult = age >= 18
is_name_luka = name.lower() == "ლუკა"

# შედეგების დაბეჭდვა
print("სრულწლოვანი:", is_adult)
print("სახელი უდრის 'ლუკა':", is_name_luka)
