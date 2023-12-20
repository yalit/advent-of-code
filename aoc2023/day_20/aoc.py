from python.libraries.utils import lcm


def handle_part_1(lines: list[str]) -> int:
    modules = get_modules(lines)

    total = [0, 0]
    for _ in range(1000):
        pulses = [("button", "broadcaster", 0)]
        while len(pulses) > 0:
            sender, receiver, pulse = pulses.pop(0)
            total[pulse] += 1

            if receiver not in modules or modules[receiver]['type'] is None:
                continue

            if modules[receiver]['type'] == "broadcaster":
                for target in modules[receiver]['targets']:
                    pulses.append((receiver, target, pulse))
                continue

            if modules[receiver]['type'] == '%':
                if pulse:
                    continue

                modules[receiver]['memory'] = 1 - modules[receiver]['memory']
                for target in modules[receiver]['targets']:
                    pulses.append((receiver, target, modules[receiver]['memory']))
                continue

            # module is a &
            modules[receiver]['memory'][sender] = pulse
            if all(p for p in modules[receiver]['memory'].values()):
                for target in modules[receiver]['targets']:
                    pulses.append((receiver, target, 0))
            else:
                for target in modules[receiver]['targets']:
                    pulses.append((receiver, target, 1))

    return total[0] * total[1]


def handle_part_2(lines: list[str]) -> int:
    modules = get_modules(lines)

    if len([m for m in modules.values() if 'rx' in m['targets']]) == 0:
        print("no rx in test input")
        return 0

    button_press = 0
    # assumption, only one module that input value to rx (verified in the input)
    (input_to_rx,) = [module['name'] for module in modules.values() if 'rx' in module['targets']]

    # assumption, is that module is a "conjunction module" and so we'll check on the values sent to that conjunction
    # module to see how long it takes for them to send a high pulse to the input of rx
    # and then take the lcm of them to see when it's possible that they will be all sending a high pulse to the input of rx
    input_of_input_of_rx = {module['name']: 0 for module in modules.values() if input_to_rx in module['targets']}

    while not found:
        button_press += 1
        pulses = [("button", "broadcaster", 0)]

        while len(pulses) > 0:
            sender, receiver, pulse = pulses.pop(0)

            if receiver not in modules or modules[receiver]['type'] is None:
                continue

            if receiver == input_to_rx and pulse:
                if input_of_input_of_rx[sender] == 0:
                    input_of_input_of_rx[sender] = button_press
                else:  # to verify the assumption that it's not hitting more than once with a high pulse for each button press
                    print(
                        "Issue : " + sender + " hitting " + receiver + " more than once during a cycle of button press with a high pulse")
                    exit()

            if modules[receiver]['type'] == "broadcaster":
                for target in modules[receiver]['targets']:
                    pulses.append((receiver, target, pulse))
                continue

            if modules[receiver]['type'] == '%':
                if pulse:
                    continue

                modules[receiver]['memory'] = 1 - modules[receiver]['memory']
                for target in modules[receiver]['targets']:
                    pulses.append((receiver, target, modules[receiver]['memory']))
                continue

            # module is a &
            modules[receiver]['memory'][sender] = pulse
            if all(p for p in modules[receiver]['memory'].values()):
                for target in modules[receiver]['targets']:
                    pulses.append((receiver, target, 0))
            else:
                for target in modules[receiver]['targets']:
                    pulses.append((receiver, target, 1))

        if all(x != 0 for x in input_of_input_of_rx.values()):
            break

    return lcm(*input_of_input_of_rx.values())


# module is in form (<name>, <type> None / % / &, state = or the value of it or the values of all the inputs, receivers)
# 0 is off/low & 1 is on/high
def get_modules(lines) -> dict[
                          str: dict['name': str, 'type': str, 'memory': str | dict[str: int], 'targets': list[str]]]:
    modules: dict[str: dict['name': str, 'type': str, 'memory': str | dict[str: int], 'targets': list[str]]] = {}

    for line in lines:
        sender, _ = line.split(' -> ')

        if sender not in modules:
            modules[get_module_name(sender)] = init_module(sender)

    for line in lines:
        sender, receivers = line.split(' -> ')

        for receiver_full_name in receivers.split(', '):
            receiver = get_module_name(receiver_full_name)
            modules[get_module_name(sender)]['targets'].append(receiver)
            if receiver not in modules:
                continue
            if modules[receiver]['type'] == '&':
                modules[receiver]['memory'][get_module_name(sender)] = 0

    return modules


def get_module_name(module):
    return module[1:] if module[0] in ['&', '%'] else module


def init_module(module):
    if module[0] in ['&', '%']:
        return {'name': get_module_name(module), 'type': module[0], 'memory': {} if module[0] == '&' else 0,
                'targets': []}

    return {'name': get_module_name(module), 'type': "broadcaster" if module == "broadcaster" else None, 'memory': 0,
            'targets': []}
