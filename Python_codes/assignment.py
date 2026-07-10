while True:

    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        name = input("Name: ")
        age = input("Age: ")
        marks = input("Marks: ")

        with open("students.txt", "a") as file:
            file.write(f"{name},{age},{marks}\n")

        print("Student Added")

    elif choice == "2":

        try:

            with open("students.txt", "r") as file:

                print("\nStudent Records\n")

                for line in file:
                    print(line.strip())

        except FileNotFoundError:
            print("Database Empty")

    elif choice == "3":
        break

    else:
        print("Invalid Choice")