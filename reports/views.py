from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from brands.models import Brand
from categories.models import Category
from inflows.models import Inflow
from outflows.models import Outflow
from products.models import Product
from suppliers.models import Supplier
from users.models import User

from .pdf_generate import (generate_brand_report_pdf,
                           generate_category_report_pdf,
                           generate_inflow_report_pdf,
                           generate_outflow_report_pdf,
                           generate_product_report_pdf,
                           generate_supplier_report_pdf,
                           generate_totality_report_pdf,
                           generate_user_report_pdf)


class ReportListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = 'report_list.html'
    permission_required = 'reports.view_report'
    context_object_name = 'reports'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class SupplierReportView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Supplier
    template_name = 'supplier_report.html'
    permission_required = 'reports.view_report'
    context_object_name = 'suppliers'

    def get(self, request, *args, **kwargs):
        if request.GET.get('format') == 'pdf':
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename="relatorio_fornecedores.pdf"'
            suppliers = self.get_queryset()
            generate_supplier_report_pdf(response, suppliers)
            return response
        return super().get(request, *args, **kwargs)


class BrandReportView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Brand
    template_name = 'brand_report.html'
    permission_required = 'reports.view_report'
    context_object_name = 'brands'

    def get(self, request, *args, **kwargs):
        if request.GET.get('format') == 'pdf':
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename="relatorio_marcas.pdf"'
            brands = self.get_queryset()
            generate_brand_report_pdf(response, brands)
            return response
        return super().get(request, *args, **kwargs)


class CategoryReportView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Category
    template_name = 'category_report.html'
    permission_required = 'reports.view_report'
    context_object_name = 'categories'

    def get(self, request, *args, **kwargs):
        if request.GET.get('format') == 'pdf':
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename="relatorio_categorias.pdf"'
            categories = self.get_queryset()
            generate_category_report_pdf(response, categories)
            return response
        return super().get(request, *args, **kwargs)


class InflowReportView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Inflow
    template_name = 'inflow_report.html'
    permission_required = 'reports.view_report'
    context_object_name = 'inflows'

    def get(self, request, *args, **kwargs):
        if request.GET.get('format') == 'pdf':
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename="relatorio_entradas.pdf"'
            inflows = self.get_queryset()
            generate_inflow_report_pdf(response, inflows)
            return response
        return super().get(request, *args, **kwargs)


class OutflowReportView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Outflow
    template_name = 'outflow_report.html'
    permission_required = 'reports.view_report'
    context_object_name = 'outflows'

    def get(self, request, *args, **kwargs):
        if request.GET.get('format') == 'pdf':
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename="relatorio_saidas.pdf"'
            outflows = self.get_queryset()
            generate_outflow_report_pdf(response, outflows)
            return response
        return super().get(request, *args, **kwargs)


class UserReportView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = User
    template_name = 'user_report.html'
    permission_required = 'reports.view_report'
    context_object_name = 'users'

    def get(self, request, *args, **kwargs):
        if request.GET.get('format') == 'pdf':
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename="relatorio_usuarios.pdf"'
            users = self.get_queryset()
            generate_user_report_pdf(response, users)
            return response
        return super().get(request, *args, **kwargs)


class ProductReportView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Product
    template_name = 'product_report.html'
    permission_required = 'reports.view_report'
    context_object_name = 'products'

    def get(self, request, *args, **kwargs):
        if request.GET.get('format') == 'pdf':
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename="relatorio_produtos.pdf"'
            products = self.get_queryset()
            generate_product_report_pdf(response, products)
            return response
        return super().get(request, *args, **kwargs)


class TotalityReportView(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    template_name = 'totality_report.html'
    permission_required = 'reports.view_report'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brand_count'] = Brand.objects.count()
        context['category_count'] = Category.objects.count()
        context['product_count'] = Product.objects.count()
        context['supplier_count'] = Supplier.objects.count()
        context['inflow_count'] = Inflow.objects.count()
        context['outflow_count'] = Outflow.objects.count()
        context['user_count'] = User.objects.count()
        return context

    def get(self, request, *args, **kwargs):
        if request.GET.get('format') == 'pdf':
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename="totality_report.pdf"'
            context = self.get_context_data(**kwargs)
            totalities = {
                'Marcas': context['brand_count'],
                'Categorias': context['category_count'],
                'Produtos': context['product_count'],
                'Fornecedores': context['supplier_count'],
                'Entradas': context['inflow_count'],
                'Saídas': context['outflow_count'],
                'Usuários': context['user_count'],
            }
            generate_totality_report_pdf(response, totalities)
            return response
        return super().get(request, *args, **kwargs)
