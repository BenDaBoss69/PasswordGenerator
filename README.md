# Random Password Generator

A simple and secure-by-design password generator built using **Python** and the **Tkinter** GUI library. This application creates memorable passwords by combining two unique random nouns, a three-digit number, and a special character.

---

## Features

* **Memorable Passwords:** Generates passwords using a dictionary of common nouns from `noun_list_1000.txt`, making them easier to remember while maintaining complexity.
* **Simple GUI:** Easy-to-use interface built with **Tkinter**.
* **One-Click Generation:** Quickly generate a new password with the "Generate Password" button.
* **Copy to Clipboard:** Instantly copy the generated password to your clipboard using the "Copy to Clipboard" button.
* **Unique Noun Selection:** Ensures the two selected nouns are not duplicates in the generated password.
* **Password Strength Checker:** Enter any password (including generated ones) into the provided field and click "Check Strength" to get an immediate strength classification.

---

## Password Strength Checker

A new UI control and helper function evaluate password strength and display the result.

How to use:
* Type or paste a password into the "Enter password to check strength" field.
* Click "Check Strength".
* A dialog shows one of: `Strong`, `Medium`, or `Weak`.

Strength rules:
* Strong — length >= 12 and contains uppercase, lowercase, digit, and special character.
* Medium — length >= 8 and meets at least three of the four character-type requirements.
* Weak — everything else.

---

## Prerequisites

To run this application, you will need **Python** (version 3.x is recommended). The required GUI library, **Tkinter**, is typically bundled with standard Python installations.

If you encounter issues, you may need to ensure Tkinter is installed. You can attempt to install it by running:

```bash
pip install tk
```

**Verification (Optional):** You can verify your Tkinter installation by running a small Python script:

```python
import tkinter
tkinter._test()
```

If a small test window appears, Tkinter is correctly installed.

---

## How to Run

1.  **Navigate to the Directory:** Open your terminal or command prompt and change the directory to the location of the `password-generator.py` file.

    ```bash
    cd path/to/PasswordGenerator/
    ```

2.  **Execute the Script:** Run the application using the Python interpreter:

    ```bash
    python password-generator.py
    ```

    The graphical interface should open, ready for use.

---

## Password Generation Logic

The `genPassword` function constructs a password by following this formula:

$$\text{Password} = \text{Noun}_1 + \text{Noun}_2 + \text{Number} + \text{SpecialCharacter}$$

1.  **Two Unique Nouns:** It randomly selects two unique nouns from the `noun_list_1000.txt` file. The script ensures the two selected nouns are not duplicates.
2.  **Three-Digit Number:** A random number between **100** and **999** is generated.
3.  **Special Character:** A random special character is chosen from the list: `!`, `@`, `#`, `$`, `%`, `^`, `&`, `*`, `-`, `_`.

**Example Generated Password:** `ElephantCactus456!`

---

## Project Structure

The project consists of three main files:

* `password-generator.py`: The main Python script containing the password generation logic and the Tkinter GUI setup.
* `noun_list_1000.txt`: A simple text file containing a large list of nouns used for creating the memorable passwords.
* `README.md`: This file, providing project information and instructions.

