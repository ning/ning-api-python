import unittest
import basetest


class TestTags(basetest.BaseTestCase):

    def test_get_tags(self):
        # Create a test blog post
        blog_title = "BlogPost %s" % self.test_id
        blog_desc = "Python Client update test %s" % self.test_id

        blog_fields = {
                "title": blog_title,
                "description": blog_desc,
                "tag": "tests",
                }
        content = self.api.post("BlogPost", blog_fields)
        self.assertTrue(content["success"])
        blog_id = content["id"]

        # check the tags on the blog post
        attrs = {
                 'count': 2,
                 'attachedTo': blog_id
        }
        content = self.api.get("Tag/list", attrs)
        self.assertTrue(content["success"])


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestTags)


if __name__ == '__main__':
    unittest.main()
