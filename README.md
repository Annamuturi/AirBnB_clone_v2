# HBNB - The Console

Welcome to HBNB - The Console, a backend interface for managing program data in a student project to build a clone of the AirBnB website. This console allows you to interact with the program data through a command-line interface. You can create, update, and destroy objects, as well as manage file storage, using a system of JSON serialization/deserialization for persistent storage between sessions.

## Project Overview

This project is divided into several tasks, each focusing on a different aspect of the console's development. Here's a breakdown of the tasks and their corresponding files:

### Task 0: Authors and README File

- `AUTHORS`: Lists the project authors.

### Task 1: Pep8 Compliance

- No specific files; all code is expected to be pep8 compliant.

### Task 2: Unit Testing

- `/tests`: Contains unit tests for the class-defining modules.

### Task 3: Make BaseModel

- `/models/base_model.py`: Defines the `BaseModel` class, a parent class to be inherited by all model classes.

### Task 4: Update BaseModel with kwargs

- `/models/base_model.py`: Adds functionality to recreate an instance of a class from a dictionary representation.

### Task 5: Create FileStorage class

- `/models/engine/file_storage.py`: Defines the `FileStorage` class, which manages the persistent file storage system.
- `/models/__init__.py`: Initializes the storage instance.
- `/models/base_model.py`: Updates `BaseModel` class with the storage management methods.

### Task 6: Console 0.0.1

- `console.py`: Adds basic functionality to the console program, allowing it to quit, handle empty lines, and respond to Ctrl+D input.

### Task 7: Console 0.1

- `console.py`: Updates the console with methods allowing the user to create, destroy, show, and update stored data.

### Task 8: Create User class

- `console.py`: Dynamically implements a `User` class in the console.
- `/models/engine/file_storage.py`: Updates `FileStorage` to support the new class.

### Task 9: More Classes

- `/models/user.py`: Implements the `User` class.
- `/models/place.py`: Implements the `Place` class.
- `/models/city.py`: Implements the `City` class.
- `/models/amenity.py`: Implements the `Amenity` class.
- `/models/state.py`: Implements the `State` class.
- `/models/review.py`: Implements the `Review` class.

### Task 10: Console 1.0

- `console.py`: Updates the console and file storage system to work dynamically with all implemented classes.

## Getting Started

1. Clone this repository:

   ```bash
   git clone <https://github.com/Annamuturi/AirBnB_clone_v2.git>
2 . cd AirBnB_clone
3. ./console.py
- Create a BaseModel instance
(hbnb) create BaseModel

- Show a specific object
(hbnb) show BaseModel <object_id>

- Destroy an object
(hbnb) destroy BaseModel <object_id>

- Update an object's attribute
(hbnb) update BaseModel <object_id> <attribute_name> <new_value>

- Use alternative syntax to show all User objects
(hbnb) User.all()

-  Use alternative syntax to update a User's attribute
(hbnb) User.update(<id>, <attribute_name>, <new_value>)

## AUTHORS
Anna Muturi
Gbolahan Oyeniyi
