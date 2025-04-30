# Jeremy Edwin Ephraim
# TP076741
def start():
    import os
    if os.path.exists('distribution.txt'):
        login()
    else:
        initial_user()


def initial_user():  # Function use for create initial user details
    import re  # Import regular expression to verify valid email address
    with open("db.txt", "w") as file:  # Create a txt file to store database
        file.write(str(['username', 'password', 'email', 'name', 'gender', 'contact number']))
    # Write header into the file for easy read purpose

    for a in range(4):  # Loop 4 times to create 4 different account
        a += 1
        temp_list = []  # Use to store current creating user's data
        with open("db.txt", "r") as file:  # Open file as read mode for further use
            db = file.read()

        username = input(f"Enter {a} user's username: ")
        while True:
            if username in db:  # Use to check weather username isn't exist
                print(f"{username} exist, please entered again.")
                username = input(f"Enter {a} user's username: ")
            else:
                break
        temp_list.append(username)  # Add current username into the temp_list

        password = input(f"Enter {a} user's password(Minimum 6 digit length): ")
        while True:
            if len(password) < 6:  # Use to check password length
                print("Password entered too short, please enter again.")
                password = input(f"Enter {a} user's password: ")
            else:
                break
        temp_list.append(password)  # Add current password into the temp_list

        email = input(f"Enter {a} user's email (e.g., username@domain.com): ")
        regex = r"^\w+[\w\.-]*@\w+\.\w+$"  # Regular expression for valid email address
        while True:
            if re.match(regex, email):
                break
            else:
                print("Invalid email format. Please enter a valid email (e.g., username@domain.com).")
                email = input(f"Enter {a} user's email (e.g., username@domain.com): ")
        while True:
            if email in db:  # Use to check weather email isn't exist
                print(f"{email} exist, please entered again.")
                email = input(f"Enter {a} user's email(e.g., username@domain.com): ")
            else:
                break
        temp_list.append(email)  # Add current email into the temp_list

        name = input(f"Enter {a} user's name: ")
        temp_list.append(name)  # Add current name into the temp_list

        gender = input(f"Enter {a} user's gender(m= Male. f= Female): ")
        while True:
            if gender.lower() in ["m", "f"]:  # Convert user input into lower case for verification purpose
                break
            else:
                print(f"Input error, please entered again.(m= Male. f= Female)")
                gender = input(f"Enter {a} user's gender(m= Male. f= Female): ")
        temp_list.append(gender.lower())  # Add current gender into the temp_list

        contact_number = input(f"Enter {a} user's contact_number: ")
        while True:
            if contact_number.isdigit():  # Verify weather is digit or other type of variable
                try:
                    contact_number = int(contact_number)
                    break
                except ValueError:
                    print("Invalid contact number. Please enter digits only.")
                    contact_number = input(f"Enter {a} user's contact_number: ")
            else:
                print("Invalid contact number. Please enter digits only.")
                contact_number = input(f"Enter {a} user's contact_number: ")
        temp_list.append(str(contact_number))  # Add current contact_number into the temp_list

        temp_list.append("false")

        temp_list = str(temp_list)  # Convert list into string to store into txt file
        file = open("db.txt", "a")  # Open database's txt file as append mode to store data
        file.write("\n")
        file.write(temp_list)  # Add current user details into txt file
    file.close()
    initial_suppliers()


