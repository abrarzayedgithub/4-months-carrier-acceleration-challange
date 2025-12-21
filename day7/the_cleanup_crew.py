try:
    numerator = float(input("Enter the first number: "))
    denominator = float(input("Enter the second number: "))
    result = numerator / denominator
    print(f"Result: {result}")
except ZeroDivisionError:
   print("Error: You cannot divide by zero.")
except ValueError:
   print("Error: Please enter valid numerical values.")
finally:
    print("Execution Complete")