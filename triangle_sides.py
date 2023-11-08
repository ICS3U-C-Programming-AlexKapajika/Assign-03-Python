#!/usr/bin/env python3
# Created by: Alex Kapajika
# Created on: Nov 05, 2023
# This program shows what type of triangle is , depending to the value of each sides on it.


def main():
    # Getting the variable options to decide which program to run
    options = input(
        "Would you like:\n[1] equilateral, isosceles or scalene\n[2] Area & Perimeter\n[3] Both\n"
    )
    # Getting the variable for the sides of a triangle
    user_sideA_str = input("What is the length of sideA: ")
    user_sideB_str = input("What is the length of sideB: ")
    user_sideC_str = input("What is the length of sideC: ")

    # Creating a function to run only the type of a triangle
    def side_type():
        if user_sideA_float == user_sideB_float == user_sideC_float:
            print("This form a equilateral triangle")
        elif (
            user_sideA_float == user_sideB_float != user_sideC_float
            or user_sideC_float == user_sideA_float != user_sideB_float
            or user_sideB_float == user_sideC_float != user_sideA_float
        ):
            print("This form an isosceles triangle")
        elif user_sideA_float != user_sideB_float != user_sideC_float:
            print("This form a scalene triangle")

    # Creating a function to run only the area and perimeter of a triangle
    def area_peri():
        sides = (user_sideA_float + user_sideB_float + user_sideC_float) / 2
        print("The perimeter equal {}".format(round(sides, 2)))
        area = (
            sides
            * (sides - user_sideA_float)
            * (sides - user_sideB_float)
            * (sides - user_sideC_float)
        ) ** 0.5
        print("The area equal {}".format(round(area, 2)))

    # Trying to Catch anything that is not a float
    try:
        options = int(options)
        user_sideA_float = float(user_sideA_str)
        user_sideB_float = float(user_sideB_str)
        user_sideC_float = float(user_sideC_str)
    except ValueError:
        print("This is not a side of a triangle")
    # Giving to the variable "options" a value.
    else:
        if options == 1:
            side_type()
        elif options == 2:
            area_peri()
        elif options == 3:
            side_type()
            area_peri()
        else:
            print("Please choose a valid option.")


if __name__ == "__main__":
    main()
