from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest

# Create your views here.


def near_hundred(request, n) -> HttpResponse:
    return HttpResponse((abs(100 - n) <= 10) or (abs(200 - n) <= 10))


def string_splosion(request, str):
    num = 1
    new_str = ""
    for letter in str:
        new_str += str[:num]
        num += 1
    return HttpResponse(new_str)


def cat_dog(request, str):
    return HttpResponse(str.count("cat") == str.count("dog"))


def lone_sum(request, a, b, c):
    if a == b and b == c and c == a:
        return HttpResponse(0)
    if a == b:
        return HttpResponse(c)
    if a == c:
        return HttpResponse(b)
    if b == c:
        return HttpResponse(a)

    else:
        return HttpResponse(a + b + c)
