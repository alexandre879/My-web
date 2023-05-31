from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from users.models import User
class CustomUserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',)
        
