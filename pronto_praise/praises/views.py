from django.shortcuts import render
from django.views.generic import TemplateView


class PraiseListView(TemplateView):
    template_name = 'praises.html'

    def get(self, request):
        return render(
            request,
            self.template_name
        )


class PraiseAddView(TemplateView):
    template_name = 'praise_add.html'

    def get(self, request):
        return render(
            request,
            self.template_name
        )