def initial_suppliers():
    with open("suppliers.txt", "w") as file:  # Create a txt file to store database
        file.write(str(['suppliers code', 'suppliers name', 'suppliers address', 'suppliers contact']))
    number_suppliers = int(input("Enter number of suppliers (Min= 3, Max= 4): "))
    while True:
        if number_suppliers == 3 or number_suppliers == 4:
            break
        else:
            print("Invalid number of suppliers. Please enter 3 or 4 only.")
            number_suppliers = int(input("Enter number of suppliers (Min= 3, Max= 4): "))
    if number_suppliers == 3 or number_suppliers == 4:
        for c in range(number_suppliers):
            c += 1
            temp_list = []
            file = open("suppliers.txt", "r")  # Open file as read mode for further use
            db = file.read()
            file.close()

            code = input(f"Enter {c} supplier's suppliers code: ")
            while True:
                if code in db:
                    print(f"{code} exist, please entered again.")
                    code = input(f"Enter {c} supplier's suppliers code: ")
                else:
                    break
            temp_list.append(code)

            name = input(f"Enter {c} supplier's's name: ")
            temp_list.append(name)  # Add current name into the temp_list

            address = input(f"Enter {c} supplier's's address: ")
            temp_list.append(address)  # Add current name into the temp_list

            contact_number = input(f"Enter {c} supplier's contact number: ")
            while True:
                if contact_number.isdigit():  # Verify weather is digit or other type of variable
                    try:
                        contact_number = int(contact_number)
                        break
                    except ValueError:
                        print("Invalid contact number. Please enter digits only.")
                        contact_number = input(f"Enter {c} supplier's contact number: ")
                else:
                    print("Invalid contact number. Please enter digits only.")
                    contact_number = str(input(f"Enter {c} supplier's contact number: "))
            temp_list.append(contact_number)  # Add current contact_number into the temp_list

            temp_list = str(temp_list)  # Convert list into string to store into txt file
            file = open("suppliers.txt", "a")  # Open database's txt file as append mode to store data
            file.write("\n")
            file.write(temp_list)
    file.close()
    initial_hospital()


def initial_hospital():
    file = open("hospital.txt", "w")  # Create a txt file to store database
    file.write(str(['hospital code', 'hospital name', 'hospital address', 'hospital contact']))
    number_hospital = int(input("Enter number of hospital (Min= 3, Max= 4): "))
    while True:
        if number_hospital == 3 or number_hospital == 4:
            break
        else:
            print("Invalid number of hospital. Please enter 3 or 4 only.")
            number_hospital = int(input("Enter number of hospital (Min= 3, Max= 4): "))
    if number_hospital == 3 or number_hospital == 4:
        for d in range(number_hospital):
            d += 1
            temp_list = []
            with open("hospital.txt", "r") as file:  # Open file as read mode for further use
                db = file.read()

            code = input(f"Enter {d} hospital's hospital code: ")
            while True:
                if code in db:
                    print(f"{code} exist, please entered again.")
                    code = input(f"Enter {d} hospital's hospital code: ")
                else:
                    break
            temp_list.append(code)

            name = input(f"Enter {d} hospital's's name: ")
            temp_list.append(name)  # Add current name into the temp_list

            address = input(f"Enter {d} hospital's's address: ")
            temp_list.append(address)  # Add current name into the temp_list

            contact_number = input(f"Enter {d} hospital's contact number: ")
            while True:
                if contact_number.isdigit():  # Verify weather is digit or other type of variable
                    try:
                        contact_number = int(contact_number)
                        break
                    except ValueError:
                        print("Invalid contact number. Please enter digits only.")
                        contact_number = input(f"Enter {d} hospital's contact number: ")
                else:
                    print("Invalid contact number. Please enter digits only.")
                    contact_number = input(f"Enter {d} hospital's contact number: ")
            temp_list.append(str(contact_number))  # Add current contact_number into the temp_list

            temp_list = str(temp_list)  # Convert list into string to store into txt file
            file = open("hospital.txt", "a")  # Open database's txt file as append mode to store data
            file.write("\n")
            file.write(temp_list)
    file.close()
    initial_inventory()


