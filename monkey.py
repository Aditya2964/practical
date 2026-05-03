monkey_position = "middle"
box_position = "corner"
banana_position = "middle"
monkey_on_box = False
monkey_has_banana = False

print("initial state:")
print(monkey_position, box_position, banana_position, monkey_on_box, monkey_has_banana)

if monkey_position != box_position:
    monkey_position = box_position
    print("Monkey walks to the box.")

if monkey_position == box_position and not monkey_on_box:
    box_position = banana_position
    monkey_position = banana_position
    print("Monkey moves the box under the banana.")

if monkey_position == banana_position and box_position == banana_position:
    monkey_on_box = True
    print("Monkey climbs on the box.")

if monkey_on_box and monkey_position == banana_position:
    monkey_has_banana = True
    print("Monkey grabs the banana.")

print("final state:")
print(monkey_position, box_position, banana_position, monkey_on_box, monkey_has_banana)

    