from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('register/', views.registerPage, name="registerPage"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name='logout'),
    path('', views.userPage, name='userPage'),
    path('account/', views.accountSettings, name='account'),
    path('updateList/<str:pk>/', views.updateList, name='update_List'),
    path('addNewItem/', views.listAddPage, name='list_Add_Page'),
    path('delete_order/<str:pk>/', views.deleteList, name="delete_order"),
    path('filterPage/', views.filterList, name="filterPage"),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_form.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_complete')

]
