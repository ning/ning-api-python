import random
import oauth2 as oauth
import unittest
import ningapi
from config import TestConfig


class BaseTestCase(unittest.TestCase):
    test_id = None

    def setUp(self):
        consumer = oauth.Consumer(
                key=TestConfig.CONSUMER_KEY,
                secret=TestConfig.CONSUMER_SECRET)
        token = oauth.Token(
                key=TestConfig.ACCESS_KEY,
                secret=TestConfig.ACCESS_SECRET)

        host = TestConfig.HOST
        network = TestConfig.SUBDOMAIN

        self.api = ningapi.Client(host, network, consumer, token)

        self.test_id = random.randint(1, 99)

    def tearDown(self):
        self.api = None

    def field_args(self, fields):
        return {"fields": ",".join(fields)}
