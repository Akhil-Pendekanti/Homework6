from app.commands import Command

class MultiplyCommand(Command):

    def execute(self):
        numbers = input("Enter two space-separated numbers: ")
        num1, num2 = map(int, numbers.split())
        result = num1 * num2
        print("Multiplication result:", result)
        