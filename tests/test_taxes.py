from ..sales_taxes.taxes import Tax, Product


class TestProduct:
    def test_book(self):
        book = Product(quantity=1, name="book", price_net=12.49)
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
