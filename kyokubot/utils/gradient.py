def hex_to_rgb(hex_color):
    return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))


def rgb_to_ansi(rgb_color):
    return f"\033[38;2;{rgb_color[0]};{rgb_color[1]};{rgb_color[2]}m"


def gradient_text(text, *colors):
    """
    返回字体颜色按顺序渐变的彩色字符串。

    :param text: 输入的字符串
    :param colors: 可变数量的颜色 (hex string, e.g., "ff0000" for red)
    :return: 渐变颜色的字符串
    """
    if len(colors) < 2:
        raise ValueError("至少需要两个颜色来生成渐变效果")

    color_rgbs = [hex_to_rgb(color) for color in colors]

    length = len(text)
    segments = len(color_rgbs) - 1
    segment_length = length // segments

    gradient_str = ""
    for i in range(segments):
        start_rgb = color_rgbs[i]
        end_rgb = color_rgbs[i + 1]

        for j in range(segment_length):
            index = i * segment_length + j
            if index >= length:
                break

            interpolated_rgb = tuple(
                int(start_rgb[k] + (end_rgb[k] - start_rgb[k]) * j / segment_length)
                for k in range(3)
            )
            ansi_color = rgb_to_ansi(interpolated_rgb)
            gradient_str += f"{ansi_color}{text[index]}"

    # 用最后一个颜色处理剩余的字符
    for index in range(segments * segment_length, length):
        ansi_color = rgb_to_ansi(color_rgbs[-1])
        gradient_str += f"{ansi_color}{text[index]}"

    # 在结尾重置字符颜色，防止留尾
    gradient_str += "\033[0m"

    return gradient_str
