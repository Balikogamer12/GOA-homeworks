# ლოგიკური ოპერატორები გამოიყენება პირობების შესადარებლად და მათი შედეგი არის True ან False. Python-ში სამი ლოგიკური ოპერატორი არსებობს:

# and - აბრუნებს True-ს, თუ ორივე პირობა სიმართლეა.

# or - აბრუნებს True-ს, თუ მინიმუმ ერთი პირობა სიმართლეა.

# not - აბრუნებს პირობის საწინააღმდეგო მნიშვნელობას (True → False, False → True).

# 1) and ოპერატორის მაგალითები:
print(True and True)   # True, რადგან ორივე პირობაა True  
print(True and False)  # False, რადგან ერთი მაინც არის False  
print(5 > 3 and 10 > 2)  # True, რადგან ორივე პირობა სწორია  
print(5 > 10 and 2 < 1)  # False, რადგან ორივე პირობა მცდარია  

# 2) or ოპერატორის მაგალითები
print(True or False)   # True, რადგან ერთი მაინც არის True  
print(False or False)  # False, რადგან ორივე პირობაა False  
print(5 > 10 or 2 < 5)  # True, რადგან მეორე პირობა სწორია  
print(10 == 10 or 3 > 100)  # True, რადგან პირველი პირობაა True  

# 3) not ოპერატორის მაგალითები
print(not True)   # False, რადგან not აბრუნებს საპირისპიროს  
print(not False)  # True, რადგან not აბრუნებს საპირისპიროს  
print(not (5 > 3))  # False, რადგან 5 > 3 არის True, ხოლო not აკეთებს False-ს  
print(not (10 < 2))  # True, რადგან 10 < 2 არის False, ხოლო not აკეთებს True-ს  
