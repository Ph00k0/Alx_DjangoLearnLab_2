from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from .models import CustomUser

@permission_required('your_app.can_edit', raise_exception=True)
def edit_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    # Logic to edit the user
    return render(request, 'edit_user.html', {'user': user})
