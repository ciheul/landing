from django.shortcuts import render
from django.views.generic import View


class DashboardView(View):
    def get(self, request):
        return render(request, 'eaglenest/dashboard.html')


class ComponentTciListView(View):
    def get(self, request):
        return render(request, 'eaglenest/component-tci-list.html')


class ComponentTciView(View):
    def get(self, request):
        return render(request, 'eaglenest/component-tci.html')


class ComponentOcView(View):
    def get(self, request):
        return render(request, 'eaglenest/component-oc.html')