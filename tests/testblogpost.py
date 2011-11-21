import unittest
import basetest


class TestBlogPosts(basetest.BaseTestCase):

    def test_get_blog_posts(self):
        fields = ["title", "description", "author.fullName", "author.iconUrl"]
        attrs = self.field_args(fields)
        attrs['count'] = 2
        content = self.api.get("BlogPost/recent", attrs)
        self.assertTrue(content["success"])

    def test_create_blog_post(self):
        blog_fields = [
            ("title", "BlogPost %s" % self.test_id),
            ("description", "Python Client test %s" % self.test_id),
            ("tag", "chicken farm"),
            ("tag", "cats")]

        content = self.api.post("BlogPost", blog_fields)
        self.assertTrue(content["success"])

    def test_update_blog_post(self):
        blog_title = "BlogPost %s" % self.test_id
        blog_desc = "Python Client update test %s" % self.test_id

        # Create a test blog post
        blog_fields = {
                "title": blog_title,
                "description": blog_desc,
                "tag": "tests",
                }
        content = self.api.post("BlogPost", blog_fields)
        self.assertTrue(content["success"])
        blog_id = content["id"]

        # Update the blog post
        blog_fields = [
                ("id", blog_id),
                ("title", "Updated %s" % blog_title),
                ("description", "Updated %s" % blog_desc),
                ("tag", "new tag")]
        content = self.api.put("BlogPost", blog_fields)
        self.assertTrue(content["success"])

    def test_delete_blog_post(self):
        blog_title = "BlogPost %s" % self.test_id
        blog_desc = "Python Client test %s" % self.test_id

        # Create a test blog post
        blog_fields = {
                "title": blog_title,
                "description": blog_desc,
                "tag": "tests",
                }
        content = self.api.post("BlogPost", blog_fields)
        self.assertTrue(content["success"])
        blog_id = content["id"]

        content = self.api.delete("BlogPost", {"id": blog_id})
        self.assertTrue(content["success"])


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestBlogPosts)


if __name__ == '__main__':
    unittest.main()
