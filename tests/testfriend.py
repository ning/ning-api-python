import unittest
import basetest


class TestFriends(basetest.BaseTestCase):

    def test_get_friends_recent(self):
        fields = ["friend", "author", "state", "createdDate", "updatedDate"]
        attrs = self.field_args(fields)
        attrs['count'] = 5
        content = self.api.get("Friend/recent", attrs)
        self.assertTrue(content["success"])

    def test_get_friends_alpha(self):
        fields = ["friend", "author", "state", "createdDate", "updatedDate"]
        attrs = self.field_args(fields)
        attrs['count'] = 5
        content = self.api.get("Friend/alpha", attrs)
        self.assertTrue(content["success"])


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestFriends)


if __name__ == '__main__':
    unittest.main()
