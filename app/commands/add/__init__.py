from app.commands import Command

class AddCommand(Command):

    def execute(self):
        numbers = input("Enter two space-separated numbers: ")
        num1, num2 = map(int, numbers.split())
        result = num1 + num2
        print("Additon result:", result)
        