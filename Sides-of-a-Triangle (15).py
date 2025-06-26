try:
    s1 = int(input("Side 1: "))
    s2 = int(input("Side 2: "))
    s3 = int(input("Side 3: "))
    if (s1 + s2 > s3) and (s1 + s3 > s2) and (s2 + s3 > s1):
        print('Such a triangle exists.')
    else:
        print('Such a triangle does not exist.')
except:
    print('Enter integer')