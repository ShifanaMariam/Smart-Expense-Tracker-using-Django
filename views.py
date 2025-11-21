from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpResponse
import csv
from .models import Expense
from .forms import ExpenseForm
from django.utils import timezone
from django.template.loader import render_to_string
from django.db.models import Sum

class ExpenseListView(LoginRequiredMixin, ListView):
    model = Expense
    template_name = 'tracker/expense_list.html'
    paginate_by = 50

    def get_queryset(self):
        qs = Expense.objects.filter(user=self.request.user)
        f = self.request.GET.get('filter')
        today = timezone.localdate()
        if f == 'today':
            qs = qs.filter(date=today)
        elif f == 'week':
            start = today - timezone.timedelta(days=today.weekday())
            qs = qs.filter(date__gte=start, date__lte=today)
        elif f == 'month':
            qs = qs.filter(date__year=today.year, date__month=today.month)
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        qs = self.get_queryset()
        total = qs.aggregate(total=Sum('amount'))['total'] or 0
        ctx['total'] = total
        return ctx

class ExpenseCreateView(LoginRequiredMixin, CreateView):
    model = Expense
    form_class = ExpenseForm
    template_name = 'tracker/expense_form.html'
    success_url = reverse_lazy('expense_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save(user=self.request.user)
        return super().form_valid(form)

class ExpenseUpdateView(LoginRequiredMixin, UpdateView):
    model = Expense
    form_class = ExpenseForm
    template_name = 'tracker/expense_form.html'
    success_url = reverse_lazy('expense_list')

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)

class ExpenseDeleteView(LoginRequiredMixin, DeleteView):
    model = Expense
    template_name = 'tracker/expense_confirm_delete.html'
    success_url = reverse_lazy('expense_list')

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)

class ExpenseChartData(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        qs = Expense.objects.filter(user=request.user)
        data = {}
        for e in qs:
            data[e.category] = data.get(e.category, 0) + float(e.amount)
        labels = list(data.keys())
        values = list(data.values())
        return JsonResponse({'labels': labels, 'values': values})

class ExportCSV(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        qs = Expense.objects.filter(user=request.user).order_by('date')
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="expenses.csv"'
        writer = csv.writer(response)
        writer.writerow(['Date','Description','Category','Amount','Notes'])
        for e in qs:
            writer.writerow([e.date, e.description, e.category, e.amount, e.notes])
        return response

class ExportPDF(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        qs = Expense.objects.filter(user=request.user).order_by('date')
        html_string = render_to_string('tracker/report_pdf.html', {'expenses': qs, 'user': request.user})
        # If WeasyPrint is installed, you can render to PDF. For now return HTML for preview.
        return HttpResponse(html_string)
