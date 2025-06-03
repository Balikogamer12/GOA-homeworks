names = ["გელა", "ლუკა", "ჯუმბერა"]

index = -1  

while index < 0 or index > 2:
    index = int(input("შემოიტანე რიცხვი 0-დან 2-ის ჩათვლით: "))

print("შენ აირჩიე:", names[index])

# -----------------------------------------------------------------------------------

word = "Python"
word[0] = "B"   
print(word)

# სტრიქონები Python-ში არიან უცვლადები (immutable)

# სწორი კოდი:

word = "Python"
word = "B" + word[1:]
print(word)  
