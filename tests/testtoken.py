import unittest
import basetest

from config import TestConfig


class TestToken(basetest.BaseTestCase):

    def test_create_token(self):
        token = self.api.login(TestConfig.EMAIL, TestConfig.PASSWORD)
        self.assertTrue(token.key)
        self.assertTrue(token.secret)


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestToken)


if __name__ == '__main__':
    unittest.main()
