import unittest
import basetest


class TestUsers(basetest.BaseTestCase):

    def test_get_users(self):
        fields = ["email", "birthdate", "location", "author.fullName",
            "author.iconUrl"]
        attrs = self.field_args(fields)
        attrs['count'] = 2
        content = self.api.get("User/recent", attrs)
        self.assertTrue(content["success"])

    def test_update_status(self):
        status_fields = {
                "statusMessage": "Python Client test %s" % self.test_id
                }
        content = self.api.put("User", status_fields)
        self.assertTrue(content["success"])


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestUsers)


if __name__ == '__main__':
    unittest.main()
