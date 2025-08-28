from django.urls import path

from reports import views

urlpatterns = [
    path('reports/list/', views.ReportListView.as_view(), name='report_list'),
    path('reports/user/', views.UserReportView.as_view(), name='user_report'),
    path('reports/brand/', views.BrandReportView.as_view(), name='brand_report'),
    path('reports/inflow/', views.InflowReportView.as_view(), name='inflow_report'),
    path('reports/outflow/', views.OutflowReportView.as_view(), name='outflow_report'),
    path('reports/product/', views.ProductReportView.as_view(), name='product_report'),
    path('reports/supplier/', views.SupplierReportView.as_view(), name='supplier_report'),
    path('reports/category/', views.CategoryReportView.as_view(), name='category_report'),
    path('reports/totality/', views.TotalityReportView.as_view(), name='totality_report'),
]
