from account import *

def main():
    test_account = Account(156646, "Myles Charlesworth", 0)
    print(f"{test_account.account_num}, {test_account.account_holder}, {test_account.balance}")
    print("-------------testing deposits method ----------------")

    try: #this block tests the ability of the user to deposit a negative balance
        test_account.deposit(-100)
    except Exception as e:
        print(e)
        print(f"{test_account.account_num}, {test_account.account_holder}, {test_account.balance}")


    try:  # This block tests a non-int input
        test_account.deposit("haha")
    except Exception as e:
        print(e)
        print(f"{test_account.account_num}, {test_account.account_holder}, {test_account.balance}")

    try:  # This block is a normal run of the deposit function
        test_account.deposit(100)
    except Exception as e:
        print(e)
        print(f"{test_account.account_num}, {test_account.account_holder}, {test_account.balance}")

    print("-------------testing withdraw method ----------------")

    print(f"{test_account.account_num}, {test_account.account_holder}, {test_account.balance}")


    try: #this block tests a 0 withdrawal
        test_account.withdraw(0)
    except Exception as e:
        print(e)
        print(f"{test_account.account_num}, {test_account.account_holder}, {test_account.balance}")

    try: # this bock tests a negative withdrawal
        test_account.withdraw(-50)
    except Exception as e:
        print(e)
        print(f"{test_account.account_num}, {test_account.account_holder}, {test_account.balance}")

    try:  # This block tests a non-int input
        test_account.deposit("haha")
    except Exception as e:
        print(e)
        print(f"{test_account.account_num}, {test_account.account_holder}, {test_account.balance}")

    try: # This block is a normal withdrawal
        test_account.withdraw(50)
    except Exception as e:
        print(e)
        print(f"{test_account.account_num}, {test_account.account_holder}, {test_account.balance}")

    print(f"{test_account.account_num}, {test_account.account_holder}, {test_account.balance}")

    print("-------------testing getter method ----------------")

    print(f"{test_account.get_balance()} is your current account balance.")



main()
