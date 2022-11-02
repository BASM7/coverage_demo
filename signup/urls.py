from django.urls import path


from . import views

urlpatterns = [
    path('create/', views.KaizenUserCreateAPIView.as_view()),
    path('lookup/<uuid:verification_code>', views.KaizenUserDetailAPIView.as_view()),
    path('verify/<uuid:verification_code>', views.KaizenUserVerifyAPIView.as_view())
]