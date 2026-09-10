"""A tiny bike-rental shop app used for Git skills practice.

Nothing here is meant to be complex. The file exists purely to give you
something small and readable to branch, edit, commit, and merge -- the
point of the exercise is the Git workflow, not the code.
"""

import argparse

SHOP_NAME = "Pedal Post"
OPENING_HOURS = "8am - 7pm"

# Each entry is "bike model": hourly rate (in USD).
RATES = {
    "cruiser": 8.0,
    "mountain": 12.0,
    "road": 10.0,
    # Add new models here
    "electric": 18.0
}

FLEET = {
    "cruiser": 16,
    "mountain": 4,
    "electric": 5
}

CUSTOMERS = {
    "C1001": "Susan",
    "C1002": "Mark Twaine",
    "C1003": "Mathew Lembark" 
}

def new_main():
    print("New main commit need to merge with feature/new")
def new():
    print("To be merged into main")
def new_v2():
    pass


def current_main():
    pass

def current_main2():
    pass

def total_bikes():
    print()
    total = 0
    for entry, amount in FLEET.items():
        rate = RATES[entry]
        total += (rate * amount)
    return total

def greet_customer():
    """Print a short welcome message using the shop's name and hours."""
    print(f"Welcome to {SHOP_NAME}! We're open {OPENING_HOURS}.")


def print_rates():
    """Print each bike model, its hourly rate, and how many are available.

    Not every model is necessarily tracked in FLEET (e.g. a newly added
    model might not have stock recorded yet) -- those are shown as
    "not tracked" rather than assumed to be zero or unlimited.
    """
    for model, rate in RATES.items():
        available = FLEET.get(model)
        stock = "not tracked" if available is None else f"{available} available"
        print(f"{model}: ${rate:.2f}/hr ({stock})")


def restock(model, quantity):
    """Add `quantity` units of `model` to the fleet."""
    FLEET[model] = FLEET.get(model, 0) + quantity
    return FLEET[model]


def main():
    """Entry point. Run with --help (or -h) to see usage."""
    parser = argparse.ArgumentParser(
        prog="shop.py",
        description="A tiny bike-rental shop CLI used for Git skills practice.",
        epilog="With no options, greets the customer and prints the rates.",
    )
    parser.add_argument(
        "--restock",
        nargs=2,
        metavar=("MODEL", "QUANTITY"),
        help="Add QUANTITY units of MODEL to the fleet and print the new total.",
    )

    parser.add_argument("--total", action="store_true")
    args = parser.parse_args()

    if args.total:
        total = total_bikes()
        print(f"The total is is {total}")
    elif args.restock:
        model, quantity = args.restock
        new_total = restock(model, int(quantity))
        print(f"Restocked {model}: now {new_total} in fleet.")
        return

    greet_customer()
    print_rates()


if __name__ == "__main__":
    main()
