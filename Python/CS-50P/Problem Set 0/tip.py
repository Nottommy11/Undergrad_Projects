def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d="test"):
    dollars = float(d.lstrip('$'))
    return dollars

def percent_to_float(p="test"):
    percent = float(p.rstrip('%')) * 0.01
    return percent

main()