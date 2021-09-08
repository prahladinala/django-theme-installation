from django.contrib import admin
from django.urls import path, include

from django.conf import settings # GET SETTINGS HERE
from django.conf.urls.static import static # TO CREATE URLs FOR STATIC FILES
# from django.http import HttpResponse
# urlpatters > list
# list item syntax > path('PATH/', FUNCTION TO RUN)

# FUNCTION THAT RETURNS SOME DATA
# def projects(request):
#     return HttpResponse('Here are our projects')

# def project(request, pk):
#     return HttpResponse('Single Project' + ' ' + str(pk))

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('projects.urls'))
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# GO TO URL http://localhost:8000/projects/
# As there is no home route/path so http://localhost:8000/ > return 404

# path('project/<str:pk>', project, name="project")
# REASON FOR str > in  long term in project we may use the id for UUID > basically number and letters
# path('project/<int:prahlad>', project, name="project") > def project(request, prahlad):
# path('project/<slug:madam>', project, name="project") > def project(request, madam):


# path('',include('projects.urls')) > include all the urls in <APP NAME>.urls ie here projects.urls