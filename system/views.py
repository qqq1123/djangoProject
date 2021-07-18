from django import http
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from system.models import Slider


def slider_list(requset):
    """
    轮播图接口
    {
        "meta": {},
        "objects": []
    }
    :param requset:
    :return:
    """
    data = {
        'meta': {

        },
        'objects': []
    }
    queryset = Slider.objects.filter(is_valid=True)
    for item in queryset:
        data['objects'].append({
            'id': item.id,
            'img_url': item.img.url,
            'target_url': item.target_url,
            'name': item.name
        })
    # return HttpResponse('ok')
    return http.JsonResponse(data)