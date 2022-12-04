from django.db import models

from utils.choices import StatusChoices
from utils.models import BaseModel
import uuid


# Create your models here.

class ProvidersData(BaseModel):
    items = models.JSONField(default=dict)
    status = models.CharField(max_length=20, choices=StatusChoices.choices, default=StatusChoices.PENDING)
    search_id = models.UUIDField(default=uuid.uuid4)

    def __str__(self):
        return f"{self.search_id}"

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Данные поиска с провайдеров"
        verbose_name_plural = "Данные поиска с провайдеров"


class ExchangeRate(BaseModel):
    rates = models.JSONField()

    def __str__(self):
        return f"{self.id}"

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Курс валют"
        verbose_name_plural = "Курс валют"
