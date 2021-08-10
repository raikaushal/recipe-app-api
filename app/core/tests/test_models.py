from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_user_with_email_sucessful(self):
        """Test for creating a new user with email is successful"""
        email = 'raikaushal07@gmail.com'
        password = 'TestPassword'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_user_email_address_normalisation(self):
        """to check wrther user email is normalized"""
        email = 'raikaushal@GMAIL.com'
        user = get_user_model().objects.create_user(
            email=email,
            password='test123'
        )
        self.assertEqual(user.email, email.lower())

    def test_user_with_no_email(self):
        """Testing the functionality with no email"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email=None,
                password='test123'
            )

    def test_create_new_superuser(self):
        """Test creating new superuser"""
        user = get_user_model().objects.create_superuser(
            'raikaushal07@gmail.com',
            'test123'
            )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
