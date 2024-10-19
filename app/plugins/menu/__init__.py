import sys
from app.commands import Command


class MenuCommand(Command):
    def execute(self):
        print(f'Welcome to the Basic Calcualator.\nSelect the operation to be performed\nAdd\nSubtract\nMultiply\nDivide')