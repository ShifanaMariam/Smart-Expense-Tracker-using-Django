from django.urls import path
from . import views

urlpatterns = [
    path('', views.ExpenseListView.as_view(), name='expense_list'),
    path('add/', views.ExpenseCreateView.as_view(), name='expense_add'),
    path('edit/<int:pk>/', views.ExpenseUpdateView.as_view(), name='expense_edit'),
    path('delete/<int:pk>/', views.ExpenseDeleteView.as_view(), name='expense_delete'),
    path('chart-data/', views.ExpenseChartData.as_view(), name='chart_data'),
    path('export/csv/', views.ExportCSV.as_view(), name='export_csv'),
    path('export/pdf/', views.ExportPDF.as_view(), name='export_pdf'),
]
