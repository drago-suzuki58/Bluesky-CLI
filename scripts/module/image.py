# This module can be used to convert an image to ASCII art and RGB colorize it.

from bs4 import BeautifulSoup
import re
import ascii_magic

def ascii(image, image_columns):
    ascii_image = ascii_magic.from_url(image)
    ascii_html = ascii_image.to_html(columns=image_columns)
    return extract_colorcode(ascii_html)

def extract_colorcode(html):
    soup = BeautifulSoup(html, 'html.parser')
    color_text_pairs = []

    for tag in soup.find_all(['span', 'br']):
        if tag.name == 'br':
            color_text_pairs.append(('\n', ''))
            continue

        style = tag.get('style')
        if style:
            color = re.search(r'color: #([A-Fa-f0-9]{6})', style)
            if color:
                color_text_pairs.append((color.group(1), tag.text))

    return color_text_pairs

def hex_color_to_ansi(s, hex_color):
    hex_color = hex_color.lstrip('#')
    r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    return f'\033[38;2;{r};{g};{b}m{s}\033[0m'

def colorize_html(html):
    color_text_pairs = extract_colorcode(html)
    result = ""
    for hex_color, text in color_text_pairs:
        if hex_color == '\n':
            result += '\n'
        else:
            result += hex_color_to_ansi(text, hex_color)
    return result