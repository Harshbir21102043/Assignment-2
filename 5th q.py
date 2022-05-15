s1 = int(input("Enter side of triangle :"))
s2 = int(input("Enter side of triangle :"))
s3 = int(input("Enter side of triangle :"))
while (s1+s2>s3) and (s1+s3>s2) and (s2+s3>s1):
    print("Triangle is valid")
    break
