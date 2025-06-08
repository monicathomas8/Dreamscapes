from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core import mail
from allauth.account.signals import user_signed_up
from django.test.client import RequestFactory


User = get_user_model()


class WelcomeEmailTest(TestCase):

    def test_welcome_email_sent_on_signup(self):
        # Create a user
        user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='securepassword123'
        )

        # Simulate a signup request
        factory = RequestFactory()
        request = factory.post('/accounts/signup/')

        # Manually trigger the signal
        user_signed_up.send(sender=User, request=request, user=user)

        # Check if the welcome email was sent
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn('Welcome to Dreamscapes', mail.outbox[0].subject)
        self.assertIn('testuser', mail.outbox[0].body)
        self.assertIn('Thank you for signing up', mail.outbox[0].body)
        self.assertIn('test@example.com', mail.outbox[0].to)