# William Teh Kang Wye
# TP070325
def initial_inventory():
    file = open("ppe.txt", "w")  # Create a txt file to store database
    file.writelines(["['item code', 'item name', 'quantity_left', 'supplier_code']\n",
                     "['HC', 'Head Cover', 100, 'S1']\n", "['FS', 'Face Shield', 100]\n", "['MS', 'Mask', 100]\n",
                     "['GL', 'Gloves', 100]\n", "['GW', 'Gown', 100]\n", "['SC', 'Shoe Covers', 100]"])

    with open("suppliers.txt", "r") as file:  # Open file as read mode for further use
        file = file.readlines()  # Convert current database into list
        suppliers = []
        for temp_suppliers in file:  # Convert current list into valid nested list
            temp_suppliers = temp_suppliers.rstrip('\n')
            temp_suppliers = eval(temp_suppliers)
            suppliers.append(temp_suppliers)

    with open("ppe.txt", "r") as file:  # Open file as read mode for further use
        file = file.readlines()  # Convert current database into list
        ppe = []
        for temp_ppe in file:  # Convert current list into valid nested list
            temp_ppe = temp_ppe.rstrip('\n')
            temp_ppe = eval(temp_ppe)
            ppe.append(temp_ppe)

    inventory_menu = []
    suppliers_menu = []
    all_item_code = []
    all_supplier_code = []

    for b in range(len(ppe)):
        inventory_menu.append(ppe[b][0])
        inventory_menu.append(ppe[b][1])
        all_item_code.append(ppe[b][0])
    all_item_code.pop(0)

    for c in range(len(suppliers)):
        suppliers_menu.append(suppliers[c][0])
        suppliers_menu.append(suppliers[c][1])
        all_supplier_code.append(suppliers[c][0])

    all_supplier_code.pop(0)

    for d in range(len(inventory_menu)):
        if d % 2 == 0:
            print(inventory_menu[d], end="\t")
        else:
            print(inventory_menu[d])

    for d in range(len(suppliers_menu)):
        if d % 2 == 0:
            print(suppliers_menu[d], end="\t")
        else:
            print(suppliers_menu[d])

    for f in range(len(all_item_code)):
        supplier_code = input(f"Enter supplier code for item code {all_item_code[f]}: ")
        while True:
            if supplier_code in all_supplier_code:
                # Find the index of the item in the ppe list
                for i, item in enumerate(file):
                    if item[0] == all_item_code[f]:
                        # Insert supplier code at the correct position
                        item.insert(3, supplier_code)
                        # Update the line in the file content
                        file[i] = str(item).replace("']", "']\n")
                break
            else:
                print("Invalid supplier code. Please enter a valid supplier code.")
                supplier_code = input(f"Enter supplier code for item code {all_item_code[f]}: ")

    # Write the updated content back to ppe.txt
    with open('ppe.txt', 'w') as new_file:
        new_file.writelines(file)
    initial_distribution()


def initial_distribution():
    file = open("distribution.txt", "w")  # Create a txt file to store database
    file.write(str(['item code', 'hospital code', 'quantity', 'date']))
    file.close()
    login()


def login():
    with open("db.txt", "r"):  # Open file as read mode for further use
        file = open("db.txt", "r")
        file = file.readlines()  # Convert current database into list
        db = []
        for temp_db in file:  # Convert current list into valid nested list
            temp_db = temp_db.rstrip('\n')
            temp_db = eval(temp_db)
            db.append(temp_db)
    user_found = False
    login_attempt = 3
    print("PPE Inventory Management System\n"
          "Please login your account.")
    username = input("Please enter your username: ")
    while True:
        for db_index, db_element in enumerate(db):  # Use to check weather username isn't in the database
            try:
                username_index = db_element.index(username)
                user_found = True
                break
            except ValueError:
                continue
        if user_found:
            break
        else:
            login_attempt -= 1
            if login_attempt != 0:
                print(f"{username} not exist, please entered again.\n"
                      f"Login attempt left: {login_attempt} ")
                username = input("Please enter your username: ")
            else:
                print(f"{login_attempt} login attempt left, terminating system.")
                exit()
    if user_found:
        password_index = username_index + 1
        user_password = db[db_index][password_index]
        login_attempt = 3
        password = input("Please enter your password: ")
        while True:
            if len(password) < 6:  # Use to check password length
                print("Password entered too short, please enter again.")
                password = input(f"Enter {username}'s password: ")
            else:  # if current password match password store in database, it will allow access to system
                if str(password) == str(user_password):
                    main_menu()
                    break

                else:
                    login_attempt -= 1
                    if login_attempt > 0:
                        print(f"Password entered incorrect, please enter again.\n"
                              f"Login attempt left: {login_attempt} ")
                        password = input(f"Enter {username}'s password: ")
                    else:
                        print(f"{login_attempt} login attempt left, terminating system.")
                        exit()


# Tan Li Xuan
# TP 074847
def main_menu():
    print("PPE Inventory Management System\n"
          "1. Track Inventory\n"
          "2. Update Inventory\n"
          "3. Search Inventory\n"
          "4. Generate Report\n"
          "5. Exit")
    selection = input("Enter your choice (1-5): ")
    while True:
        if selection == '1':
            track_inventory()
            break

        elif selection == '2':
            inventory_update()
            break

        elif selection == '3':
            search_inventory()
            break

        elif selection == '4':
            inventory_report()
            break

        elif selection == '5':
            print("Exiting program.")
            exit()
        else:
            print("Invalid input, please enter again.\n"
                  "PPE Inventory Management System\n"
                  "1. Track Inventory\n"
                  "2. Update Inventory\n"
                  "3. Search Inventory\n"
                  "4. Generate Report\n"
                  "5. Exit")
            selection = input("Enter your choice (1-5): ")


