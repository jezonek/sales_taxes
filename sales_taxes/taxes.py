from enum import Enum
from dataclasses import dataclass, field
from .utils import round_up_tax
from math import fsum


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
            self.tax_amount = round_up_tax(
                self.price_net * (TAX_AMOUNT_MAP[self.category] + 0.05)
            )

        else:
            self.tax_amount = round_up_tax(
                self.price_net * TAX_AMOUNT_MAP[self.category]
            )

    def set_price_gross(self) -> None:
        self.price_gross = fsum([self.price_net, self.tax_amount])

    def __post_init__(self):
        self.set_category()
        self.set_is_imported()
        self.set_tax_amount()
        self.set_price_gross()


@dataclass
class Collection:
    objects: list = []

    @property
    def objects(self):
        return self._objects

    @objects.setter
    def objects(self, initial):
        assert isinstance(initial, list)

        for obj in initial:
            assert isinstance(obj, Product)

        self._objects = initial

    def tax(self):
        if not self._objects:
            return 0
        return round(sum([x.tax_amount for x in self.objects]), 2)

    def price_gross(self):
        if not self._objects:
            return 0
        return round(sum([x.price_gross for x in self.objects]), 2)

    def add(self, new_obj: Product):
        assert isinstance(new_obj, Product)
        self._objects.append(new_obj)
