from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view # get요청만 처리함

from .serializers import BookSerializer
from rest_framework import status

from .models import Book
# Create your views here.


def ajax(request):
    return render(request,'ajax.html')



# GET 요청만 처리
@api_view(['GET'])
def helloAPI(request):
    return Response('Hello REST API')


@api_view(['GET', 'POST'])
def booksAPI(request):

    # 전송 방식을 확인하는 방법은 request.method를 확인하면 된다.
    if request.method == 'GET':
        # 전체 데이터 가져오기
        books = Book.objects.all()
        serializer = BookSerializer(books,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    elif request.method == 'POST':
        #   클라이언트가 전송한 데이터를 Model이 사용할 수 있는 데이터로 변환
        serializer = BookSerializer(data=request.data)
    # print("1") # 이 코드가 실행이 안되면 URL 과 method 연결 실수


    # 유효성 검사
    if serializer.is_valid():
        # print("321") # 이 코드가 안 찍힌다면, 이름이 잘못된것

        serializer.save() # 데이터를 저장
        
        # 성공했을 때, 전송한 데이터를 다시 전송
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
    # 실패했을 때의 처리
    Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# 기본키를 가지고 데이터를 1개 찾아오는데, 없으면 404 에러를 발생시킨다.
from rest_framework.generics import get_object_or_404
@api_view(['GET'])
def bookAPI(request,bid): # bid를 받아서 처리.
    
    # 기본키를 가지고 데이터 1개 가져오기
    book = get_object_or_404(Book,bid=bid)
    serializer = BookSerializer(book)
    return Response(serializer.data, status=status.HTTP_200_OK)
