def menu():
    print ( "1: Append ")
    print ( "2: Insert")
    print ( "3: Remove")
    print ( "4: Sort")
    print ( "5: Reverse")
    print ( "6: Count")
    print ( "7: Index")
    print ( "8: Exit")
    choose = int(input("Select 1 to 8:"))
    return choose
list1= []
s=input("Enter list elements:")
list1=s.split()
print(list1)
while 1:
    choose=menu()
        if choose == 8 :
            break;
        elif choose == 1:
            x= input("Enter a Element For appended:")
            list1.append(x)
            print("list is :", list1)
        elif choose == 2:
            x= input("Enterf a Element For Insert:")
            list1.insert(x)
            print ("List is :",list1)
            