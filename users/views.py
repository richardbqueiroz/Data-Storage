from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, FormView,
                                  ListView, UpdateView)

from app import metrics
from users import forms, models


class UserListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.User
    template_name = 'user_list.html'
    context_object_name = 'users'
    paginate_by = 10
    permission_required = 'users.view_user'

    def get_queryset(self):
        queryset = super().get_queryset()
        username = self.request.GET.get('user_name')
        full_name = self.request.GET.get('full_name')
        email = self.request.GET.get('email')
        cpf = self.request.GET.get('cpf')

        if username:
            queryset = queryset.filter(username__icontains=username)
        if full_name:
            queryset = queryset.filter(full_name__icontains=full_name)
        if email:
            queryset = queryset.filter(email__icontains=email)
        if cpf:
            queryset = queryset.filter(cpf__icontains=cpf)

        return queryset.order_by('username')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_metrics'] = metrics.get_user_metrics()
        return context


class UserCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.User
    form_class = forms.UserCreateForm
    template_name = 'user_create.html'
    context_object_name = 'users'
    success_url = reverse_lazy('user_list')
    permission_required = 'users.add_user'

    def form_valid(self, form):
        return super().form_valid(form)


class UserDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.User
    template_name = 'user_detail.html'
    context_object_name = 'users'
    permission_required = 'users.view_user'


class UserUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.User
    form_class = forms.UserUpdateForm
    template_name = 'user_update.html'
    context_object_name = 'users'
    success_url = reverse_lazy('user_list')
    permission_required = 'users.change_user'

    def form_valid(self, form):
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        user_to_edit = self.get_object()
        if user_to_edit.is_superuser and user_to_edit != request.user:
            return redirect('user_list')
        return super().dispatch(request, *args, **kwargs)


class UserDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.User
    template_name = 'user_delete.html'
    context_object_name = 'users'
    success_url = reverse_lazy('user_list')
    permission_required = 'users.delete_user'

    def get_object(self, queryset=None):
        user = super().get_object(queryset)
        if user.is_superuser:
            return redirect('user_list')
        return user

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        if user == request.user:
            return redirect('user_list')
        return super().delete(request, *args, **kwargs)


class UserPasswordView(LoginRequiredMixin, PermissionRequiredMixin, FormView):
    model = models.User
    form_class = forms.UserPasswordChangeForm
    context_object_name = 'users'
    template_name = 'user_password_change.html'
    success_url = reverse_lazy('user_list')
    permission_required = 'users.change_user'

    def get_object(self):
        return get_object_or_404(models.User, pk=self.kwargs['pk'])

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.get_object()
        return kwargs

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
