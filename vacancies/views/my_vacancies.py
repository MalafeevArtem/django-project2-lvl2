import datetime

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from django.forms import forms, models

from django.shortcuts import redirect, render

from django.utils.decorators import method_decorator

from django.views import View

from vacancies import forms, models


@method_decorator(login_required, name='dispatch')
class MyVacanciesView(View):
    def get(self, request):
        user = request.user
        is_company = models.Company.objects.filter(owner__id=user.id).first()

        if is_company is not None:
            vacancies = models.Vacancy.objects.filter(company__owner__id=user.id)

            if vacancies.first() is None:
                messages.add_message(request, messages.INFO, 'У вас пока нет вакансий, но вы можете создать первую!')

                return render(request, '../vacancies-list.html')

            context = {
                'vacancies': vacancies
            }

            return render(request, '../vacancies-list.html', context)

        messages.add_message(request, messages.INFO, 'Необходимо создать компанию!')

        return render(request, '../company-edit.html', {'form': forms.MyCompanyEditForm()})


@method_decorator(login_required, name='dispatch')
class MyVacancyEditView(View):
    def get(self, request, vacancy_id):
        user = request.user
        vacancy = models.Vacancy.objects.get(company__owner__id=user.id, id=vacancy_id)

        return render(request, '../vacancies-edit.html', {'form': forms.MyVacancyEditForm(instance=vacancy),
                                                                 'title': vacancy.title})

    def post(self, request, vacancy_id):
        user = request.user
        instance = models.Vacancy.objects.get(company__owner__id=user.id, id=vacancy_id)
        form = forms.MyVacancyEditForm(request.POST, instance=instance)
        company = models.Company.objects.get(owner__id=user.id)

        if form.is_valid():
            vacancy = form.save(commit=False)
            vacancy.company = company
            vacancy.published_at = datetime.date.today()
            form.save()

            messages.add_message(request, messages.INFO, 'Изменения успешно сохранены!')

            return redirect('/mycompany/vacancies/{0}'.format(vacancy_id))

        return render(request, '../vacancies-edit.html', {'form': form})


@method_decorator(login_required, name='dispatch')
class MyVacancyCreateView(View):
    def get(self, request):

        return render(request, '../vacancies-edit.html', {'form': forms.MyVacancyEditForm()})

    def post(self, request):
        user = request.user
        form = forms.MyVacancyEditForm(request.POST)
        company = models.Company.objects.get(owner__id=user.id)

        if form.is_valid():
            vacancy = form.save(commit=False)
            vacancy.company = company
            vacancy.published_at = datetime.date.today()
            form.save()

            messages.add_message(request, messages.INFO, 'Вакансия успешно создана!')
            vacancy_id = form.save().id

            return redirect('/mycompany/vacancies/{0}'.format(vacancy_id))

        return render(request, '../vacancies-edit.html', {'form': form})
