# E-commerce Packaging Algorithm

This project implements a packaging algorithm that helps create the best possible product packages based on user-defined priorities, budget, and available items. It generates multiple packages while ensuring that prioritized items are considered and any budget constraints are respected.
Features

    Create packages based on a specified budget and prioritized items.
    Add additional items to the package within the remaining budget.
    Provide error messages for prioritized items that cannot be afforded.
    Generate multiple distinct packages based on the available item collection.

## Requirements

    Python 3.x
    No additional libraries are required.

## Getting Started
Clone the Repository

To clone this repository, follow these steps:

    1.Open your terminal (Command Prompt, PowerShell, or any terminal emulator).

    2. Navigate to the directory where you want to clone the project.

    3. Run the following command:

```bash

git clone https://github.com/Makbelhailu/packaging-algorithm.git
```

Change to the project directory:

```bash

    cd packaging-algorithm
```
Usage

    Run the script using the command line:

```bash

python algorithm.py # or python3 algorithm.py
```
Enter your budget and priorities when prompted. The priorities should be comma-separated. For example:

    Enter your budget: 1000
    Enter your priority items (comma-separated): mirror,desk,bed

The script will output the generated packages, including their total prices and messages regarding remaining budget or affordability of prioritized items.

### Example

When you run the program with a budget of 1000 and priorities of mirror,desk,bed, the output might look like this:

```json

Package 1:
{
    "total_price": 999.99,
    "package": [
        {"name": "Desk", "price": 149.99},
        {"name": "Mirror", "price": 59.99},
        {"name": "Rug", "price": 199.99},
        ...
    ],
    "remaining_budget": 0,
    "message": "No remaining budget."
}

Package 2:
{
    "total_price": 850.00,
    "package": [
        {"name": "Sofa Bed", "price": 599.99},
        ...
    ],
    "remaining_budget": 150.00,
    "message": "Remaining budget: $150.00"
}
```

## License

This project is open source and available under the MIT License.
