from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from palak.views import budget,stage1,budget_stage1,update_stage1,updated_stage1,datatable,stages2,script_input,update_stage2_budget
app_name = 'palak'

urlpatterns = [
    path('',views.homepage,name="homepage"),
    path('script_info/',views.script_info,name="script_info"),
    path('character/',views.character,name="character"),
    path('screenplays/',views.screenplays,name="screenplays"),
    path('character_edit/',views.character_edit,name="character_edit"),
    path('budget/', views.budget, name="test"),
	url(r'^run-sh/$', views.index, name='run_sh'),
    path('check/', views.checkbox, name="check"),
	path('update/', views.update_budget, name="update"),
	path('datatable/', views.datatable, name="datatable"),
	path('updated/', views.updated_budget, name="update2"),
	path('stage2/', views.stages2, name="stages2"),
    # path('stage2/', views.stage1_saved, name="stage1_saved"),
	path('stage2/update', views.update_stage2, name="stage2.1"),
	path('update_2/', views.update_stage2_budget, name="update_stage2"),
	path('script/', views.script_input, name="script"),
	path('update/stage1', views.update_stage1, name="update1"),
	
	path('budget/stage1', views.stage1, name="stage1"),
	path('updated/stage1', views.updated_stage1, name="stage1.1"),
   
] 
