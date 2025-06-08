from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile
from allauth.account.signals import user_signed_up
from django.core.mail import send_mail
from django.conf import settings


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(user_signed_up)
def send_welcome_email(request, user, **kwargs):
    send_mail(
        subject='Welcome to Dreamscapes!',
        message=(
            f'Hi {user.username},\n\n'
            'Thank you for signing up for Dreamscapes!\n\n'
            'We are thrilled to have you join our community of dreamers.\n'
            'Your journey into the world of imagination starts now.\n\n'
            'If you have questions or need assistance, don\'t hesitate to '
            'reach out.\n\n'
            'We are excited to have you on board.\n\n'
            'Best regards,\nThe Dreamscapes Team'
        ),
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user.email],
        fail_silently=False,
    )
