import unittest
import basetest


class TestPhotos(basetest.BaseTestCase):

    def test_get_photos(self):
        fields = ["title", "description", "author.fullName", "author.iconUrl"]
        attrs = self.field_args(fields)
        attrs['count'] = 2
        content = self.api.get("Photo/recent", attrs)
        self.assertTrue(content["success"])

    def test_create_photo(self):
        photo_title = "Photo %s" % self.test_id
        photo_desc = "Python Client test %s" % self.test_id
        photo_path = "/Users/devin/Pictures/nasa/NASA-23.jpg"
        photo_content_type = "image/jpeg"

        photo_fields = {
                "title": photo_title,
                "description": photo_desc,
                "file": photo_path,
                "content_type": photo_content_type
                }
        content = self.api.post("Photo", photo_fields)
        self.assertTrue(content["success"])

    def test_update_photo(self):
        photo_title = "Photo %s" % self.test_id
        photo_desc = "Python Client test %s" % self.test_id
        photo_file = "/Users/devin/Pictures/nasa/NASA-23.jpg"
        photo_content_type = "image/jpeg"

        photo_fields = {
                "title": photo_title,
                "description": photo_desc,
                "file": photo_file,
                "content_type": photo_content_type
                }
        content = self.api.post("Photo", photo_fields)
        self.assertTrue(content["success"])
        photo_id = content["id"]

        photo_fields = {
                "id": photo_id,
                "title": "Updated %s" % photo_title,
                "description": "Updated %s" % photo_desc,
                }
        content = self.api.put("Photo", photo_fields)
        self.assertTrue(content["success"])

    def test_delete_photo(self):
        photo_title = "Photo %s" % self.test_id
        photo_desc = "Python Client test %s" % self.test_id
        photo_file = "/Users/devin/Pictures/nasa/NASA-23.jpg"
        photo_content_type = "image/jpeg"

        photo_fields = {
                "title": photo_title,
                "description": photo_desc,
                "file": photo_file,
                "content_type": photo_content_type
                }
        content = self.api.post("Photo", photo_fields)
        self.assertTrue(content["success"])
        photo_id = content["id"]

        content = self.api.delete("Photo", {"id": photo_id})
        self.assertTrue(content["success"])


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestPhotos)


if __name__ == '__main__':
    unittest.main()
