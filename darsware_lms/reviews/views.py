from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView

from .forms import ReviewForm
from .models import Review
from django.views import View
from django.views.generic import ListView



# Create your views here.

# Create a Class-based view for the review page
class ReviewView(View):
    """This class-based view handles the review page."""

    def get(self, request):
        """Handle GET requests to render the review form."""
        form = ReviewForm()
        return render(request, "reviews/review.html", {"form": form})

    def post(self, request):
        """Handle POST requests to process the review form."""
        form = ReviewForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            form.save()
            return HttpResponseRedirect("/review/thank-you/")

        return render(request, "reviews/review.html", {"form": form})


# Create review function

# def review(request):
#     """This function renders the review page."""
#     # Check if the request method is POST to process the form submission and validate the data
#     if request.method == "POST":
#         # Create a form instance
#         form = ReviewForm(request.POST)  # POST is submitted data dict into form using POST method
#
#         # Check if the submitted form data is valid
#         if form.is_valid():
#             # form.cleaned_data is a dictionary of form data
#             # Keys are form field names and values are form field values
#             # print(form.cleaned_data)
#             # print(form.cleaned_data["user_email"])
#
#
#             # Save the form data to the database
#             ##### Method 1 #####
#             # Create a new Review object and populate it with the cleaned data
#             # Saving data to the database using form Django form module - NOT - ModelForm
#             # review_form_data = Review(
#             #     user_name=form.cleaned_data["user_name"],
#             #     user_email=form.cleaned_data["user_email"],
#             #     user_review=form.cleaned_data["user_review"],
#             #     rating=form.cleaned_data["rating"]
#             # )
#             # # Save the Review object (review_form_data) to the database
#             # review_form_data.save()
#
#             ##### Method 2 #####
#             # Alternatively, save the form data to the database using ModelForm
#             form.save()
#             return HttpResponseRedirect("/review/thank-you/")
#     # If the request method is GET, create a new empty form
#     else:
#         # If the form is not valid, render a new empty form
#         form = ReviewForm()
#
#     return render(request, "reviews/review.html", {
#         "form": form # the validated form
#     })

class ThankYouView(TemplateView):
    """This class-based view handles the thank you page."""

    template_name = "reviews/thank_you.html"

    # Method overriding from TemplateView.
    # It returns a dictionary containing data (called "context")
    # that you want to make available within the template (thank_you.html).
    def get_context_data(self, **kwargs):
        """Add context data to the template."""
        context = super().get_context_data(**kwargs)
        context["message"] = "Thank you for your feedback!"
        return context

###1. Function View ######
# def thank_you(request):
#     """This function renders the thank you page."""
#     return render(request, "reviews/thank_you.html")



#####2. Template Class-based View ######
# class ReviewsListView(TemplateView):
#     template_name = "reviews/reviews_list.html"
#     # Method overriding from TemplateView.
#     def get_context_data(self, **kwargs):
#         """Add context data to the template."""
#         context = super().get_context_data(**kwargs)
#         # Get all reviews from the database
#         reviews = Review.objects.all() # import Review model from .models.py
#         # Add the reviews fetched from the database to the context as a new key
#         context["reviews"] = reviews
#         return context


##### 3. ListView Class-based view ######
class ReviewsListView(ListView):
    """This class-based view handles the list of reviews."""

    model = Review  # Specify the model to use
    template_name = "reviews/reviews_list.html"  # Specify the template to use
    context_object_name = "reviews"  # Specify the name of the context variable to expose in the template
    #
    # def get_queryset(self):
    #     """Override the get_queryset method to customize the queryset."""
    #     # You can customize the queryset here if needed
    #     base_query = super().get_queryset()
    #     # For example, you can filter the reviews based on some criteria
    #     # filtered_data = base_query.filter(rating__gte=3)  # Example: filter reviews with rating >= 3
    #     # return filtered_data # When reload the page, it will show the filtered data only
    #     return base_query






# Create a view class for the single review page
### 1. Using TemplateView class view ####
# class SingleReviewView(TemplateView):
#     template_name = "reviews/single_review.html"
#
#     def get_context_data(self, **kwargs):
#         """Add context data to the template."""
#         context = super().get_context_data(**kwargs)
#         # kwargs is a dictionary containing the URL parameters
#         # Get the review ID from the URL parameters
#         review_id = kwargs.get("id")
#         selected_review = Review.objects.get(pk=review_id)  # import Review model from .models.py
#
#         # Get all reviews from the database
#         reviews = Review.objects.all()  # import Review model from .models.py
#         # Add the reviews fetched from the database to the context as a new key
#         context["review"] = selected_review
#         return context


### 2. Using DetailView class view ####
class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review  # Specify the model to use
    # - The model is `Review`.
    # - `DetailView` automatically assigns the retrieved object to a context variable named `review`.
    # Change url-pattern to use the primary key (pk) instead of id <int:pk>

    # If you want to use a custom name for the context variable
    # Instead of the default `review`, you can specify a custom name using the `context_object_name` attribute.
    # For example:
    # context_object_name = "my_custom_review_name"


