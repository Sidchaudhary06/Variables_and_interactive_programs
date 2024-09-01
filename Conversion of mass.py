LOTS_TO_GRAMS = 13.3
POUNDS_TO_LOTS = 32
TALENTS_TO_POUNDS = 20
GRAMS_IN_KG = 1000

talents = int(input("Enter the mass in talents (leiviskä): "))
pounds = int(input("Enter the mass in pounds (naula): "))
lots = int(input("Enter the mass in lots (luoti): "))

total_lots = (talents * TALENTS_TO_POUNDS * POUNDS_TO_LOTS) + (pounds * POUNDS_TO_LOTS) + lots

total_grams = total_lots * LOTS_TO_GRAMS

kilograms = int(total_grams // GRAMS_IN_KG)
grams = total_grams % GRAMS_IN_KG

print(f"The mass is {kilograms} kilograms and {grams:.2f} grams.")
