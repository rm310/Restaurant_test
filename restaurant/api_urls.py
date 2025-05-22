from rest_framework.routers import DefaultRouter
from .views import DishesMenuSet

router = DefaultRouter
router.register(r'dishes', DishesMenuSet, basename = 'dishes_menu')

urlpatterns = router.urls