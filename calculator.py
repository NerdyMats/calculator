result = 0
operations = ['*', '/', '-', '+']

print("welcome to the calculator")

while True:
    what_to_do = input("do you want to calculate then type 'c' or 'q' to quit, ").lower()
    print()
    if what_to_do == 'q':
        break

    elif what_to_do == 'c':
        input_str = input("first number or 'ans'. ")
        if input_str.lower() == 'ans':
                first_number = result

        else:
            try:
                first_number = float(input_str)
            except ValueError:
                print("that is not a valid option.")
                continue
            if first_number.is_integer():
                first_number = int(first_number)


        operation = input("do you want to do: '*2', '/2', '*', '/', '-', '+': ")
        if operation == '*2':
            result = first_number * first_number

            if first_number.is_integer():
                first_number = int(first_number)
            result_string = str(first_number) + "²"
            if result.is_integer():
                result = int(result)

            print("the answer on", result_string, "=", result)
            continue
        elif operation == '/2':
            result = first_number ** 0.5

            if first_number.is_integer():
                first_number = int(first_number)
            result_string = "√" + str(first_number)
            if result.is_integer():
                result = int(result)

            print("the answer on", result_string, "=", result)
            continue
        else:
            if operation in operations:
                input_str_2 = input("second number or 'ans'. ")
                if input_str_2.lower() == 'ans':
                    second_number = result

                else:
                    try:
                        second_number = float(input_str_2)
                    except ValueError:
                        print("that is not a valid option.")
                        continue
                if second_number.is_integer():
                    second_number = int(second_number)

                if operation == '*':
                    result = first_number * second_number
                elif operation == '/':
                    result = first_number / second_number
                elif operation == '+':
                    result = first_number + second_number
                elif operation == '-':
                    result = first_number - second_number

                print("the answer on:", first_number, operation, second_number, "=", result)

            else:
                print("that is not a valid option")
                continue

    else:
        print("that is not a valid option.")
        continue
