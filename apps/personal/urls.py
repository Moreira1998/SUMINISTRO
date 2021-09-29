from django.urls import path, include
from apps.personal.viewsets import PersonalViewSet, RolViewSet
from rest_framework.routers import DefaultRouter
from apps.personal.views import PersonalList, PersonalNew, PersonalUpdate, PersonalDelete

# -------------------------------------------------------->
# Routers ApI
routers = DefaultRouter()
routers.register(r'', PersonalViewSet)
routers.register(r'role', RolViewSet)

app_name = 'personal'

urlpatterns = [

    # -------------------------------------------------------->
    # Path Routers API
    path('api/', include(routers.urls)),

    # -------------------------------------------------------->
    # Path Personal

    path('personalList', PersonalList.as_view(), name='personal_list'),
    path('personalNew', PersonalNew.as_view(), name='personal_new'),
    path('personalUpdate/<str:pk>', PersonalUpdate.as_view(), name='personal_update'),
    path('personalDelete/<str:pk>', PersonalDelete.as_view(), name='personal_delete'),

]
