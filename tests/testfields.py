import unittest
import basetest

from ningapi import NingError
from ningapi.types import Activity, BlogPost, Photo, User


class FieldsBaseTest(basetest.BaseTestCase):
    endpoint = None
    field_names = None

    def __init__(self, field_name):
        super(FieldsBaseTest, self).__init__()
        self.field_name = field_name

    def runTest(self):
        fields = [self.field_name]
        attrs = self.field_args(fields)

        try:
            content = self.api.get(self.endpoint, attrs)
        except NingError, e:
            if (e.error_code == 4 and e.error_subcode == 1):
                self.fail("'%s' does not accept field: '%s'" % (self.endpoint,
                    self.field_name))

        self.assertTrue(content["success"])
        entry = content['entry'][0]
        self.assertIn(self.field_name, entry,
            "Response should contain '%s' field but found: %s" % (
            self.field_name, ", ".join(entry.keys())))


class TestActivityFields(FieldsBaseTest):
    endpoint = "Activity/recent"
    field_names = Activity.field_map.keys()


class TestBlogFields(FieldsBaseTest):
    endpoint = "BlogPost/recent"
    field_names = BlogPost.field_map.keys()


class TestPhotoFields(FieldsBaseTest):
    endpoint = "Photo/recent"
    field_names = Photo.field_map.keys()


class TestUserFields(FieldsBaseTest):
    endpoint = "User/recent"
    field_names = User.field_map.keys()


def build_suite(test_class):
    """Build a test suite for the given class"""
    suite = unittest.TestSuite()
    suite.addTests(test_class(field_name) for field_name in
        test_class.field_names)
    return suite


def load_tests(loader, tests, pattern):
    test_classes = (TestActivityFields, TestBlogFields, TestPhotoFields,
        TestUserFields)

    suite = unittest.TestSuite()
    for test_class in test_classes:
        suite.addTests(build_suite(test_class))
    return suite