def track_inventory():
    with open("ppe.txt", "r") as file:  # Open file as read mode for further use
        file = file.readlines()  # Convert current database into list
        ppe = []
        for temp_ppe in file:  # Convert current list into valid nested list
            temp_ppe = temp_ppe.rstrip('\n')
            temp_ppe = eval(temp_ppe)
            ppe.append(temp_ppe)
    inventory_menu = []
    temp_inventory_menu = [[item for item in sublist[:-1]] for sublist in ppe]

    for a in range(len(temp_inventory_menu) - 1):
        for b in range(a + 1, len(temp_inventory_menu)):
            if temp_inventory_menu[a][0] > temp_inventory_menu[b][0]:
                temp_inventory_menu[a], temp_inventory_menu[b] = temp_inventory_menu[b], temp_inventory_menu[a]

    for c in range(len(temp_inventory_menu)):
        inventory_menu.append(temp_inventory_menu[c][0])
        inventory_menu.append(temp_inventory_menu[c][1])
        inventory_menu.append(temp_inventory_menu[c][2])
    inventory_menu[0:0] = inventory_menu[-3:]
    inventory_menu = inventory_menu[:-3]

    print("Item Inventory Tracking\n"
          "1. Total available quantity of all items sorted in ascending order by item code\n"
          "2. Records of all items that has stock quantity less than 25 boxes\n"
          "3. Back to main menu")
    selection = input("Enter your choice (1-3): ")
    while True:
        if selection == '1':
            for e in range(len(inventory_menu)):
                if (e + 1) % 3 == 0:
                    print(inventory_menu[e])
                else:
                    print(inventory_menu[e], end="\t")
            print()
            print("2. Records of all items that has stock quantity less than 25 boxes\n"
                  "3. Back to main menu")
            selection = input("Enter your choice (2-3): ")

        elif selection == '2':
            for f in range(len(inventory_menu[:3])):
                print(inventory_menu[f], end="\t")
            print()
            for g in range(3, len(inventory_menu), 3):
                item_code = inventory_menu[g]
                item_name = inventory_menu[g + 1]
                quantity_left = inventory_menu[g + 2]
                if quantity_left < 25:
                    print(f"{item_code}\t{item_name}\t{quantity_left}")

            print()
            print("1. Total available quantity of all items sorted in ascending order by item code\n"
                  "3. Back to main menu")
            selection = input("Enter your choice (1/3): ")

        elif selection == '3':
            main_menu()
            break

        else:
            print("Invalid input, please enter again.")
            selection = input("Enter your choice : ")


def search_inventory():
    with open("distribution.txt", "r") as file:  # Open file as read mode for further use
        file = file.readlines()  # Convert current database into list
        distribution = []
        for temp_distribution in file:  # Convert current list into valid nested list
            temp_distribution = temp_distribution.rstrip('\n')
            temp_distribution = eval(temp_distribution)
            distribution.append(temp_distribution)

    with open("ppe.txt", "r") as file:  # Open file as read mode for further use
        file = file.readlines()  # Convert current database into list
        ppe = []
        for temp_ppe in file:  # Convert current list into valid nested list
            temp_ppe = temp_ppe.rstrip('\n')
            temp_ppe = eval(temp_ppe)
            ppe.append(temp_ppe)
    inventory_menu = []
    all_item_code = []

    for c in range(len(ppe)):
        inventory_menu.append(ppe[c][0])
        inventory_menu.append(ppe[c][1])
        all_item_code.append(ppe[c][0])
    all_item_code.pop(0)

    print("Item Inventory Search")
    for e in range(len(inventory_menu)):
        if (e + 1) % 2 == 0:
            print(inventory_menu[e])
        else:
            print(inventory_menu[e], end="\t")

    print("BACK\t Back to main menu")
    search_code = input("Enter item code or enter BACK:")
    search_code = search_code.upper()
    while True:
        if search_code in all_item_code:
            temp_search = {}
            for f in distribution[1:]:
                item_code, hospital_code, quantity = f[0].strip(), f[1].strip(), int(f[2])
                if item_code == search_code:
                    temp_search[hospital_code] = temp_search.get(hospital_code, 0) + quantity
            search = dict(sorted(temp_search.items()))

            for g in ppe[1:]:
                item_code, item_name = g[0].strip(), g[1].strip()
                if item_code == search_code:
                    print(item_name)
            print("Hospital code\t Quantity distributed")
            for hospital_code, total_quantity in search.items():
                print(hospital_code, end="\t")
                print(total_quantity, end="\n")

            search_code = input("Enter item code or enter BACK:")
            search_code = search_code.upper()

        elif search_code == 'BACK':
            main_menu()
        else:
            print('Invalid input. Please enter valid item code or back only.')
            search_code = input("Enter item code or enter BACK:")
            search_code = search_code.upper()


