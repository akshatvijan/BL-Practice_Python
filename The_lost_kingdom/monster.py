def choose_monster():
    monsters = [
        ["Goblin", 100, 20, 50],
        ["Dragon", 500, 80, 500],
        ["Orc", 250, 40, 150],
        ["Troll", 350, 60, 300]
    ]
    print(f"Choose a monster")
    print("Goblin")
    print("Dragon")
    print("Orc")
    print("Troll")

    mons=input("enter monster name")
    if mons=="Goblin":
        reward=monsters[0][3]
        health=monsters[0][1]
        attack=monsters[0][2]
        score=reward+(health//10)-attack

    elif mons=="Dragon":
        reward=monsters[1][3]
        health=monsters[1][1]
        attack=monsters[1][2]
        score=reward+(health//10)-attack

    elif mons=="Orc":
        reward=monsters[2][3]
        health=monsters[2][1]
        attack=monsters[2][2]
        score=reward+(health//10)-attack


    elif mons=="Troll":
        reward=monsters[3][3]
        health=monsters[3][1]
        attack=monsters[3][2]
        score=reward+(health//10)-attack

    return score


