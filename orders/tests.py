from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from orders.models import Order


User = get_user_model()


class ShippingInfoTest(TestCase):
    """Test case for shipping information retrieval."""
    def setUp(self):
        """Set up a user and an order for testing."""
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass',
        )
        self.client.login(username='testuser', password='testpass')
        self.cart_data = {
            '1': {
                'title': 'Test Art',
                'price': '10.00',
                'image': 'test_image.jpg',
            },

        }

    def test_shipping_info_creates_order(self):
        session = self.client.session
        session['cart'] = self.cart_data
        session.save()

        response = self.client.post(reverse('shipping-info'), data={
            'first_name': 'Alice',
            'last_name': 'Smith',
            'email': 'alice@example.com',
            'address_line_1': '123 Art Lane',
            'city': 'London',
            'postal_code': 'W1A 1AA',
            'country': 'GB',
        })

        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            Order.objects.filter(
                user=self.user,
                email='alice@example.com'
            ).exists()
        )
