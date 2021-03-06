from rest_framework.routers import DefaultRouter
from .views import UserView, PersonalbudgetView

router = DefaultRouter()
router.register(r'users', UserView, basename='user')
router.register(r'personalbudgets', PersonalbudgetView, basename='personalbudget')
urlpatterns = router.urls
