from django.views.generic import DeleteView
from .models import Articles

class AAAAA(DeleteView):
    model = Articles
    template_name = "main.motivation.html"
    motivation = 'motivation'