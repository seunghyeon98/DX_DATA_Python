from django.shortcuts import render

# Create your views here.

from app0726.models import Item

def index(request):
    # 전체 데이터 가져오기
    data = Item.objects.all()
    print(data)
    for temp in data:
        print(temp)
    # 필터링
    # data = Item.objects.filter(price = 1000)

    return render(request,'index.html',{'data':data})



# url 뒤에 붙은 파라미터는 2번째 매개변수를 이용해서 가져온다.
def detail(request,itemid):
    item = Item.objects.get(itemid = itemid)
    return render(request,'detail.html',{'item':item})