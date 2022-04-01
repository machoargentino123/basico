from django.urls import path
from prueba import views


app_name = 'luces_app'

urlpatterns = [
    path("list/",views.ListPruebaAPIView.as_view(),name="prueba_list"),
    path("estado/<int:pk>/",views.EstadoAPIView.as_view(),name="estado"),
    path("create/", views.CreatePruebaAPIView.as_view(),name="prueba_create"),
    path("update/<int:pk>/",views.UpdatePruebaAPIView.as_view(),name="update_prueba"),
    path("delete/<int:pk>/",views.DeletePruebaAPIView.as_view(),name="delete_prueba"),
    path("luces2/",views.LucesListView2.as_view(),name="Luces2"),
    path("editar/<int:pk>/",views.FormularioListView.as_view(),name="editar"),
    path("formulario2/",views.FormularioListView2.as_view(),name="formulario2"),
    path("luces/",views.LucesListView3.as_view(),name="Luces"),
    path("list2/",views.ListPruebaAPIView2.as_view(),name="prueba_list2"),
    path("panel/",views.PanelView.as_view(),name="panel"),
    ##Aca van las vistas del logger.
    path("logger/",views.ListLoggerAPIView.as_view(),name="logger"),
    path("logger/create/",views.CreateLoggerAPIView.as_view(),name="logger_create"),

]

