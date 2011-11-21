import unittest
import basetest


class TestListers(basetest.BaseTestCase):

    ITERATE_SIZE = 20

    def test_blog_post_recent(self):
        from ningapi.access import BlogPostAccessor
        lister = BlogPostAccessor(self.api)
        for blog_post in lister.list_recent(self.ITERATE_SIZE):
            self.assertIsNotNone(blog_post.title)

    def test_photo_recent(self):
        from ningapi.access import PhotoAccessor
        lister = PhotoAccessor(self.api)
        for photo in lister.list_recent(self.ITERATE_SIZE):
            self.assertIsNotNone(photo.title)

    def test_network_alpha(self):
        from ningapi.access import NetworkAccessor
        lister = NetworkAccessor(self.api)
        for network in lister.list_alpha(self.ITERATE_SIZE):
            self.assertIsNotNone(network.name)

    def test_user_alpha(self):
        from ningapi.access import UserAccessor
        lister = UserAccessor(self.api)
        for user in lister.list_alpha(self.ITERATE_SIZE):
            self.assertIsNotNone(user.full_name)

    def test_user_recent(self):
        from ningapi.access import UserAccessor
        lister = UserAccessor(self.api)
        for user in lister.list_recent(self.ITERATE_SIZE):
            self.assertIsNotNone(user.full_name)

    def test_friend_recent(self):
        from ningapi.access import FriendAccessor
        lister = FriendAccessor(self.api)
        for friend in lister.list_recent(self.ITERATE_SIZE):
<<<<<<< HEAD
            self.assertIsNotNone(friend.author)

    def test_friend_alpha(self):
        from ningapi.access import FriendAccessor
        lister = FriendAccessor(self.api)
        for friend in lister.list_alpha(self.ITERATE_SIZE):
            self.assertIsNotNone(friend.author)
=======
            self.assertIsNotNone(friend.friend)
>>>>>>> a7d936dfff1a9fd9d535a09d7501dc942592713a


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestListers)


if __name__ == '__main__':
    unittest.main()
