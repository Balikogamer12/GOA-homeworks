name = input("გთხოვთ, დაწერეთ თქვენი სახელი: ")
age = int(input("გთხოვთ, დაწერეთ თქვენი ასაკი: "))

is_adult = age >= 18
is_name_luka = name.lower() == "ლუკა"

print("სრულწლოვანი:", is_adult)
print("სახელი უდრის 'ლუკა':", is_name_luka)
