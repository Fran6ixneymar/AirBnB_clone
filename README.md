# Airbnb Clone

This project is an Airbnb clone, which aims to replicate some of the core functionalities of the popular accommodation rental platform. The clone is implemented as a Python package with a command interpreter, allowing users to interact with the application through a command-line interface.

## Command Interpreter

The command interpreter is built using the `cmd` module in Python. It provides a command-line interface where users can enter commands to perform various operations related to managing accommodations, bookings, users, and more.

### How to Start the Command Interpreter

To start the command interpreter, you need to run the `console.py` file. You can do this by executing the following command in your terminal:

```
python console.py
```

### How to Use the Command Interpreter

Once the command interpreter is running, you can enter commands to interact with the application. The commands follow a specific syntax: `command [arguments]`.

Here are some of the commands available in the command interpreter:

- `create <object>`: Creates a new object. Available objects include "accommodation," "booking," and "user." You can specify additional arguments to provide details for the object.

- `show <object> <id>`: Shows the details of a specific object. You need to provide the object type (e.g., "accommodation") and the object's ID.

- `update <object> <id> <attribute> <value>`: Updates a specific attribute of an object. You need to provide the object type, the object's ID, the attribute name, and the new value.

- `delete <object> <id>`: Deletes a specific object. You need to provide the object type and the object's ID.

- `list <object>`: Lists all objects of a specific type.

These are just a few examples of the commands available in the command interpreter. You can explore the application further by trying out different commands and their variations.

### Examples

Here are some examples of how to use the command interpreter:

1. Creating a new accommodation:

```
create accommodation --name "Cozy Cabin" --location "Mountain View" --price 100
```

This command creates a new accommodation with the name "Cozy Cabin," located in "Mountain View," and priced at $100.

2. Showing details of an accommodation:

```
show accommodation 123
```

This command displays the details of the accommodation with the ID 123.

3. Updating an accommodation's price:

```
update accommodation 123 price 150
```

This command updates the price of the accommodation with the ID 123 to $150.

4. Deleting an accommodation:

```
delete accommodation 123
```

This command deletes the accommodation with the ID 123.

5. Listing all accommodations:

```
list accommodation
```

This command lists all the accommodations available in the application.

These examples illustrate how to interact with the command interpreter to perform various operations within the Airbnb clone.

Feel free to explore more commands and experiment with different options to gain a deeper understanding of the functionalities offered by the Airbnb clone.
