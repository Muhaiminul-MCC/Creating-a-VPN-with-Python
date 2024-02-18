year = int(input("Enter your year: "))
if year%4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not leaper")
    else:
        print("LEAP YEAR")        

else:
    print("Not lipear year")