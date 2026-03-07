import sys


def parse_inventory(args: list) -> dict:
    inventory: dict = {}
    for arg in args:
        try:
            name, quantity = arg.split(":")
            qty: int = int(quantity)
            if qty <= 0:
                print(f"Error: '{name}' quantity must be positive, got {qty}")
                continue
            inventory[name] = {
                "name": name,
                "quantity": qty
            }
        except ValueError:
            print(f"Invalid format '{arg}' — use \"item:quantity\"")
    return inventory


def total_quantity(inventory: dict) -> int:
    total = 0
    for item in inventory.values():
        total += item["quantity"]
    return total


def unique_items(inventory: dict) -> int:
    return len(inventory)


def system_analysis(inventory: dict) -> None:
    print(f"Total items in inventory: {total_quantity(inventory)}")
    print(f"Unique item types: {unique_items(inventory)}")


def display_inventory(inventory: dict) -> None:
    print("\n=== Current Inventory ===")
    total = total_quantity(inventory)
    printed = {}

    for _ in inventory:
        max_name = None
        max_qty = 0
        for name, item in inventory.items():
            if name not in printed and item["quantity"] > max_qty:
                max_qty = item["quantity"]
                max_name = name
        if max_name:
            qty = inventory.get(max_name)["quantity"]
            percentage = (qty / total) * 100
            if qty > 1:
                print(f"{max_name}: {qty} units ({percentage:.1f}%)")
            else:
                print(f"{max_name}: {qty} unit ({percentage:.1f}%)")
            printed[max_name] = True


def display_stats(inventory: dict) -> None:
    print("\n=== Inventory Statistics ===")
    max_name = None
    max_qty = 0
    min_name = None
    min_qty = None
    for name, item in inventory.items():
        if item["quantity"] > max_qty:
            max_qty = item["quantity"]
            max_name = name
        if min_qty is None or item["quantity"] < min_qty:
            min_qty = item["quantity"]
            min_name = name
    if max_name:
        if max_qty > 1:
            print(f"Most abundant: {max_name} ({max_qty} units)")
        else:
            print(f"Most abundant: {max_name} ({max_qty} unit)")
    if min_name:
        if min_qty > 1:
            print(f"Least abundant: {min_name} ({min_qty} units)")
        else:
            print(f"Least abundant: {min_name} ({min_qty} unit)")


def display_categories(inventory: dict) -> None:
    print("\n=== Item Categories ===")
    scarce: dict = {}
    moderate: dict = {}
    for name, item in inventory.items():
        qty = item["quantity"]
        if qty > 3:
            moderate.update({name: qty})
        else:
            scarce.update({name: qty})
    if moderate:
        print(f"Moderate: {moderate}")
    if scarce:
        print(f"Scarce: {scarce}")


def display_suggestions(inventory: dict) -> None:
    needed = ""
    for name, item in inventory.items():
        if item["quantity"] <= 1:
            needed += name + ", "
    if needed:
        print("\n=== Management Suggestions ===")
        print(f"Restock needed: {needed[:-2]}")


def display_properties(inventory: dict) -> None:
    print("\n=== Dictionary Properties Demo ===")
    key_str = ""
    val_str = ""
    for val in inventory.keys():
        key_str += val + ", "
    for val in inventory.values():
        val_str += f"{val['quantity']}, "
    print(f"Dictionary keys: {key_str[:-2]}")
    print(f"Dictionary values: {val_str[:-2]}")
    key_name = None
    for key in inventory.keys():
        key_name = key
        break
    result = inventory.get(key_name) is not None
    print(f"Sample lookup - '{key_name}' in inventory: {result}")


def main() -> None:
    print("=== Inventory System Analysis ===")
    if len(sys.argv) < 2:
        print("Usage: python3 ft_inventory_system.py <item:quantity> ...")
        return
    inventory = parse_inventory(sys.argv[1:])
    if not inventory:
        return

    system_analysis(inventory)

    display_inventory(inventory)

    display_stats(inventory)

    display_categories(inventory)

    display_suggestions(inventory)

    display_properties(inventory)


if __name__ == "__main__":
    main()
