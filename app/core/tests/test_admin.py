from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

# https://www.mlr2d.org/contents/djangorestapi/05_modifying_djangoadmininterface

class AdminSiteTests(TestCase):
    # Setup function is run before every test
    # create a super user, log him in and create a normal user
    def setUp(self):
        """Create a super user and log him in
        Create a user"""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@londonappdev.com',
            password='password123'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='test@londonappdev.com',
            password='password123',
            name='Test user full name'
        )

    def test_users_listed(self):
        """Test that users are listed on user page"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        # AssertContains checks if certain value is present in a dict
        # Also checks if the http response is OK (200)
        # name field is not available in default UserAdmin class
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """Test that the user edit page works # /admin/core/user/1"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)