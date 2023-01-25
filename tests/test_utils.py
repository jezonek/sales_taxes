from ..sales_taxes.utils import parse_one_line


def test_parse_one_line():
    test_data = [
        ("1 book at 12.49", 1, "book", 12.49),
        ("1 music CD at 14.99", 1, "music CD", 14.99),
        ("1 chocolate bar at 0.85", 1, "chocolate bar", 0.85),
        (
            "1 imported box of chocolates at 10.00",
            1,
            "imported box of chocolates",
            10.00,
        ),
        (
            "1 imported bottle of perfume at 47.50",
            1,
            "imported bottle of perfume",
            47.50,
        ),
        (
            "1 imported bottle of perfume at 27.99",
            1,
            "imported bottle of perfume",
            27.99,
        ),
        ("1 bottle of perfume at 18.99", 1, "bottle of perfume", 18.99),
        ("1 packet of headache pills at 9.75", 1, "packet of headache pills", 9.75),
        (
            "1 box of imported chocolates at 11.25",
            1,
            "box of imported chocolates",
            11.25,
        ),
    ]
    for data in test_data:
        assert parse_one_line(data[0]) == (data[1], data[2], data[3])
