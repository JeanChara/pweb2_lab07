from django.http import HttpResponse
from django.views.generic import View

from django.template.loader import get_template
from .utils import render_to_pdf

class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        template = get_template('pdf/invoice.html')
        context = {
            'customer_name': 'Mayte Antuanet',
            'invoice_id': 1233434,
            'amount': 39.99,
            'today': 'Today', 
        }
        html = template.render(context)
        pdf = render_to_pdf('pdf/invoice.html', context)
        return HttpResponse(pdf, content_type = 'application/pdf')