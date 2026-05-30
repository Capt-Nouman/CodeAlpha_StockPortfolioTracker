# ============================================
#   CodeAlpha Internship - Task 2
#   Stock Portfolio Tracker
#   Intern: Nouman Majeed | CA/DF1/106067
# ============================================

import csv

# Hardcoded stock prices (dictionary)
STOCK_PRICES = {
    "AAPL":  180,   # Apple
    "TSLA":  250,   # Tesla
    "GOOGL": 140,   # Google
    "AMZN":  185,   # Amazon
    "MSFT":  420,   # Microsoft
    "META":  510,   # Meta
    "NFLX":  650,   # Netflix
    "NVDA":  900,   # NVIDIA
}

def show_available_stocks():
    print("\n📈 Available Stocks:")
    print("-" * 30)
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol:<8} ${price}")
    print("-" * 30)

def get_portfolio():
    portfolio = {}
    print("\n✅ Enter stock symbol and quantity (type 'done' to finish):")
    
    while True:
        symbol = input("\n  Stock Symbol (e.g. AAPL): ").strip().upper()
        
        if symbol == "DONE":
            break
        
        if symbol not in STOCK_PRICES:
            print(f"  ❌ '{symbol}' not found! Please choose from the list above.")
            continue
        
        try:
            qty = int(input(f"  Quantity for {symbol}: ").strip())
            if qty <= 0:
                print("  ❌ Quantity must be greater than 0!")
                continue
            portfolio[symbol] = portfolio.get(symbol, 0) + qty
        except ValueError:
            print("  ❌ Please enter a valid number!")
    
    return portfolio

def calculate_portfolio(portfolio):
    results = []
    total = 0
    for symbol, qty in portfolio.items():
        price      = STOCK_PRICES[symbol]
        investment = price * qty
        total     += investment
        results.append((symbol, qty, price, investment))
    return results, total

def display_results(results, total):
    print("\n" + "=" * 50)
    print("        📊 YOUR STOCK PORTFOLIO SUMMARY")
    print("=" * 50)
    print(f"  {'Stock':<8} {'Qty':<8} {'Price':<12} {'Investment'}")
    print("-" * 50)
    for symbol, qty, price, investment in results:
        print(f"  {symbol:<8} {qty:<8} ${price:<11} ${investment:,.2f}")
    print("-" * 50)
    print(f"  {'TOTAL INVESTMENT':<28} ${total:,.2f}")
    print("=" * 50)

def save_results(results, total):
    print("\n💾 Save your portfolio?")
    print("  1. Save as .txt")
    print("  2. Save as .csv")
    print("  3. Don't save")
    
    choice = input("\n  Enter choice (1/2/3): ").strip()
    
    if choice == "1":
        with open("portfolio_result.txt", "w") as f:
            f.write("=" * 50 + "\n")
            f.write("     STOCK PORTFOLIO SUMMARY\n")
            f.write("     Intern: Nouman Majeed | CA/DF1/106067\n")
            f.write("=" * 50 + "\n")
            f.write(f"{'Stock':<8} {'Qty':<8} {'Price':<12} {'Investment'}\n")
            f.write("-" * 50 + "\n")
            for symbol, qty, price, investment in results:
                f.write(f"{symbol:<8} {qty:<8} ${price:<11} ${investment:,.2f}\n")
            f.write("-" * 50 + "\n")
            f.write(f"TOTAL INVESTMENT:            ${total:,.2f}\n")
            f.write("=" * 50 + "\n")
        print("  ✅ Saved as 'portfolio_result.txt'")

    elif choice == "2":
        with open("portfolio_result.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Stock", "Quantity", "Price ($)", "Investment ($)"])
            for symbol, qty, price, investment in results:
                writer.writerow([symbol, qty, price, f"{investment:,.2f}"])
            writer.writerow([])
            writer.writerow(["TOTAL", "", "", f"{total:,.2f}"])
        print("  ✅ Saved as 'portfolio_result.csv'")

    else:
        print("  ℹ️  Results not saved.")

def main():
    print("\n" + "=" * 50)
    print("   🚀 STOCK PORTFOLIO TRACKER")
    print("   CodeAlpha Internship Task 2")
    print("=" * 50)

    show_available_stocks()
    portfolio = get_portfolio()

    if not portfolio:
        print("\n⚠️  No stocks entered. Exiting...")
        return

    results, total = calculate_portfolio(portfolio)
    display_results(results, total)
    save_results(results, total)

    print("\n👋 Thank you for using Stock Portfolio Tracker!\n")

if __name__ == "__main__":
    main()
