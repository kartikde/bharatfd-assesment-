from rest_framework import viewsets
from .models import FAQ
from .serializers import FAQSerializer
from rest_framework.response import Response

class FAQViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def list(self, request, *args, **kwargs):
        lang = request.query_params.get('lang', 'en')
        faqs = self.queryset

        data = [
            {
                'id': faq.id,
                'question': faq.get_translated_faq(lang)['question'],
                'answer': faq.get_translated_faq(lang)['answer'],
            }
            for faq in faqs
        ]

        return Response(data)
