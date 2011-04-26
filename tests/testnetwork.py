import unittest
import basetest


class TestNetworks(basetest.BaseTestCase):

    def test_get_networks(self):
        fields = ["id",
                "author",
                "createdDate",
                "subdomain",
                "name",
                "iconUrl",
                "defaultUserIconUrl",
                "blogPostModeration",
                "eventModeration",
                "groupModeration",
                "photoModeration",
                "userModeration",
                "videoModeration",
                "xapiStatus",
                ]
        attrs = self.field_args(fields)
        attrs['count'] = 2
        content = self.api.get("Network/alpha", attrs)
        self.assertTrue(content['success'])


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestNetworks)


if __name__ == "__main__":
    unittest.main()
