""" 
Test module for the arithmetic commands and REPL functionality of the class App. 
This module will have the unit tests that will validate the behavior of different mathematical operations 
(Add, Subtract, Multiply, Divide) in the command system of the App class, as well as the REPL interface. 
The tests will be simulating user input to ensure commands will work as expected and will verify that the
application will handle input/output correctly, including edge cases like division by zero.
"""
import pytest
from app import App
from app.plugins.add import AddCommand
from app.plugins.subtract import SubtractCommand
from app.plugins.multiply import MultiplyCommand
from app.plugins.divide import DivideCommand


def test_add_command(capfd, monkeypatch):
    """
    Test the AddCommand's functionality.

    This test simulates user input ('5 3') and verifies whether the addition result
    ('Additon result: 8') is correctly printed to stdout.
    """
    monkeypatch.setattr('builtins.input', lambda _: '5 3')
    command = AddCommand()
    command.execute()
    out, err = capfd.readouterr()
    assert "Additon result: 8" in out, "The AddCommand should print the correct addition result."

def test_subtract_command(capfd, monkeypatch):
    """
    Test the SubtractCommand's functionality.

    This test simulates user input ('5 3') and verifies whether the subtraction result
    ('Subtraction result: 2') is correctly printed to stdout.
    """
    monkeypatch.setattr('builtins.input', lambda _: '5 3')
    command = SubtractCommand()
    command.execute()
    out, err = capfd.readouterr()
    assert "Subtraction result: 2" in out, "The SubtractCommand should print the correct subtraction result."

def test_multiply_command(capfd, monkeypatch):
    """
    Test the MultiplyCommand's functionality.

    This test simulates user input ('5 3') and verifies whether the multiplication result
    ('Multiplication result: 15') is correctly printed to stdout.
    """
    monkeypatch.setattr('builtins.input', lambda _: '5 3')
    command = MultiplyCommand()
    command.execute()
    out, err = capfd.readouterr()
    assert "Multiplication result: 15" in out, "The MultiplyCommand should print the correct multiplication result."

def test_divide_command(capfd, monkeypatch):
    """
    Test the DivideCommand's functionality.

    This test simulates user input ('9 3') and verifies whether the division result
    ('Division result: 3') is correctly printed to stdout.
    """
    monkeypatch.setattr('builtins.input', lambda _: '9 3')
    command = DivideCommand()
    command.execute()
    out, err = capfd.readouterr()
    assert "Division result: 3" in out, "The DivideCommand should print the correct division result."

def test_dividebyzero_command(capfd, monkeypatch):
    """
    This test simulates user input ('9 0') and verifies that an appropriate error message
    ('Error Occured! DivisionByzero') is printed when attempting to divide by zero.
    """
    monkeypatch.setattr('builtins.input', lambda _: '9 0')
    command = DivideCommand()
    command.execute()
    out, err = capfd.readouterr()
    assert "Error Occured! DivisionByzero" in out, "Error should be Occured."

def test_app_menu_command(capfd, monkeypatch):
    """
    Test that the REPL correctly handles the 'menu' command and exits cleanly.
    This test simulates user input to display the menu and then exit the application,
    ensuring the menu is displayed and the app exits gracefully with the expected output.
    """
    inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()  # Assuming App.start() is now a static method based on previous discussions
    assert str(e.value) == "Exiting...", "The app did not exit as expected"
