from django.views import generic


class HomePage(generic.TemplateView):
    template_name = "home.html"

class AboutPage(generic.TemplateView):
    template_name = "about.html"

class ex1(generic.TemplateView):
    template_name = "ex1.html"

class ex2(generic.TemplateView):
    template_name = "ex2.html"

class ex3(generic.TemplateView):
    template_name = "ex3.html"