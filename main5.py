# bill generation App

# {item:^10} stirng formatting alinging it to centre
#{'-' *74} repeating 74 times
#{' ' * 54} repeat space 54 times
#u20B9 fro rupees symbol

# Bill Generation App

APPLE_GST = 0.12
ORANGE_GST = 0.05

buyer_name = input("Enter Buyer Name: ")

apple_price_kg = int(input("Enter Apple price per kg: "))
apple_quantity_kg = float(input("Enter Apple Quantity in kg: "))

orange_price_kg = int(input("Enter Orange price per kg: "))
orange_quantity_kg = float(input("Enter Orange Quantity in kg: "))

total_price_apple = apple_price_kg * apple_quantity_kg
total_price_orange = orange_price_kg * orange_quantity_kg

total_gst_apple = total_price_apple * APPLE_GST
total_gst_orange = total_price_orange * ORANGE_GST

total_billing_apple = total_price_apple + total_gst_apple
total_billing_orange = total_price_orange + total_gst_orange

total_amount = total_billing_apple + total_billing_orange
total_round_amount = round(total_amount)

print(f"\nBuyer Name: {buyer_name}")
print("-" * 74)

print(f"| {'Item Code':^10} | {'Price/Unit':^10} | {'# Unit':^6} | {'Price':^10} | {'GST':^10} | {'Total w/ GST':^10} |")

print("-" * 74)

print(f"| {'Apple':^10} | {('Rs ' + str(apple_price_kg)):^10} | {apple_quantity_kg:^6} | {('Rs ' + str(total_price_apple)):^10} | {('Rs ' + str(total_gst_apple)):^10} | {('Rs ' + str(total_billing_apple)):^12} |")

print(f"| {'Orange':^10} | {('Rs ' + str(orange_price_kg)):^10} | {orange_quantity_kg:^6} | {('Rs ' + str(total_price_orange)):^10} | {('Rs ' + str(total_gst_orange)):^10} | {('Rs ' + str(total_billing_orange)):^12} |")

print("-" * 74)
print(f"Total{' ' * 54}{total_amount:.2f}")
print(f"Total Round{' ' * 54}{total_round_amount:.2f}")
print("-" * 74)