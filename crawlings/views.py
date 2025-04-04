from django.shortcuts import render, redirect, get_object_or_404

from .models import Stock, Comment
from .forms import CommentForm
from .utils import get_toss_data

# 사용자 입력을 받을 수 있도록 stock_finder.html 렌더링
def index(request):
    # 폼을 띄워서 검색할 수 있도록 한다.
    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        # 유효성 검사
        if form.is_valid():
            keyword = form.cleaned_data['stock_name']
            # 크롤링하기
            stock_name, stock_code, contents = get_toss_data(keyword)

            # DB에 있는지 확인하는 작업 필요!
            stock, created = Stock.objects.get_or_create(
                code=stock_code,
                defaults={'name': stock_name}    # 새롭게 생성할 때만 적용
            )

            if not created and stock.name != stock_name:    # 기존에 있던 내용이라면
                stock.name = stock_name
                stock.save()    # 저장

            # 댓글도 저장하기
            for content in contents:
                comment = Comment(stock=stock, content=content)
                comment.save()

            # 검색한 결과의 댓글 목록을 출력한다.
            comments = stock.comments.all()

            context = {
                'form': form,
                'stock': stock,
                'comments': comments,
            }
            
            return render(request, 'crawlings/stock_finder.html', context)
    else:
        form = CommentForm()
    context = {
        'form': form,
    }
    return render(request, 'crawlings/stock_finder.html', context)
    
    
# 특정 토론 데이터 삭제
def delete_comment(request):
    if request.method == 'POST':
        # 숨김 처리해서 가져온 데이터 받기기
        comment_pk = request.POST.get('comment_pk')
        stock_code = request.POST.get('stock_code')
        
        comment = get_object_or_404(Comment, pk=comment_pk)
        comment.delete()

        stock = get_object_or_404(Stock, code=stock_code)
        comments = stock.comments.all()

        form = CommentForm(data={'stock_name': stock.name})

        context = {
            'form': form,
            'stock' : stock,
            'comments': comments,
        }

        return render(request, 'crawlings/stock_finder.html', context)
