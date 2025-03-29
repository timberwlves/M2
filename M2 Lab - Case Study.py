# Grayson Belmonte
# File Name: M2 Lab - Case Study
# brief Description: A Python App that
# takes student names and test if student
# qualifies for deans list/ honor roll.


def main():
    while True:
        lastName = input("Input student's last name here: ")

        if lastName == "ZZZ":
            break

        firstName = input("Input student first name here: ")
        gradeAverage = float(input("Input GPA here: "))

        if gradeAverage >= 3.5:
            print(f"{firstName} has made the Dean's List.")

        elif gradeAverage >= 3.25:
            print(f"{firstName} has made the Honor Roll.")

        else:
            print(f"{firstName} has not made Dean's List or Honor roll.")

if __name__ == "__main__":
    main()


