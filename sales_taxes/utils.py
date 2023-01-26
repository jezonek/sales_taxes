import re


def parse_one_line(line):
    pattern = r"(?P<quantity>\d+) (?P<product>(\w+| )+) at (?P<price>\d+\.\d+)"
    match = re.match(pattern, line)
    return int(match["quantity"]), match["product"], float(match["price"])


def round_up_tax(x):
    """Function to round up float number in financial way (For tax purpose)
    It rounds up number always up, to whole 0.05 part.


    Args:
        x (float): Number to be rounded up

    Returns:
        float: Same number rounded up financial way
    """
    number_as_str = format(round(x, 2), ".2f")
    tax_round_up_map = {
        0: (0, 0),
        1: (0, 4),
        2: (0, 3),
        3: (0, 2),
        4: (0, 1),
        5: (0, 0),
        6: (1, -6),
        7: (1, -7),
        8: (1, -8),
        9: (1, -9),
    }

    matched_appendix = tax_round_up_map[int(number_as_str[-1])]
    return x + (matched_appendix[0] * 0.1) + (matched_appendix[1] * 0.01)
