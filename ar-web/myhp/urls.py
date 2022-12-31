from django.urls import path
from .views import myhpListView, myhpDetailView, myhpCreateView, myhpUpdateFormView, myhpDeleteView
from .views import ImageUploadView
 
urlpatterns = [
     path("", myhpListView, name="myhp-list"),
     path("detail/<int:pk>/", myhpDetailView, name="myhp-detail"),
     path("create/", myhpCreateView, name="myhp-create"),
     path("update/<int:pk>/", myhpUpdateFormView, name="myhp-update"),
     path("delete/<int:pk>/", myhpDeleteView, name="myhp-delete"),
     path("image-upload/", ImageUploadView.as_view(), name="image-upload")
]

