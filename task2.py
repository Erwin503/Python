arr = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
err = "Invalid"
iscor = True
while True :
    iscor = True
    print ("Enter the number of month")
    month = int(input())
    print ("Enter the number of day")
    day = int(input())
    if (day < 1 or day > 31) and (month < 1 or month > 12):
        print(err)
        iscor = False
    elif month < 8 :
        if month != 2:
            if month%2==0:
                if day > 30: 
                    print(err)
                    iscor = False
                elif day > 31:
                    print(err)
                    iscor = False
        elif day>28 : 
            print(err)
            iscor = False
    elif month%2==1:
        if day > 30: 
            print(err)
            iscor = False
    elif day > 31:
        print(err)
        iscor = False
    if iscor:
        print(arr[month-1]+day)