from django.test import TestCase
from .models import FAQ

class FAQTestCase(TestCase):
    def setUp(self):
        self.faq = FAQ.objects.create(question="What is Django?", answer="Django is a web framework.")

    def test_translation(self):
        self.assertIsNotNone(self.faq.question_hi)
        self.assertIsNotNone(self.faq.answer_hi)

    def test_api_response(self):
        response = self.client.get('/api/faqs/?lang=hi')
        self.assertEqual(response.status_code, 200)
