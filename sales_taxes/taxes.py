from enum import Enum
from dataclasses import dataclass, field
from .utils import round_nearest, round_down


class Tax(Enum):
    BOOKS = 1
    FOOD = 2
    MEDICAL_PRODUCT = 3
    REST = 4


TAX_AMOUNT_MAP = {Tax.BOOKS: 0, Tax.FOOD: 0, Tax.MEDICAL_PRODUCT: 0, Tax.REST: 0.1}

CATEGORY_KEYWORDS = {
    Tax.BOOKS: ["book"],
    Tax.FOOD: ["chocolate"],
    Tax.MEDICAL_PRODUCT: ["headache pills"],
}


@dataclass
class Product:
    quantity: int
    name: str
    price_net: float
    category: Tax = field(init=False)
    is_imported: bool = field(init=False)
    tax_amount: float = field(init=False)
    price_gross: float = field(init=False)

    def set_category(self) -> None:
        self.category = Tax.REST

        for category in CATEGORY_KEYWORDS:
            print(category)
            for keyword in CATEGORY_KEYWORDS[category]:
                if keyword in self.name:
                    self.category = category

    def set_is_imported(self) -> None:
        if "imported" in self.name:
            self.is_imported = True
        else:
            self.is_imported = False

    def set_tax_amount(self) -> None:
        if self.is_imported:
            self.tax_amount = round_nearest(
                self.price_net * (TAX_AMOUNT_MAP[self.category] + 0.05),
                0.05,
            )
        else:
            self.tax_amount = round_nearest(
                self.price_net * TAX_AMOUNT_MAP[self.category], 0.05
            )

    def set_price_gross(self) -> None:
        self.price_gross = self.price_net + self.tax_amount

    def __post_init__(self):
        self.set_category()
        self.set_is_imported()
        self.set_tax_amount()
        self.set_price_gross()
