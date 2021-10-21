#!/usr/bin/env python3

# Created by: Mr. Coxall
# Created on: Dec 2019
# This program uses an array to calculate the mean
#  from randomly generated numbers


import random


def main():
    # this function uses an array to generate 10 random numbers
    #  from 1-100 and output the mean

    mean_numbers = []

    # process & output
    for loop_counter in range(0, 10):
        number_in_array = random.randint(0, 100 + 1)
        mean_numbers.append(number_in_array)

    print("The random number from (1-100) are...")
    print("")
    print("{0}".format(mean_numbers))

    mean_calculation = sum(mean_numbers) / len(mean_numbers)
    rounded_mean = round(mean_calculation, 1)

    print("\nThe mean of the randomly generated numbers is {0}".format(rounded_mean))
    print("\nDone.")


if __name__ == "__main__":
    main()
