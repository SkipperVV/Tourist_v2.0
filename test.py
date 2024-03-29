from django.contrib.auth.models import User, Group

print(User)
def sample_view(request):
    current_user = request.user
    print('current_user', current_user)

print('dgfsdgsad')
