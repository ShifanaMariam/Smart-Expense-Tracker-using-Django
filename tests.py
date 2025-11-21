from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Expense
from django.urls import reverse

User = get_user_model()

class SimpleTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='pass')
        self.client.login(username='testuser', password='pass')

    def test_create_expense(self):
        resp = self.client.post(reverse('expense_add'), {
            'description':'uber ride', 'amount':'150.00', 'date':'2025-01-01', 'category':'Other'
        })
        self.assertEqual(resp.status_code, 302)
        self.assertTrue(Expense.objects.filter(user=self.user, description='uber ride').exists())
