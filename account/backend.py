from django.contrib.auth.backends import ModelBackend, UserModel
from django.db.models import Q


#this code for login with email or username
class EmailorUsernameModelBackend(ModelBackend):
    # authenticate 
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # get user with username or email using Q
            user = UserModel.objects.get(Q(username=username) | Q(email=username))
        # If the userModel did not exist
        except UserModel.DoesNotExist:
            #set password
            UserModel().set_password(password)
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
    # get user with user_id
    def get_user(self, user_id):
        try:
            # get user 
            user = UserModel.objects.get(pk=user_id)
        # if userModel does not exist
        except UserModel.DoesNotExist:
            return None
        # if user_can_authenticate return user else return None
        return user if self.user_can_authenticate(user) else None