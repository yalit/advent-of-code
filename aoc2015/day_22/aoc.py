def handle_part_1(lines: list[str], hard = False) -> int:
    player_health, player_mana = int(lines[0].split()[1]), int(lines[0].split()[3])
    boss_health, boss_damage = int(lines[1].split()[1]), int(lines[1].split()[3])

    state = (player_health, player_mana, boss_health, 0, 0, 0, 0, 0)  # player_hit, player_mana, player_armor, boss_hit, shield_timer, poison_timer, recharge_timer, mana_spent, turn
    to_visit = [state]

    least_amount_spent = float('inf')
    while to_visit:
        player_health, player_mana, boss_health, shield_timer, poison_timer, recharge_timer, mana_spent, turn = to_visit.pop()

        if boss_health <= 0:
            least_amount_spent = min(least_amount_spent, mana_spent)
            continue

        if mana_spent >= least_amount_spent:
            continue

        if player_health <= 0:
            continue

        player_armor = 0 if shield_timer == 0 else 7
        shield_timer = max(0, shield_timer - 1)

        if poison_timer > 0:
            boss_health -= 3
        poison_timer = max(0, poison_timer - 1)

        if recharge_timer > 0:
            player_mana += 101
        recharge_timer = max(0, recharge_timer - 1)

        if turn % 2 == 0: # Player's turn
            if hard:
                player_health -= 1
                if player_health <= 0:
                    continue

            if player_mana >= 53:
                to_visit.append((player_health, player_mana - 53, boss_health - 4, shield_timer, poison_timer, recharge_timer, mana_spent + 53, turn + 1))

            if player_mana >= 73:
                to_visit.append((player_health + 2, player_mana - 73, boss_health - 2, shield_timer, poison_timer, recharge_timer, mana_spent + 73, turn + 1))

            if player_mana >= 113 and shield_timer == 0:
                to_visit.append((player_health, player_mana - 113, boss_health, 6, poison_timer, recharge_timer, mana_spent + 113, turn + 1))

            if player_mana >= 173 and poison_timer == 0:
                to_visit.append((player_health, player_mana - 173, boss_health, shield_timer, 6, recharge_timer, mana_spent + 173, turn + 1))

            if player_mana >= 229 and recharge_timer == 0:
                to_visit.append((player_health, player_mana - 229, boss_health, shield_timer, poison_timer, 5, mana_spent + 229, turn + 1))

        else: # Boss's turn
            damage = max(1, boss_damage - player_armor)
            to_visit.append((player_health - damage, player_mana, boss_health, shield_timer, poison_timer, recharge_timer, mana_spent, turn + 1))

    return least_amount_spent


def handle_part_2(lines: list[str]) -> int:
    return handle_part_1(lines, True)
