def main():
 weight = float(input("Weight (kg): "))
 is_active = bool(input("Are you active? (Y/N): ") == "Y")
 water_needed = weight / 30
 if is_active:
    water_needed *= 1.2
 print("Water daily: {:.1f} litres".format(water_needed))
main()