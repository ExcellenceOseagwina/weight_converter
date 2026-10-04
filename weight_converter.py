weight = int(input("Enter Your Weight: "))
weight_unit = input("Weight in Lbs(L) or Kg(K): ")

# To convert weight in Lbs (L) which is also pounds to Kilograms - Kg(K).
# Kg is the unit of Kilogram.
if weight_unit.upper() == "L":
                 converted_weight = weight * 0.454
                 print(f"Your weight is {converted_weight} Kg")
                 
# To convert weight in Kg(K) which is kilogram to Pounds - Lbs(L). 
# lbs is the unit of Pounds.
elif weight_unit.upper() == "K":
                 converted_weight = weight / 0.454
                 print(f"Your weight is {converted_weight} Lbs")
                 
# If the inputted unit is in neither Kg(K) or Lbs(L) or not any supported unit like Tons, show error 
else:
                 print(f"Error: {weight_unit.upper()} is not a unit or supported unit.\n please enter the correct unit or supported unit in Lbs(l) or Kg(k)")