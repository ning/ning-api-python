import unittest
import basetest


class TestActivity(basetest.BaseTestCase):

    def test_get_activity(self):
        fields = ["title", "description", "author.fullName", "author.iconUrl"]
        attrs = self.field_args(fields)
        attrs['count'] = 2
        content = self.api.get("Activity/recent", attrs)
        self.assertTrue(content["success"])


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestActivity)


if __name__ == '__main__':
    unittest.main()
