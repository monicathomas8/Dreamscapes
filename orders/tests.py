from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from orders.models import Order, OrderItem
from artwork.models import Artwork
from unittest.mock import patch

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

    # Mock cart data
        self.artwork = Artwork.objects.create(
            title='Test Art',
            price=10.00,
            image='test.jpg',
        )

        self.cart_data = {
            str(self.artwork.id): {
                'title': self.artwork.title,
                'price': str(self.artwork.price),
                'image': 'test.jpg',
                'quantity': 1,
            }
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


class CheckoutPaymentTest(TestCase):
    """Test case for checkout payment process."""

    def setUp(self):
        """Set up a user and an order for testing."""
        self.user = User.objects.create_user(
            username='paymentuser',
            password='testpass'
        )
        self.client.login(username='paymentuser', password='testpass')
        self.order = Order.objects.create(
            user=self.user,
            total_price=25.00,
            status='Pending'
        )
        self.session = self.client.session
        self.session['order_id'] = self.order.id
        self.session.save()

    @patch('stripe.PaymentIntent.create')  # mock Stripe
    def test_checkout_payment_creates_intent(self, mock_create_intent):
        """Test that checkout payment creates a Stripe PaymentIntent."""
        mock_create_intent.return_value.client_secret = 'test_client_secret'

        response = self.client.get(reverse('checkout-payment'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'test_client_secret')


class CheckoutPaymentViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='monicatester',
            password='testpass'
        )
        self.client.login(username='monicatester', password='testpass')
        self.order = Order.objects.create(
            user=self.user,
            total_price=50.00,
            status='Pending'
        )
        session = self.client.session
        session['order_id'] = self.order.id
        session.save()

    @patch('stripe.PaymentIntent.create')
    def test_checkout_payment_view_loads_and_has_client_secret(
        self, mock_create
    ):
        mock_create.return_value.client_secret = 'fake_secret'

        response = self.client.get(reverse('checkout-payment'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'fake_secret')


class CheckoutPaymentDisplayTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='displayuser', password='displaypass'
        )
        self.client.login(username='displayuser', password='displaypass')

        self.artwork = Artwork.objects.create(
            title='Display Test Art',
            price=25.00,
            description='Test art for display',
            image='test.jpg'
        )

        self.order = Order.objects.create(
            user=self.user,
            total_price=25.00,
            status='Pending'
        )

        OrderItem.objects.create(
            order=self.order,
            artwork=self.artwork,
            price=25.00,
            quantity=1,
        )

        session = self.client.session
        session['order_id'] = self.order.id
        session.save()

    def test_checkout_payment_displays_order_items(self):
        response = self.client.get(reverse('checkout-payment'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Display Test Art')
        self.assertContains(response, '£25.00')