def inventory_update():
    import datetime as dt
    date = dt.datetime.now()

    # Read PPE data
    with open("ppe.txt", "r") as file:
        file = file.readlines()
        ppe = []
        for temp_ppe in file:
            temp_ppe = temp_ppe.rstrip('\n')
            temp_ppe = eval(temp_ppe)
            ppe.append(temp_ppe)

    # Read hospital data
    with open("hospital.txt", "r") as file:
        file = file.readlines()
        hospital = []
        for temp_hospital in file:
            temp_hospital = temp_hospital.rstrip('\n')
            temp_hospital = eval(temp_hospital)
            hospital.append(temp_hospital)

    inventory_menu = []
    all_item_code = []
    all_hospital_code = []

    for a in range(len(hospital)):
        all_hospital_code.append(hospital[a][0])
    all_hospital_code.pop(0)

    for c in range(len(ppe)):
        inventory_menu.append(ppe[c][0])
        inventory_menu.append(ppe[c][1])
        inventory_menu.append(ppe[c][2])
        inventory_menu.append(ppe[c][3])
        all_item_code.append(ppe[c][0])
    all_item_code.pop(0)
    all_item_code.append('BACK')

    print("Item Inventory Update")
    for e in range(len(inventory_menu)):
        if (e + 1) % 4 == 0:
            print(inventory_menu[e])
        else:
            print(inventory_menu[e], end="\t")

    print("BACK\t Back to main menu")
    search_code = input("Enter item code you would like to update or enter BACK:").upper()

    while True:
        if search_code in all_item_code:
            if search_code == 'BACK':
                main_menu()
            else:
                print("1. Receiving from suppliers\n"
                      "2. Distributing to the hospitals\n"
                      "3. Back to main menu")
                selection = input("Enter your choice (1-3): ")

                if selection == '1':
                    quantity_received = int(input("Enter quantity received: "))
                    while quantity_received <= 0:
                        print('Invalid quantity, please enter again')
                        quantity_received = int(input("Enter quantity received: "))

                    for f in range(1, len(ppe)):
                        if ppe[f][0] == search_code:
                            ppe[f][2] += quantity_received
                            new_data = [str(sublist) + "\n" for sublist in ppe]
                            break

                    with open('ppe.txt', "w") as new_file:
                        new_file.writelines(new_data)

                    log = [search_code, 'SUPPLIER', str(quantity_received), date.strftime("%x")]
                    with open('distribution.txt', "a") as new_file:
                        new_file.writelines(str(log))
                        new_file.write("\n")

                    print('Item inventory quantity Updated.\n'
                          '1. Continue update another item\n'
                          '2. Back to main menu')
                    selection = input("Enter your choice (1-2): ")
                    if selection == '1':
                        inventory_update()
                    elif selection == '2':
                        main_menu()

                elif selection == '2':
                    hospital_code = input("Enter hospital code: ").upper()
                    while hospital_code not in all_hospital_code:
                        print('Invalid hospital code, please enter again.')
                        hospital_code = input("Enter hospital code: ").upper()

                    quantity_distribute = int(input("Enter quantity distribute: "))
                    while quantity_distribute <= 0:
                        print('Invalid quantity, please enter again')
                        quantity_distribute = int(input("Enter quantity distribute: "))

                    for f in range(1, len(ppe)):
                        if ppe[f][0] == search_code:
                            while quantity_distribute > int(ppe[f][2]):
                                print(f"Quantity left not enough. {ppe[f][1]} left : {ppe[f][2]}")
                                quantity_distribute = int(input("Enter quantity distribute: "))

                            ppe[f][2] -= quantity_distribute
                            new_data = [str(sublist) + "\n" for sublist in ppe]
                            break

                    with open('ppe.txt', "w") as new_file:
                        new_file.writelines(new_data)

                    log = [search_code, hospital_code, str(quantity_distribute), date.strftime("%x")]
                    with open('distribution.txt', "a") as new_file:
                        new_file.writelines(str(log))
                        new_file.write("\n")

                    print('Item inventory quantity Updated.\n'
                          '1. Continue update another item\n'
                          '2. Back to main menu')
                    selection = input("Enter your choice (1-2): ")
                    if selection == '1':
                        inventory_update()
                    elif selection == '2':
                        main_menu()

                elif selection == '3':
                    main_menu()

                elif selection == 'BACK':
                    main_menu()
        else:
            print('Invalid input. Please enter valid item code or back only.')
            search_code = input("Enter item code or enter BACK:").upper()


