import excelfunc


def action_list():
    while True:
        command = int(input("Choose command:\n 1.Create user \n 2.Edit user \n 3.Reset user \n 4.list of users \n 5.Delete user \n 6.Return"))
        print(command)
        if command == 1:
            user_id = input("Enter user id:")
            user_pass = input("Enter user password:")
            user_name = input("Enter user name:")
            user_last = input("Enter user last name:")
            user_email = input("Enter user email:")
            user_phone = input("Enter user phone:")
            user_type = input("Enter user type:")
            excelfunc.addUser(user_id, user_pass, user_name, user_last, user_email, user_phone, user_type)

        if command == 2:
            excelfunc.Print_User_list()
            id_num = int(input("Enter id number to edit:"))
            edit_choice = input("type which choice edit:\n Username\n Password\n Name\n Lastname\n email\n phone\n "
                                "type ")
            edit = input("Enter the edit:")
            excelfunc.editUser(id_num, edit, edit_choice)
        if command == 3:
            id_num = int(input("Enter id number to Reset"))
            excelfunc.resetUser(id_num)
        if command == 4:
            excelfunc.listOfUsers()
        if command == 5:
            id_num = int(input("Enter id number to delete"))
            excelfunc.deleteUser(id_num)
        if command == 6:
            return
