import unittest
import basetest

class TestUsers(basetest.BaseTestCase):

    def test_get_users(self):
        fields = ["birthdate", "location", "author.fullName",
            "author.iconUrl"]
        attrs = self.field_args(fields)
        attrs['count'] = 2
        content = self.api.get("User/recent", attrs)
        self.assertTrue(content["success"])

    def test_update_status(self):
        status = "Python Client test %s" % self.test_id
        status_fields = {
                "statusMessage": status
                }
        content = self.api.put("User", status_fields)
        self.assertTrue(content["success"])

        fields = ["statusMessage"]
        attrs = self.field_args(fields)
        content = self.api.get("User", attrs)
        self.assertTrue(content["success"])
        self.assertEqual(status, content["entry"]["statusMessage"],
            "Status did not set properly: '%s' != '%s'" %
            (status, content["entry"]["statusMessage"]))


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestUsers)


if __name__ == '__main__':
    unittest.main()
