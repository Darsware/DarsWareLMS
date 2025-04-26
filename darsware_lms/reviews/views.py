from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review
from django.views import View



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

def thank_you(request):
    """This function renders the thank you page."""
    return render(request, "reviews/thank_you.html")

