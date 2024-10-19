from app.commands import Command

class DivideCommand(Command):

    def execute(self):
        result = 0.0
        numbers = input("Enter two space-separated numbers: ")
        num1, num2 = map(int, numbers.split())
        if(num2 != 0):
            result = num1 / num2
            print("Division result:",result)
        else:
            print("Error Occured! DivisionByzero or DivisionByNegative")
        