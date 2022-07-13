def main():
    dollars = input("How much was the meal? ")
    percent = input("What percentage would you like to tip? ")
    tip = float(dollars) * (float(percent)/100)
    print(f"Leave ${tip:.2f}")

main()