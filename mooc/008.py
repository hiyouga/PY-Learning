#month.py

months = "JanFebMarAprMayJunJulAugSepOctNovDec"

n = input("Please input month(1-12):")
pos = (int(n) - 1) * 3
monthabbr = months[pos:pos+3]
print("The abbr is : "+monthabbr+".")