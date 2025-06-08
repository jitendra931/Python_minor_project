import time

class LowBalanceException(Exception):
    pass

class AttemptException(Exception):
    pass

attempt = 1  # global 

def withdraw():
    global attempt
    pinsaved = 123
    balance = 50000
    pin = int(input("enter pin: "))

    if pin == pinsaved:
        try:
            amt = int(input("enter amount: "))
            temp = balance - amt  # 50-10 =40
            if temp < 1000:  # 40<1000
                raise LowBalanceException("low balance")
            balance = balance - amt  # 50-40
            print("remaining balance is", balance)
        except Exception as var:
            print(var)  # msg
            print(var._class_)

    else:
        r = input("do you want to continue y/n: ")
        if r.lower() == 'y':
            attempt += 1  # attempt = attempt + 1
            try:
                if attempt == 4:
                    raise AttemptException("reached maximum attempt limit")
            except Exception as obj:
                print(obj)
                print("try again")
                time.sleep(3)
            else:
                withdraw()
        else:
            print("thank you")
            return 

# main
withdraw()
