from functools import reduce


def handle_part_1(lines: list[str]) -> int:
    width = 25
    height = 6
    layer_length = width * height
    input = list(map(int, lines[0]))
    layers = sorted([(input[i:i+layer_length].count(0), input[i:i+layer_length]) for i in range(0, len(input), layer_length)])

    return layers[0][1].count(1)*layers[0][1].count(2)


def handle_part_2(lines: list[str]) -> int:
    width = 25
    height = 6
    layer_length = width * height
    input = list(map(int, lines[0]))
    layers = [(input[i:i + layer_length].count(0), input[i:i + layer_length]) for i in range(0, len(input), layer_length)]
    digits = [[l[1][i] for l in layers] for i in range(layer_length)]
    def find_color(colors):
        current_color = 2
        a = 0
        while current_color == 2 and a < len(colors):
            current_color = colors[a]
            a+=1
        return current_color

    digit_color = list(map(find_color, digits))
    for i in range(height):
        print("".join(map(lambda a: " " if not a else str(a),digit_color[i*width:(i+1)*width])))
    return 0
