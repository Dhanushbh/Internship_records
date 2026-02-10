import random

print("🎮 === RoboController 1.0 (Console Game) === 🎮\n")

# Inputs
robot_name = input("Enter robot name: ")
boat_name = input("Enter boat name: ")
target_distance = int(input("Enter target distance (meters): "))

distance_travelled = 0
checkpoints = []

directions = ["up", "down", "left", "right"]

print("\nGame Started! Control the robot using: up / down / left / right\n")

# Obstacle loop (game loop)
while distance_travelled < target_distance:
    move = input("Your move (up/down/left/right): ").lower()

    if move not in directions:
        print("❌ Invalid move! Try again.")
        continue

    # Random obstacle
    obstacle = random.choice([True, False])

    # Nested if for wall handling
    if obstacle:
        print("🚧 Obstacle ahead!")
        speed = 2

        wall = random.choice([True, False])
        if wall:
            print("🧱 Wall detected! Direction changed.")
            move = random.choice(directions)
            print("➡ New direction:", move)
    else:
        if distance_travelled < target_distance // 2:
            speed = 6
            print("✅ Clear path, moving fast.")
        else:
            speed = 3
            print("⚠ Near target, moving carefully.")

    distance_travelled += speed
    checkpoints.append(move)

    print(f"🤖 {robot_name} moved {move} by {speed}m")
    print(f"📏 Total distance: {distance_travelled}/{target_distance} meters")

    # Random unexpected direction change
    if random.choice([True, False]):
        rand_dir = random.choice(directions)
        checkpoints.append(rand_dir)
        print("🔄 Unexpected turn:", rand_dir)

    # Option to remove checkpoint
    remove_cp = input("Remove last checkpoint? (yes/no): ").lower()
    if remove_cp == "yes" and checkpoints:
        removed = checkpoints.pop()
        print("❌ Removed checkpoint:", removed)
n
    print("📍 Checkpoints so far:", checkpoints)
    print("-" * 40)

print("\n🏁 === GAME OVER: TRIP SUMMARY === 🏁")
print(f"🤖 Robot Name      : {robot_name}")
print(f"🚤 Boat Name       : {boat_name}")
print(f"🎯 Target Distance : {target_distance} meters")
print(f"📏 Travelled       : {distance_travelled} meters")
print(f"📍 Final Checkpoints: {checkpoints}")
print("✅ Mission Completed!")
