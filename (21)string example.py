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
    if choose == 8:
        break;
    elif choose == 1:
        x= input("Enter a Element For appended:")
        list1.append(x)
        print("list is :", list1)
    elif choose == 2:
        x= input("Enterf a Element For Insert:")
        index = int(input("enter insert index:"))
        if index<len(list1):
            list1.insert(index,x)
            print("list is , list1")
    elif choose == 3:
        x = input("Enter a remove element:")
        if x in list1:
                list1.remove(x)
                print("List is ", list1)
    elif choose == 4:
        list1.sort()
        print("List is ", list1)
    elif choose == 5:
        list1.reverse()
        print("List is ", list1)
    elif choose == 6:
        x = input("Enter a element for count:")
        print("Count is ", list1.count(x))
    elif choose == 7:
        x = input("Enter a element for find index:")
        if x in list1:
            index = list1.index(x)
        else:
            index = 0
            print("Index is ", index)
    else:
            print("Invalid choose")
    print("-")
            