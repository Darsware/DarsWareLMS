# import urlpatterns
from django.urls import include


from django.urls import path
from . import views

urlpatterns = [
    path("", views.ReviewView.as_view(), name="review"), # /review/
    path("thank-you/", views.ThankYouView.as_view(), name="thank_you"),
    path("reviews/", views.ReviewsListView.as_view(), name="review_list"), # /review/reviews/
]