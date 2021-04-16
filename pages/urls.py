from django.urls import path
from pages.views import base, BooksApi, BooksApiById, funcbased, funcbasedid


urlpatterns = [

    path('', base, name='base'),


    path('api/books', BooksApi.as_view(), name='apibooks1'),

    path('api/books/', BooksApi.as_view(), name='apibooks2'),

    path('api/books/<int:id>', BooksApiById.as_view(), name='apibooksid1'),

    path('api/books/<int:id>/', BooksApiById.as_view(), name='apibooksid2'),


    path("funcbased/api/books", funcbased, name='funcbased1'),

    path("funcbased/api/books/", funcbased, name='funcbased2'),

    path("funcbased/api/books/<int:id>", funcbasedid, name='funcbasedid1'),

    path("funcbased/api/books/<int:id>/", funcbasedid, name='funcbasedid2'),

]
