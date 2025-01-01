# ChoobinV2 - Persian Programming Language

## Introduction
**ChoobinV2** is a modern Persian programming language designed for simplicity and efficiency. It is suitable for a variety of applications, from basic scripting to complex software development. The goal of Choobin is to make programming accessible and enjoyable for Persian-speaking developers.

## Features
- **Simple Syntax**: Easy to read and write.
- **Powerful Constructs**: Includes modern programming features.
- **Versatile**: Suitable for scripting, web development, and more.
- **Open Source**: Fully open-source and community-driven.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Basic Commands](#basic-commands)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites
To run the Choobin interpreter, you need Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

### Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/OnlyParsa/ChoobinV2
Navigate to the Project Directory:
cd ChoobinV2
Install the Package:
pip install .
Usage
Running the Interpreter
To start the Choobin interpreter, use the following command:

choobin
Running Choobin Scripts
You can also run .choob files directly:

Create a Choobin script file, for example example.choob:
say "Hello, Choobin!"
Make the script executable:
chmod +x example.choob
Run the script:
./example.choob
Basic Commands
say Command
The say command is used to print text or the result of an expression to the output.

Example:
say "Hello, Choobin!"
Output:

Hello, Choobin!
set Command
The set command is used to define variables.

Example:
choobin
set x = 10
say x
Output:

10
repeat Command
The repeat command is used to execute a block of code multiple times.

Example:
choobin
repeat 3 {
    say "This is a loop"
}
Output:

Code
This is a loop
This is a loop
This is a loop
More Commands
For more commands and detailed documentation, please refer to the official documentation.

Examples
Here are some example scripts to help you get started:

Basic Arithmetic
choobin
set a = 5
set b = 3
say a + b
Conditional Statements
choobin
set x = 10
if (x > 5) {
    say "x is greater than 5"
} else {
    say "x is not greater than 5"
}
Functions
choobin
def greet(name) {
    say "Hello, " + name + "!"
}
greet("Parsa")
Contributing
We welcome contributions from the community! Please read our Contributing Guide to learn how to get involved.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Thank you for using Choobin! We hope you enjoy programming with it.
