# Raven-Morph-API

Raven Morph API is a project inspired by the character Raven Darkhölme, also known as Mystique, from the X-Men. This API uses Flask to provide dynamic endpoints based on a static JSON file. From a JSON file, Raven Morph can provide a static API, which is very useful for testing environments.

This tool aims to ease developers' efforts in populating data in front-end environments without sacrificing the simulation of a real environment, maintaining the possibility of flexibility and ease of inserting mockup content.

## Features

- Dynamic reading of a JSON file to create endpoints based on the JSON objects.
- Provision of static data through a simple and easy-to-use API.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/raven-api.git
   ```

2. Install the dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Ensure you have the `data.json` file with the data you want to provide through the API.

2. Run the Flask server:

   ```bash
   python app.py
   ```

3. Access the API endpoints at `http://localhost:5000/`.

## JSON Example

Example structure of the `data.json` file:

```json
{
    "initialBalance": -3205,
    "finalBalance": 4722,
    "savingsReduction": -247,
    "monthlySavings": 7927,
    "expenses": [
        {"category": "Food", "planned": 50, "actual": 50, "difference": 0},
        {"category": "Transport", "planned": 100, "actual": 90, "difference": 10}
    ],
    "income": [
        {"category": "Savings", "planned": 50, "actual": 50, "difference": 0},
        {"category": "Salary", "planned": 3000, "actual": 3000, "difference": 0}
    ]
}
```

For the example above, each object in the JSON will return a respective endpoint with its exact name and internal data, as in the following examples:

- http://127.0.0.1:5000/initialBalance
```json
{
 "initialBalance": -3205
}
```
- http://127.0.0.1:5000/expenses
```json
{
  "expenses": [
    {
      "category": "Food",
      "difference": 0,
      "planned": 50,
      "actual": 50
    },
    {
      "category": "Transport",
      "difference": 10,
      "planned": 100,
      "actual": 90
    }
  ]
}
```
## Contributions

Contributions are welcome! Feel free to submit pull requests or open issues if you find any problems or have suggestions.
