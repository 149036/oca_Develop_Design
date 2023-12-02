gmail_list = [
    ["ex1@gmail.com", "pass"],
    ["ex2@gmail.com", "pass"],
    ["ex3@gmail.com", "pass"],
    ["ex4@gmail.com", "pass"],
]
"""
ex1@gmail.com pass
ex2@gmail.com pass
ex3@gmail.com pass
ex4@gmail.com pass
"""

num = int(input("アカウント数を入力:"))

account_list = []
state_list = []
for i in range(num):
    state_list.append(False)
    account_list.append(input("gmailとpasswordを入力:").split())
    """
	ex@gmail.com password
	"""


while 1:
    print(f"storage   : 1")
    print(f"login     : 2")
    print(f"bulklogin : 3")
    # print(f"state_list = {state_list}")
    a = input(">")

    if a == "1":
        print("storage")

    if a == "2":
        print("select login account")

        for i, x in enumerate(account_list):
            print(f"{x[0]} : {i + 1}")

        n = int(input(">"))

        if account_list[n - 1] == gmail_list[n - 1]:
            state_list[n - 1] = True

            for i in range(len(account_list)):
                print(f"{state_list[i]} : {account_list[i][0]}")

            print(f"account {account_list[n - 1][0]} login succsess")
        else:
            print("failed")

    if a == "3":
        if account_list == gmail_list:
            for i in range(len(account_list)):
                state_list[i] = True

            for i in range(len(account_list)):
                print(f"{state_list[i]} : {account_list[i][0]}")

            print("bulklogin succsess")

            break
        else:
            print("failed")
