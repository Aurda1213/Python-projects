# Odd or Even

print("Are we in an odd or even year?")

year = int(input("What year are we in?\n"))

odd_even = year % 2

if odd_even == 0:
    print(f"{year} is an even year.")
else:
    print(f"{year} is an odd year.")