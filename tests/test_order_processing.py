import time

import pytest

from config.config import config
from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.store_page import StorePage


@pytest.mark.usefixtures("driver")
# @pytest.mark.flaky(rerurns=config.RERUN)
class TestOrderProcessing:
    def test_order_product_as_a_guest(self):
        home_page = HomePage(self.driver).open()
        home_page.menu.open_store_page()
        #
        store_page = StorePage(self.driver).wait_for_page_to_load()
        store_page.footer.click_dismiss_button()
        store_page.add_item_to_cart("Belt")
        # time.sleep(5)
        assert store_page.menu.amount() == "65,00"

        home_page.menu.menu_pop_up().go_to_the_cart()
        # cart_page = CartPage(self.driver).wait_for_page_to_load()
        # cart_page.assert_item_data("Belt", "65,00")
