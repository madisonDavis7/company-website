#pages/views.py
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def home_page_view(request):
    context = {
        "inventory_list": ["Widget 1", "Widget 2", "Widget 3"], 
        "greeting": "THank you FOR visitING.", 
	}
    return render(request, "home.html", context)

class AboutPageView(TemplateView):
    template_name = "about.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contact_address"] = "123 Main Street"
        context["phone_number"] = "555-555-5555"
        return context

class ProductsPageView(TemplateView):
    template_name = "products.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["book_one"] = "Snowcrash"
        context["book_two"] = "Quicksilver"
        context["book_three"] = "Anathem"
        context["book_four"] = "Cryptonomico"

        return context
        