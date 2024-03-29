def weight_conversion (weight , unit):
    if unit == "kg":
        result = weight * 2.2
    else: 
        result = weight * 0.453
    return result

def length_conversion ( length , unit):
    if unit == "m":
        result = length * 3.28
    else:
        result = length * 0.30
    return result

print (" please enter 1 for weight, 2 for length: ")
option= input()
option = int(option)

if option == 1:
    print(" please enter weight number: ")
    weight = input()
    weight = float(weight)
    
    print(" please enter unit kg or lb: ")
    unit = input()
    unit = unit.strip().lower()
    final_weight = weight_conversion (weight , unit)
    print ("weight after conversion is {}." .format(final_weight))

elif option == 2:
    print(" please enter length number: ")
    length = input()
    length = float(length)

    print(" please enter unit m or ft: ")
    unit = input()
    unit = unit.strip().lower()

    final_length = length_conversion ( length , unit)
    print (" length after conversion is {}." .format(final_length))

else:
    print ( " please try again ")