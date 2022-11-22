#!/usr/bin/env python3

# Created by Cristiano Sellitto
# Created in November 2022
# A program that prints out 1000 to 2000 on five lines each


def main():
    # Prints out 1000 to 2000 on five lines each

    dummy_value = input("\nPress Enter to start printing 1000 to 2000:\n")
    for number in range(1000, 2001):
        if number % 10 == 4 or number % 10 == 9:
            print(number)
        else:
            print(number, end=" ")
    print("")
    print("\nDone.")


if __name__ == "__main__":
    main()
