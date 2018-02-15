while True:
    print("enter '1'for exit ")
    c=input("enter character: ")
    if c=='1':
        break
    else:
        if((c>='a' and c<='z') or (c>='A' and c<='Z')):
            print(c,"alphabet")
        else:
            print(c,"not an alphabet")
