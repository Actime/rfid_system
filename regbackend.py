from registration.backends.default.views import RegistrationView
from competitors.forms import AuthenticationRegistrationForm
from competitors.models import Competitor, Authentication

"""
Custom registration view class
"""
class CustomRegistrationView(RegistrationView):
    # init the form class
    form_class = AuthenticationRegistrationForm
    
    def register(self, request, form_class):
        """
        Register override function
        """
        new_user = super(CustomRegistrationView, self).register(request, form_class)
        # Authentication model
        authentication = Authentication()
        # Competitor model
        competitor = Competitor()
        # Assign all the competitor model variables
        competitor.name = form_class.cleaned_data['name']
        competitor.second_name = form_class.cleaned_data['second_name']
        competitor.birth_date = form_class.cleaned_data['birth_date']
        competitor.city = form_class.cleaned_data['city']
        competitor.state = form_class.cleaned_data['state']
        competitor.country = form_class.cleaned_data['country']
        competitor.zip_code = form_class.cleaned_data['zip_code']
        competitor.address = form_class.cleaned_data['address']
        competitor.address2 = form_class.cleaned_data['address2']
        competitor.email = new_user.email
        competitor.phone_number = form_class.cleaned_data['phone_number']
        competitor.sex = form_class.cleaned_data['sex']
        # Save the competitor
        competitor.save()
        # Set the variables to the authentication model
        authentication.competitor = competitor
        authentication.user = new_user
        # Save the authentication model
        authentication.save()
        # Return the authentication model if it is well saved
        return authentication
    # End of register function
    
# End of CustomRegistrationView class