from .views import *
from django.urls import path

urlpatterns = [
    path('sign_up/', SignupPageView.as_view(), name='sign_up'),
    path('sign_in/', SignInView.as_view(), name='sign_in'),
    path('logout/', logout2, name='logout'),
    # path('all/', all),
    # path('get/<int:id>/', get),
    # path('update/<int:id>/', update),
    # path('delete/<int:id>/', delete),
]
