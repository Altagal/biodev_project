from django.urls import path, include
from embriao import views

urlpatterns = [
    #BOTIJAO
    path('botijoes', views.botijao_list, name='botijao_list'),
    path('criar-botijao', views.botijao_create, name='botijao_create'),
    path('editar-botijao/<int:pk>', views.botijao_update, name='botijao_update'),
    path('deletar-botijao/<int:pk>', views.botijao_delete, name='botijao_delete'),
    
    #CANECO
    path('canecos', views.caneco_list, name='caneco_list'),
    path('criar-caneco', views.caneco_create, name='caneco_create'),
    path('editar-caneco/<int:pk>', views.caneco_update, name='caneco_update'),
    path('deletar-caneco/<int:pk>', views.caneco_delete, name='caneco_delete'),

    path('hacks', views.hack_list, name='hack_list'),
    path('criar-hack', views.hack_create, name='hack_create'),
    path('editar-hack/<int:pk>', views.hack_update, name='hack_update'),
    path('deletar-hack/<int:pk>', views.hack_delete, name='hack_delete'),
    
    path('palhetas', views.palheta_list, name='palheta_list'),
    path('criar-palheta', views.palheta_create, name='palheta_create'),
    path('editar-palheta/<int:pk>', views.palheta_update, name='palheta_update'),
    path('deletar-palheta/<int:pk>', views.palheta_delete, name='palheta_delete'),
]
