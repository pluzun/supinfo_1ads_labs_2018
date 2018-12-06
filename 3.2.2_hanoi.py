def hanoi(height, from_tower, to_tower, helper_tower):
    if height >= 1:
        hanoi(height - 1, from_tower, helper_tower, to_tower)

        disk = from_tower.pop()
        print("Moving the disk", disk, "from the", from_tower[0], "to the", to_tower[0])
        to_tower.append(disk)
        print(from_tower, to_tower, helper_tower)

        hanoi(height - 1, helper_tower, to_tower, from_tower)

tower_1 = ['tower 1', 6, 5, 4, 3, 2, 1]
hanoi(len(tower_1) - 1, tower_1, ['tower 3'], ['tower 2'])
