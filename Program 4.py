# Python program to sort elements using match-case (switch-case style)

nums = [9, 2, 7, 1, 5]

print("Choose sorting order:")
print("1. Ascending (min → max)")
print("2. Descending (max → min)")

choice = int(input("Enter choice: "))

match choice:
    case 1:
        ascending = sorted(nums)
        print("Sorted Ascending:", ascending)

    case 2:
        descending = sorted(nums, reverse=True)
        print("Sorted Descending:", descending)

    case n:
        print("Invalid choice!")