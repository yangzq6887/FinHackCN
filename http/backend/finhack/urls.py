from rest_framework.routers import SimpleRouter
from django.urls import path
from .views import BacktestModelViewSet
from .tests import signal

router = SimpleRouter()
router.register("backtest", BacktestModelViewSet)

#path('my-view/', my_view, {'http_method': 'get'}, name='my-view-get'),
urlpatterns = [
    path('signal/', signal),
    # path("backtest/", BacktestModelViewSet.as_view({'get': 'list'}))
    # path("backtest/<int:id>", BacktestModelViewSet.as_view({'get': 'show'}))
]
urlpatterns += router.urls