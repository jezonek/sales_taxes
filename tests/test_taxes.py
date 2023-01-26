from ..sales_taxes.taxes import Tax, Product, Collection
import math


class TestProduct:
    def test_book(self):
        book = Product(quantity=1, name="book", price_net=12.49)
        assert isinstance(book.price_gross, float)
        assert round(book.price_gross, 2) == round(12.49, 2)

    def test_cd(self):
        cd = Product(quantity=1, name="music CD", price_net=14.99)
        assert round(cd.price_gross, 2) == round(16.49, 2)

    def test_chocolade(self):
        chocolade = Product(quantity=1, name="chocolate bar", price_net=0.85)
        assert round(chocolade.price_gross, 2) == round(0.85, 2)

    def test_imported_chocolade(self):
        chocolade = Product(
            quantity=1, name="imported box of chocolates", price_net=10.00
        )
        assert round(chocolade.price_gross, 2) == round(10.50, 2)

    def test_imported_perfumes(self):
        perfumes = Product(
            quantity=1, name="imported bottle of perfume", price_net=47.50
        )
        assert round(perfumes.price_gross, 2) == round(54.65, 2)

    def test_perfumes(self):
        perfumes = Product(quantity=1, name="bottle of perfume", price_net=18.99)
        assert round(perfumes.price_gross, 2) == round(20.89, 2)

    def test_headache_pills(self):
        perfumes = Product(quantity=1, name="packet of headache pills", price_net=9.75)
        assert round(perfumes.price_gross, 2) == round(9.75, 2)

    def test_first_bunch(self):
        test_book = Product(quantity=1, name="book", price_net=12.49)
        test_cd = Product(quantity=1, name="music CD", price_net=14.99)
        test_chocolade = Product(quantity=1, name="chocolate bar", price_net=0.85)
        assert round(
            test_book.tax_amount + test_cd.tax_amount + test_chocolade.tax_amount, 2
        ) == round(1.50, 2)
        assert round(
            test_book.price_gross + test_cd.price_gross + test_chocolade.price_gross, 2
        ) == round(29.83, 2)

    def test_second_bunch(self):
        test_ch = Product(
            quantity=1, name="imported box of chocolates", price_net=10.00
        )
        test_perfume = Product(
            quantity=1, name="imported bottle of perfume", price_net=47.50
        )
        assert round(test_ch.tax_amount + test_perfume.tax_amount, 2) == round(7.65, 2)
        assert round(test_ch.price_gross + test_perfume.price_gross, 2) == round(
            65.15, 2
        )

    def test_third_bunch(self):
        test_1 = Product(quantity=1, name="imported bottle of perfume", price_net=27.99)
        test_2 = Product(quantity=1, name="bottle of perfume", price_net=18.99)
        test_3 = Product(quantity=1, name="packet of headache pills", price_net=9.75)
        test_4 = Product(quantity=1, name="box of imported chocolates", price_net=11.25)
        assert round(
            test_1.tax_amount
            + test_2.tax_amount
            + test_3.tax_amount
            + test_4.tax_amount,
            2,
        ) == round(6.70, 2)
        assert round(
            test_1.price_gross
            + test_2.price_gross
            + test_3.price_gross
            + test_4.price_gross,
            2,
        ) == round(74.68, 2)


class TestCollection:
    def test_collection_a(self):
        test_book = Product(quantity=1, name="book", price_net=12.49)
        test_cd = Product(quantity=1, name="music CD", price_net=14.99)
        test_chocolade = Product(quantity=1, name="chocolate bar", price_net=0.85)

        test_collection = Collection([test_book, test_cd, test_chocolade])
        assert test_collection.tax() == round(1.50, 2)
        assert test_collection.price_gross() == round(29.83, 2)

    def test_collection_b(self):
        test_ch = Product(
            quantity=1, name="imported box of chocolates", price_net=10.00
        )
        test_perfume = Product(
            quantity=1, name="imported bottle of perfume", price_net=47.50
        )
        test_collection = Collection([test_ch, test_perfume])
        assert test_collection.tax() == round(7.65, 2)
        assert test_collection.price_gross() == round(65.15, 2)

    def test_collection_c(self):
        test_1 = Product(quantity=1, name="imported bottle of perfume", price_net=27.99)
        test_2 = Product(quantity=1, name="bottle of perfume", price_net=18.99)
        test_3 = Product(quantity=1, name="packet of headache pills", price_net=9.75)
        test_4 = Product(quantity=1, name="box of imported chocolates", price_net=11.25)
        test_collection = Collection([test_1, test_2, test_3, test_4])
        assert test_collection.tax() == round(6.70, 2)
        assert test_collection.price_gross() == round(74.68, 2)

    def test_empty_collection(self):
        test_collection = Collection([])
        assert test_collection.tax() == 0
        assert test_collection.price_gross() == 0
