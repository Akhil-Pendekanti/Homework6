# Plugins Architecture - Homework5

This repository implements a plugin-based command handling system in Python. The project demonstrates how to dynamically load and execute commands through a plugin system.

## Branches

- **master**: The main branch with all the core functionality.
- **commands**: A branch focused on implementing different command classes.
- **plugins**: The current branch where the plugin system for command handling is implemented.

## Features

- **Command Classes**: The project supports various command classes, such as `AddCommand`, which takes user input and returns the addition of two numbers.
- **Plugin System**: The plugin system dynamically loads and handles commands, allowing for easy extension and customization without modifying the core logic.
- **Testing**: Includes parameterized test cases to validate the functionality of command classes.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Akhil-Pendekanti/HomeWork5.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Homework5
    ```

3. Checkout the `plugins` branch to access the latest plugin system implementation:

    ```bash
    git checkout plugins
    ```

4. Install any dependencies (if applicable).
    ```bash
    pip3 install -r requirements.txt
    ```

5. **Run the main Python file:**
    ```bash
    python main.py
    ```

6. **Execute a command:**
    The program will prompt for user input. For example, to add two numbers:
    ```
    Type 'menu' to show menu
    Type 'exit' to exit 
    >>> menu
    Welcome to the Basic Calcualator.
    Select the operation to be performed
    Add
    Subtract
    Multiply
    Divide
    >>> add
    Enter two space-seperated numbers: 23 2
    Addition result: 25
    ```

## Running Tests

To run the tests for this project:
Results are stored in the folder **Results** for the main branch and the child branches.

```bash
pytest 
pytest --pylint
pytest --pylint --cov
```

## Usage

To run the project:

```bash
python main.py