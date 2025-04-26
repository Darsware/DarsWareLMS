from django import forms
from .models import Review

# # Using the forms module from Django to create a form for the review page
# class ReviewForm(forms.Form):
#     """This class creates a form for the review page."""
#
#     user_name = forms.CharField(
#         label="Your Name",
#         widget=forms.TextInput(attrs={"class": "form-control", "style": "width: 70%;"}),
#         max_length=100,
#         error_messages={
#             "required": "Please enter your name.",
#             "max_length": "Your name is too long. Please enter a shorter name.",
#         }
#     )
#     user_email = forms.EmailField(
#         label="Your Email",
#         widget=forms.EmailInput(attrs={"class": "form-control", "style": "width: 70%;"}),
#         max_length=100,
#         error_messages={
#             "required": "Please enter your email address.",
#             "max_length": "Your email address is too long. Please enter a shorter email address.",
#         }
#     )
#     user_review = forms.CharField(
#         label="Your Feedback",
#         widget=forms.Textarea(attrs={"class": "form-control", "style": "width: 90%;"}),
#         max_length=250,
#         error_messages={
#             "required": "Please enter your review.",
#         }
#     )
#     rating = forms.IntegerField(
#         label="Your Rating",
#         widget=forms.NumberInput(attrs={"class": "form-control", "style": "width: 20%;"}),
#         min_value=1,
#         max_value=5,
#         error_messages={
#             "required": "Please provide a rating.",
#             "min_value": "Rating must be at least 1.",
#             "max_value": "Rating cannot exceed 5.",
#         }
#     )

# # Using the forms model from Django to create a form for the review page
class ReviewForm(forms.ModelForm):
    """This class creates a form for the review page."""

    class Meta: # Let Django know which model this form is connected to
        model = Review # Pointing to the Review model

        # Include all fields from the model to show in the form
        # fields = "__all__"  # This will include all fields from the model

        # # If you want to exclude certain fields, you can use the exclude attribute
        # # For example, this will exclude the 'owner_comment' field from the form
        # exclude = ["owner_comment"]


        # # Alternatively, we can specify the fields we want to include in the form

        # Specify fields from the model that we want to include in the form
        fields = ["user_name", "user_email", "user_review", "rating"]

        # Specify the labels for the fields
        labels = {
            "user_name": "Your Name",
            "user_email": "Your Email",
            "user_review": "Your Feedback",
            "rating": "Your Rating",
        }

        error_messages = {
            "user_name": {
                "required": "Please enter your name.",
                "max_length": "Your name is too long. Please enter a shorter name.",
            },
            "user_email": {
                "required": "Please enter your email address.",
                "max_length": "Your email address is too long. Please enter a shorter email address.",
            },
            "user_review": {
                "required": "Please enter your review.",
            },
            "rating": {
                "required": "Please provide a rating.",
                "min_value": "Rating must be at least 1.",
                "max_value": "Rating cannot exceed 5.",
            }
        }


        widgets = {
            "user_name": forms.TextInput(attrs={
                "class": "form-control",
                "style": "width: 70%;"}),

            "user_email": forms.EmailInput(attrs={"class": "form-control", "style": "width: 70%;"}),
            "user_review": forms.Textarea(attrs={"class": "form-control", "style": "width: 90%;"}),
            "rating": forms.NumberInput(attrs={"class": "form-control", "style": "width: 20%;"}),
        }