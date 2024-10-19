'''
This module contains tests for the App class's REPL functionality.
The tests check:
- The behavior of the REPL when it receives the 'exit' command.
- The handling of unknown commands before exiting the REPL.
'''
import pytest
from app import App

def test_app_start_exit_command(capfd, monkeypatch):
    """Test that the REPL exits correctly on 'exit' command."""
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    assert e.type == SystemExit

def test_app_start_unknown_command(capfd, monkeypatch):
    """Test how the REPL handles an unknown command before exiting."""
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit) as excinfo:
        app.start()
    captured = capfd.readouterr()
    assert "No such command: unknown_command" in captured.out
