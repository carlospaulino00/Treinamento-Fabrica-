from rest_framework import routers
from nota_fiscal.views import PostoAtendimentoViewSet



router = routers.DefaultRouter()
router.register('', PostoAtendimentoViewSet)

urlpatterns = router.urls