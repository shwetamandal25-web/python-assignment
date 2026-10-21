vehicle_type = input("Enter vehicle type: ")
fastag_active = input("Is FASTag active? ")
is_national_holiday = input("Is today a national holiday? ")

if fastag_active == "no":
    print("Double toll penalty applied: cash mode")

elif fastag_active == "yes":

    if is_national_holiday == "yes":
        print("Festive waiver applied: half toll")

    else:
        if vehicle_type == "car":
            print("100 rupees")

        elif vehicle_type == "SUV":
            print("150 rupees")

        elif vehicle_type == "truck":
            print("300 rupees")

        else:
            print("Invalid vehicle category")