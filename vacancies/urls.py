from django.urls import path

from django.conf import settings

from django.conf.urls.static import static

from vacancies.views import public, my_company, my_vacancies, authoriztion

urlpatterns = [
    path('', public.MainView.as_view()),
    path('vacancies/', public.VacanciesView.as_view()),
    path('vacancies/cat/<str:specialization>/', public.SpecialtyView.as_view()),
    path('companies/<int:id>/', public.CompanyView.as_view()),
    path('vacancies/<int:vacancy_id>/', public.VacancyView.as_view()),
    path('vacancies/<int:vacancy_id>/send/', public.SendView.as_view()),

    path('mycompany/', my_company.MyCompanyEditView.as_view()),
    path('mycompany/create/', my_company.MyCompanyCreateView.as_view()),
    path('mycompany/vacancies/', my_vacancies.MyVacanciesView.as_view()),
    path('mycompany/vacancies/<vacancy_id>/', my_vacancies.MyVacancyEditView.as_view()),
    path('mycompany/vacancy/create/', my_vacancies.MyVacancyCreateView.as_view()),

    path('login/', authoriztion.LoginView.as_view()),
    path('register/', authoriztion.RegisterView.as_view()),
    path('logout/', authoriztion.LogoutView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
