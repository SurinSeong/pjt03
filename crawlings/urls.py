from django.urls import path
from . import views

app_name = 'crawlings'
urlpatterns = [
    path('index/', views.index, name='index'),    # 사용자 입력받아서 종목 토론 데이터 검색하기 -> 검색한 결과(토론 목록)을 출력
    path('delete_comment/', views.delete_comment, name='delete_comment'),    # 댓글 목록에서 하나 삭제

]
