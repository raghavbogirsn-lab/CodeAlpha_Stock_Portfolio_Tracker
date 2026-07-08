# 📈 Stock Portfolio Tracker

A simple command-line Python tool that calculates the total investment value of a user's stock portfolio using a hardcoded dictionary of stock prices. Built as part of the **CodeAlpha Python Programming Internship**.

## Features

- 📋 Displays a list of available stocks and their current prices
- ➕ Lets the user build a portfolio by entering stock symbols and quantities
- ✅ Validates stock symbols and quantities, with clear error messages for invalid input
- 🧮 Calculates the subtotal for each holding and the total portfolio value
- 🗂️ Prints a clean, formatted summary of the portfolio
- 💾 Optionally saves the report to a `.txt` or `.csv` file with a timestamp

## Requirements

- Python 3.6+
- No external libraries needed (uses only the standard library: `csv`, `datetime`)

## Installation

```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
```

## Usage

Run the script from the command line:

```bash
python CodeAlpha_stock_tracker.py
```

You'll be shown the list of available stocks, then prompted to enter a stock symbol and quantity repeatedly. Type `done` (or press Enter) when you're finished adding stocks.

### Available Stocks (hardcoded)

| Symbol | Price (per share) |
|--------|-------------------|
| AAPL   | $180              |
| TSLA   | $250              |
| GOOGL  | $140              |
| AMZN   | $175              |
| MSFT   | $410              |

## Example Run

```
========================================
   📈 STOCK PORTFOLIO TRACKER 📈
========================================

Available stocks and prices:
  AAPL: $180
  TSLA: $250
  GOOGL: $140
  AMZN: $175
  MSFT: $410

Enter stock symbol (or 'done' to finish): AAPL
Enter quantity: 5
  ✅ Added: 5 shares of AAPL at $180.00 = $900.00

Enter stock symbol (or 'done' to finish): done

----- Portfolio Summary -----
AAPL: 5 shares @ $180.00 = $900.00
Total Investment: $900.00
------------------------------

Save results to a file? (yes/no): yes
Save as .txt or .csv? csv
Saved successfully to portfolio_report.csv

Thank you for using the Stock Portfolio Tracker!
```

## Output Files

When saving is chosen, the script generates one of the following in the project directory:

- `portfolio_report.txt` — a plain-text summary with a timestamp
- `portfolio_report.csv` — a CSV file with columns for Symbol, Quantity, Price, and Subtotal

## Project Structure

```
.
├── CodeAlpha_stock_tracker.py   # Main script
└── README.md                    # Project documentation
```

## Key Concepts Used

- Dictionaries for stock price lookup
- Loops and input validation
- Functions and modular code organization
- Basic file handling (`.txt` and `.csv` output)
- The `datetime` module for timestamps

## Author

Developed as part of the **CodeAlpha Python Programming Internship**.

## License

This project is open source and available under the [MIT License](LICENSE).
