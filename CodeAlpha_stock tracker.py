"""
Stock Portfolio Tracker
------------------------
A simple command-line tool that calculates the total investment value
of a user's stock portfolio using a hardcoded dictionary of stock prices.

Key concepts used: dictionary, input/output, basic arithmetic, file handling (optional).
"""

import csv
from datetime import datetime

# ------------------------------------------------------------------
# Hardcoded dictionary of stock prices (symbol -> price per share)
# ------------------------------------------------------------------
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 175,
    "MSFT": 410
}


def show_available_stocks():
    """Display the list of stocks and their prices to the user."""
    print("\nAvailable stocks and prices:")
    for symbol, price in stock_prices.items():
        print(f"  {symbol}: ${price}")
    print()


def get_user_input():
    """
    Repeatedly ask the user for a stock symbol and quantity.
    Returns a list of dictionaries, each containing:
        {"symbol": str, "quantity": int, "price": float, "subtotal": float}
    """
    portfolio = []

    while True:
        symbol = input("Enter stock symbol (or 'done' to finish): ").strip().upper()

        if symbol == "DONE" or symbol == "":
            break

        # Validate that the stock exists in our price dictionary
        if symbol not in stock_prices:
            print(f"  ⚠️  '{symbol}' not found in stock list. Please try again.\n")
            continue

        # Validate the quantity input
        try:
            quantity = int(input("Enter quantity: "))
            if quantity <= 0:
                print("  ⚠️  Quantity must be a positive number. Please try again.\n")
                continue
        except ValueError:
            print("  ⚠️  Invalid input. Quantity must be a whole number. Please try again.\n")
            continue

        price = stock_prices[symbol]
        subtotal = price * quantity

        portfolio.append({
            "symbol": symbol,
            "quantity": quantity,
            "price": price,
            "subtotal": subtotal
        })

        print(f"  ✅ Added: {quantity} shares of {symbol} at ${price:.2f} = ${subtotal:.2f}\n")

    return portfolio


def calculate_total(portfolio):
    """Calculate and return the total investment value of the portfolio."""
    return sum(item["subtotal"] for item in portfolio)


def display_summary(portfolio, total):
    """Print a clean summary of the portfolio and total investment."""
    print("\n----- Portfolio Summary -----")
    if not portfolio:
        print("No stocks were added.")
        return

    for item in portfolio:
        print(f"{item['symbol']}: {item['quantity']} shares @ "
              f"${item['price']:.2f} = ${item['subtotal']:.2f}")

    print(f"Total Investment: ${total:.2f}")
    print("------------------------------\n")


def save_to_file(portfolio, total):
    """Ask the user whether to save results, and in which format (.txt or .csv)."""
    choice = input("Save results to a file? (yes/no): ").strip().lower()

    if choice != "yes":
        print("Results not saved.")
        return

    file_format = input("Save as .txt or .csv? ").strip().lower()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if file_format == "txt":
        filename = "portfolio_report.txt"
        try:
            with open(filename, "w") as f:
                f.write("Stock Portfolio Report\n")
                f.write(f"Generated on: {timestamp}\n")
                f.write("-" * 40 + "\n")
                for item in portfolio:
                    f.write(f"{item['symbol']}: {item['quantity']} shares @ "
                            f"${item['price']:.2f} = ${item['subtotal']:.2f}\n")
                f.write("-" * 40 + "\n")
                f.write(f"Total Investment: ${total:.2f}\n")
            print(f"Saved successfully to {filename}")
        except IOError as e:
            print(f"Error saving file: {e}")

    elif file_format == "csv":
        filename = "portfolio_report.csv"
        try:
            with open(filename, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["Generated on:", timestamp])
                writer.writerow([])
                writer.writerow(["Symbol", "Quantity", "Price", "Subtotal"])
                for item in portfolio:
                    writer.writerow([
                        item["symbol"],
                        item["quantity"],
                        f"{item['price']:.2f}",
                        f"{item['subtotal']:.2f}"
                    ])
                writer.writerow([])
                writer.writerow(["Total Investment", "", "", f"{total:.2f}"])
            print(f"Saved successfully to {filename}")
        except IOError as e:
            print(f"Error saving file: {e}")

    else:
        print("Invalid format choice. File not saved.")


def main():
    """Main function that runs the stock portfolio tracker program."""
    print("=" * 40)
    print("   📈 STOCK PORTFOLIO TRACKER 📈")
    print("=" * 40)

    show_available_stocks()
    portfolio = get_user_input()
    total = calculate_total(portfolio)
    display_summary(portfolio, total)

    if portfolio:
        save_to_file(portfolio, total)

    print("\nThank you for using the Stock Portfolio Tracker!")


if __name__ == "__main__":
    main()