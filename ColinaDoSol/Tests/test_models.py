from django.contrib.auth import get_user_model
from django.test import TestCase

CustomUser = get_user_model()

class UserTestCase(TestCase):
    def setUp(self):
        self.admin_user = CustomUser.objects.create_user(
            username='admin',
            password='admin_password',
            role='ADMIN'
        )
        self.manager_user = CustomUser.objects.create_user(
            username='manager',
            password='manager_password',
            role='LOJISTA'
        )

    def test_create_user(self):
        # Verify user creation
        user_count = CustomUser.objects.count()
        self.assertEqual(user_count, 2)

    def test_change_user_fields(self):
        # Change fields for a user
        self.manager_user.phone_number = '123456789'
        self.manager_user.save()

        # Verify the updated field value
        updated_user = CustomUser.objects.get(username='manager')
        self.assertEqual(updated_user.phone_number, '123456789')

    def test_delete_user(self):
        # Delete a user
        self.admin_user.delete()

        # Verify user deletion
        user_count = CustomUser.objects.count()
        self.assertEqual(user_count, 1)

    def test_change_admin_password(self):
        # Change the admin user's password
        self.admin_user.set_password('new_admin_password')
        self.admin_user.save()

        # Verify the password change
        self.assertTrue(self.admin_user.check_password('new_admin_password'))
