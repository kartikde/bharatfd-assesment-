from django.db import models
from ckeditor.fields import RichTextField
from django.core.cache import cache
from googletrans import Translator

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    question_hi = models.TextField(null=True, blank=True)
    answer_hi = RichTextField(null=True, blank=True)
    question_bn = models.TextField(null=True, blank=True)
    answer_bn = RichTextField(null=True, blank=True)

    def translate_text(self, text, target_lang):
        translator = Translator()
        return translator.translate(text, dest=target_lang).text

    def save(self, *args, **kwargs):
        if not self.question_hi:
            self.question_hi = self.translate_text(self.question, 'hi')
        if not self.answer_hi:
            self.answer_hi = self.translate_text(self.answer, 'hi')
        if not self.question_bn:
            self.question_bn = self.translate_text(self.question, 'bn')
        if not self.answer_bn:
            self.answer_bn = self.translate_text(self.answer, 'bn')
        super().save(*args, **kwargs)

    def get_translated_faq(self, lang='en'):
        cache_key = f"faq_{self.id}_{lang}"
        cached_data = cache.get(cache_key)

        if cached_data:
            return cached_data

        if lang == 'hi':
            result = {'question': self.question_hi, 'answer': self.answer_hi}
        elif lang == 'bn':
            result = {'question': self.question_bn, 'answer': self.answer_bn}
        else:
            result = {'question': self.question, 'answer': self.answer}

        cache.set(cache_key, result, timeout=86400)
        return result
