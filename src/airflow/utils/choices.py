from django.db.models import TextChoices


class StatusChoices(TextChoices):
    PENDING = ('PENDING', 'Pending')
    COMPLETED = ('COMPLETED', 'Completed')