def inventory_report():
    with open("ppe.txt", "r") as file:  # Open file as read mode for further use
        file = file.readlines()  # Convert current database into list
        ppe = []
        for temp_ppe in file:  # Convert current list into valid nested list
            temp_ppe = temp_ppe.rstrip('\n')
            temp_ppe = eval(temp_ppe)
            ppe.append(temp_ppe)

    with open("distribution.txt", "r") as file:  # Open file as read mode for further use
        file = file.readlines()  # Convert current database into list
        distribution = []
        for temp_distribution in file:  # Convert current list into valid nested list
            temp_distribution = temp_distribution.rstrip('\n')
            temp_distribution = eval(temp_distribution)
            distribution.append(temp_distribution)

    print("PPE Inventory Management System\n"
          "1. List of suppliers with their PPE equipments supplied\n"
          "2. List of hospitals with quantity of distribution items\n"
          "3. Overall transaction report for a selected month\n"
          "4. Main menu")
    selection = input("Enter your choice (1-4): ")
    while True:
        if selection == '1':
            search_result = []
            supplier_search = input("Enter supplier code: ")

            for item_code, item_name, _, supplier_code in ppe[1:]:  # Skip header, ignore name and quantity
                if supplier_code == supplier_search:
                    search_result.append(item_code)
                    search_result.append(item_name)

            print(f"List of PPE Equipments Supplied")
            for a in range(len(search_result)):
                if (a + 1) % 2 == 0:
                    print(search_result[a])
                else:
                    print(search_result[a], end="\t")
            print()
            inventory_report()
            break

        elif selection == '2':
            hospital_search = input("Enter hospital code: ")
            search_result = [item for item in distribution if item[1] == hospital_search]
            print(f"List of PPE Equipments Distributed")
            for item in search_result:
                print(f"  - Item Code: {item[0]}, Quantity: {item[2]}, Date: {item[3]}")
            print()
            inventory_report()
            break
        elif selection == '3':
            month_search = input("Enter month (e.g., 6 for June): ")
            while not month_search.isdigit() or not 1 <= int(month_search) <= 12:
                print("Invalid month. Please enter a number between 1 and 12.")
                month_search = input("Enter month (e.g., 6 for June): ")
            month_search = int(month_search)

            search_result = [row for row in distribution[1:] if int(row[3].split('/')[0]) == month_search]

            # Overall transaction report (assuming 'quantity' represents the total transaction amount)
            total_transactions = len(search_result)
            total_quantity = sum(int(row[2]) for row in search_result)  # Sum quantities (assuming they represent transaction amounts)

            print("Overall Transaction Report for Month:", month_search)
            print(f"Total Transactions: {total_transactions}")
            print(f"Total Quantity (Units): {total_quantity}")
            if search_result:
                print("\nDetailed Transaction List:")
                print("{:<15} {:<15} {:<15}".format("Item Code", "Hospital Code", "Quantity"))  # Formatted table header
                for row in search_result:
                    print("{:<15} {:<15} {:<15}".format(row[0], row[1], row[2]))  # Formatted table data
            print()
            inventory_report()
            break

        elif selection == '4':
            main_menu()
            break
        else:
            print("Invalid input.Please enter again.\n"
                  "PPE Inventory Management System\n"
                  "1. List of suppliers with their PPE equipments supplied\n"
                  "2. List of hospitals with quantity of distribution items\n"
                  "3. Overall transaction report for a selected month\n"
                  "4. Main menu")
            selection = input("Enter your choice (1-4): ")


start()
