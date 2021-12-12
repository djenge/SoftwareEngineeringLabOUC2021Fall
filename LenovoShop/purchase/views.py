from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from LenovoShop.purchase.models import Item


# 获取商品的所有评论
def get_comments(request):
    item_id = request.GET.get('item_id')
    if item_id is not None:
        item = Item.objects.get(item_id=item_id)
        comments = item.item_comments_set.all()
        json_data = []
        for comment in comments:
            result = {}
            result['user_name'] = comment[0]
            result['comment_body'] = comment[1]
            result['comment_time'] = comment[2]
            ###新加在comment中的可在这继续添加
            ###
            ###
            json_data.append(result)
        return JsonResponse(json_data)
    else:
        return JsonResponse({'error': '查找商品失败！'})
