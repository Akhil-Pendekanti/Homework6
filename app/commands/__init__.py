from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        self.commands[command_name] = command

    def execute_command(self, command_name: str):
        """Calling the execute method when command given is matched."""
        try:
            command_name = command_name.lower()
            self.commands[command_name].execute()
        except KeyError:
            print(f"No such command: {command_name}")
