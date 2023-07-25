from django.contrib.auth.decorators import user_passes_test

from ColinaDoSol.models import User


def admin_required(view_func):
    actual_decorator = user_passes_test(
        lambda user: user.is_authenticated and (user.role == User.Role.ADMIN or user.is_superuser),
        login_url='/login'
    )
    return actual_decorator(view_func)

