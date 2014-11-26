from __future__ import unicode_literals

from .views import SupervisorCRUDL

urlpatterns = SupervisorCRUDL().as_urlpatterns()