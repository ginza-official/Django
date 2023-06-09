from django.urls import path
from .views import *

urlpatterns = [
    path("", UserListView.as_view()),  # list all users
    path("<int:pk>", UserbyID.as_view()),  # find user by id
    path("search/", UsernameListSearch.as_view()),  # find user by username
    path("search/<str:username>", UsernameSearch.as_view()),  # user search by username retriveview
    path("filter/", UserFilter.as_view()),  # user search by custom filterset class
    path("custom/", CustomFilter.as_view()),  # custom dynamic filter
    # product section
    path("product/list", ProductListView.as_view()),  # list all products and filter
    path("product/price/", ProductFilterView.as_view()),  # list all products

]
