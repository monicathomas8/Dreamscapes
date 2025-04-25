from django.core.mail import send_mail


def send_confirmation_email(order):
    subject = f'Order Confirmation - #{order.id}'
    message = (
        f'Thank you for your purchase, {order.user.username}!\n\n'
        f'Order Details:\n'
        f'Order ID: {order.id}\n'
        f'Total Price: £{order.total_price}\n'
        f'Items:\n'
        f' - {", ".join([item.artwork.title for item in order.items.all()])}\n\n'
        f'Your digital downloads are now available in your dashboard!'
    )
    recipient_list = [order.user.email]
    send_mail(subject, message, 'your-email@gmail.com', recipient_list)
