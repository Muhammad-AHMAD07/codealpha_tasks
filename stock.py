stock_prices = {
    "ABC": 100,
    "DEF": 400,
    "GHI": 289,
    "JKL": 330,
    "MNO": 30
}

def get_stocks():
    portfolio = {}
    print("Enter your stocks (type 'done' when finished)")
    while True:
        stock = input("Stock symbol (e.g., ABC): ").upper()
        if stock == "DONE":
            break
        if stock not in stock_prices:
            print("Invalid stock symbol. Try again.")
            continue
        try:
            quantity = float(input(f"Quantity of {stock}: "))
            portfolio[stock] = quantity
        except ValueError:
            print("Please enter a valid number for quantity.")
    return portfolio

def calculate_total(portfolio):
    total_value = 0
    print("\nYour Portfolio:")
    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        value = price * qty
        total_value += value
        print(f"{stock}: {qty} shares x Rs {price} = Rs {value}")
    print(f"\nTotal Investment Value: Rs {total_value}")
    return total_value

def save_to_file(portfolio, total_value):
    filename = input("\nEnter filename to save portfolio (e.g., portfolio.txt or portfolio.csv): ")

    if filename.endswith(".csv"):
        import csv
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Stock", "Quantity", "Price per Share", "Value"])
            for stock, qty in portfolio.items():
                value = stock_prices[stock] * qty
                writer.writerow([stock, qty, stock_prices[stock], round(value, 2)])
            writer.writerow(["", "", "Total Value", round(total_value, 2)])
        print("Portfolio saved to CSV file:", filename)

    elif filename.endswith(".txt"):
        with open(filename, "w") as file:
            file.write("=== Your Portfolio ===\n")
            for stock, qty in portfolio.items():
                value = stock_prices[stock] * qty
                file.write(f"{stock}: {qty} X Rs {stock_prices[stock]} = Rs {value}\n")
            file.write(f"\nTotal Investment: Rs {total_value}\n")
        print("Portfolio saved to text file:", filename)
    else:
        print("Unsupported file format. Use .txt or .csv")

pf = get_stocks()
total = calculate_total(pf)

save = input("\nWould you like to save this portfolio to a file? (y/n): ").lower()
if save == "y":
    save_to_file(pf, total)

print("\nThank you for using the Stock Tracker!")