import random
import time

print("🎮 === RoboController 1.0 (Terminal Game) === 🎮\n")

# --- User Inputs ---
robot_name = input("Enter robot name: ")

while True:
    try:
        target_distance = int(input("Enter target distance (meters): "))
        break
    except ValueError:
        print("❌ Please enter a valid number (e.g., 50, 100).")

# --- Initial State ---
x, y = 0, 0
distance_travelled = 0
checkpoints = []
directions = ["up", "down", "left", "right"]
current_dir = random.choice(directions)

print("\n🤖 Robot is moving automatically...\n")

# --- Game Loop ---
while distance_travelled < target_distance:
    print("-" * 50)
    print(f"🤖 Robot: {robot_name}")
    print(f"📍 Position: ({x}, {y})")
    print(f"➡ Current Direction: {current_dir}")

    # Obstacle check
    obstacle = random.choice([True, False])
    if obstacle:
        print("🚧 Obstacle detected! Robot slows down.")

    # Movement logic (nested if for wall handling)
    dx, dy = 0, 0
    if current_dir == "up":
        dx = 1
    elif current_dir == "down":
        dx = -1
    elif current_dir == "left":
        dy = -1
    elif current_dir == "right":
        dy = 1

    # Wall detection
    wall = random.choice([True, False])
    if wall:
        print("🧱 Wall found! Changing direction automatically...")
        current_dir = random.choice(directions)
        print(f"➡ New direction: {current_dir}")
    else:
        x += dx
        y += dy

        # Speed decision (if–elif–else)
        if obstacle:
            speed = 2
        elif distance_travelled < target_distance // 2:
            speed = 6
        else:
            speed = 3

        distance_travelled += speed
        checkpoints.append(current_dir)
        print(f"➡ Robot moved {current_dir.upper()} by {speed} meters")

    print(f"📏 Distance Travelled: {distance_travelled}/{target_distance} m")
    print(f"📌 Checkpoints: {checkpoints}")

    print("⏸ Human pause (2 seconds)...\n")
    time.sleep(2)

# --- Final Summary ---
print("\n🏁 === TRIP SUMMARY === 🏁")
print(f"🤖 Robot Name        : {robot_name}")
print(f"🎯 Target Distance   : {target_distance} meters")
print(f"📏 Total Travelled   : {distance_travelled} meters")
print(f"📌 Final Checkpoints : {checkpoints}")
print("✅ Mission Completed Successfully!")
