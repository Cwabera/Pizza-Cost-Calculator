# Python Pizza Order Cost Calculator

## Overview

The **Python Pizza Order Cost Calculator** is a simple command-line application that calculates the total cost of a pizza order based on user input. The program prompts the user for the pizza size, number of additional toppings, and delivery distance, then computes the total cost according to predefined pricing rules.

This project demonstrates core Python programming concepts including user input handling, conditional statements, arithmetic calculations, and formatted output.

---

## Learning Objectives

This project helps practice the following Python skills:

* Using `input()` to gather user data
* Implementing `if` / `elif` conditional logic
* Performing arithmetic calculations
* Using formatted output with **f-strings**
* Building a simple real-world command-line program

---

## Pricing Rules

### Pizza Sizes

* **Small Pizza**: $8
* **Large Pizza**: $12

### Toppings

* Each additional topping costs **$1**

### Delivery Fee

* **$2** for the first **5 miles**
* **$1** for each additional mile after 5 miles

---

## How the Program Works

1. The user selects a pizza size (`small` or `large`)
2. The user enters the number of additional toppings
3. The user enters the delivery distance in miles
4. The program calculates:

   * Base pizza cost
   * Topping cost
   * Delivery cost
5. The total order cost is displayed.

---

## Example Run

```
Enter pizza size (small/large): small
How many extra toppings?: 2
Delivery distance in miles?: 7

Order Summary
-------------
Pizza size: small
Toppings cost: $2
Delivery cost: $4
Total cost: $14
```

---

## How to Run the Program

### 1. Clone or download the project

```
git clone <your-repository-url>
cd pizza-calculator
```

### 2. Run the Python script

```
python3 pizza_calculator.py
```

### 3. Follow the prompts in the terminal

---

## Technologies Used

* Python 3
* Command Line Interface (CLI)

---

## Project Structure

```
pizza-calculator/
│
├── pizza_calculator.py
└── README.md
```

---

## Author: CWABERA

Created as part of a Python programming lab exercise.
