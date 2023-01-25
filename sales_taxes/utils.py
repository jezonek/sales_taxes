import re
import math


def parse_user_input():
    pass


def parse_one_line(line):
    pattern = r"(?P<quantity>\d+) (?P<product>(\w+| )+) at (?P<price>\d+\.\d+)"
    match = re.match(pattern, line)
    return int(match["quantity"]), match["product"], float(match["price"])


def round_nearest(x, a):
    return int(round(x / a)) * a


def round_down(x, a):
    return math.floor(x / a) * a
