import random
battery = 100.0

for waypoint in range(1, 11):
    battery_loss = random.uniform(1.5, 3.5)
    battery -= battery_loss
    print(f"Waypoint {waypoint}: Battery level is at {battery:.2f} % (Lost: {battery_loss:.2f} % )")
    
    if battery < 75.0:
        print("[EMERGENCY RETURN TRIGGERED]")
        break   
    elif battery < 80.0:
        print("Caution: Battery has dropped below 80%")