import unittest
import adshopcart_methods as methods


class AdshopcartPositiveTestCases(unittest.TestCase):

    @staticmethod
    def test_advantage_shopping():
        methods.setUp()
        methods.create_new_user()
        methods.name_and_cart()
        methods.log_out_log_in()
        methods.delete_account_retry_login()
        methods.product_check()
        methods.top_checks()
        methods.contact_section()
        methods.tearDown()