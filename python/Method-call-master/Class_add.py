# Define a class called Add
class Add:
    # Constructor method to initialize the instance with a value
    def __init__(self, value):
        # Check if the provided value is an integer
        if not isinstance(value, int):
            # Raise a TypeError if the value is not an integer
            raise TypeError("This only accepts numbers.")
        # Assign the value to the instance variable
        self.value = value

    # Define the behavior when an instance is called
    def __call__(self, next_value):
        # Create a new instance with the sum of the current value and the provided value
        return Add(self.value + next_value)

    # Define the string representation of the instance
    def __repr__(self):
        return f"{self.value}"

# Try block to handle potential TypeErrors during instantiation
try:
    # Create instances and demonstrate the functionality
    result1 = Add(10)
    result2 = Add(10)(11)
    result3 = Add(10)(11)(12)
    
    # Display the results
    sum_result = result1, result2, result3
    for i in sum_result:
        print(i)

# Except block to handle TypeErrors and display an error message
except TypeError as e:
    print(f"TypeError: {e}")

