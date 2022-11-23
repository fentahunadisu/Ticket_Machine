print("********** will come to drug store ********")
cosmetics = 0
medicine = 0
perfume = 0
def drug_stor():
    if order == "cosmetics":
        global cosmetics
        cosmetics += 1
        print(f"c - {cosmetics}")
    if order == "medicine":
        global medicine
        medicine += 1
        print(f"p - {medicine}")
    if order == "perfume":
        global perfume
        perfume += 1
        print(f"m - {perfume}")
def massage(msg):
    return msg
massage1 = massage("your number is")
massage2 = massage("please wait and someone will assist you shortly")
list = """"
       1 cosmetics
       2 medicine
       3 perfume"""
id_list = [1234,4321]
count = 0
count_limit = 3

while count_limit > count:
    id = int(input("please enter your id"))
    if id in id_list:
        print(list)
        order = input("please choose your product area from drug store")
        while order != "":
            print(massage1)
            drug_stor()
            print(massage2)
            permission = input("do you want continue y/n")
            if permission == "y":
                order = input("please choose your product area: ")
            else:
                print("try again please")
            break
        else:
            order = input("please choose your product area from drug the list")
    else:
        print("please try again")
    count += 1
else:

    import time



    def countdown(t):

        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1

        print('Fire in the hole!!')

    t = input("Enter the time in seconds: ")

    countdown(int(t))