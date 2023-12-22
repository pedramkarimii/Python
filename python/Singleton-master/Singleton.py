class Id:
    Get_Value = {}
    list = []

    def __init__(self, input_value):
        self.input_value = input_value

    def __new__(cls, input_value):
        if input_value not in cls.Get_Value:
            add = cls.Get_Value
            cls.Get_Value[input_value] = add
            return True
        else:
            return False

    def checking_values(self):
        if self.input_value not in self.list:
            add = self.list
            self.list[self.input_value] = add
            return False
        else:
            return True

    def __eq__(self, other):
        return self.input_value == other

    def __repr__(self):
        return f"{self.input_value}"


# input
try:
    num_inputs = int(input("Enter the number of inputs: "))
    inputs = [input("Enter a value: ") for _ in range(num_inputs)]
    # output
    results = [Id(user_input) for user_input in inputs]
    print("Repeated words(True or False):", results)
except ValueError:
    print("ValueError!!!Enter the correct value")

# Example question
akbar = Id("akbar")
asqar = Id("asqar")
sum_input = f"input1: {akbar}\ninput2: {asqar}"

print(akbar is asqar)
print(Id("akbar") == Id("asqar"))
