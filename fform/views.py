from django.shortcuts import render
from fform.models import Post
from fform.serializers import PostSerializer
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from django.http import Http404
def home(request):
	return render(request,'post.html')
def postnew(request):
	return render(request,'post_list.html')
def postnew1(request):
	return render(request,'post_list1.html')
def postnew2(request):
	return render(request,'post_list2.html')
def postnew3(request):
	return render(request,'post_list3.html')
class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)
@csrf_exempt
def post_detail(request,pk):
	try:
		post = Post.objects.get(pk=pk)
	except Author.DoesNotExists:
		return HttpResponse(status=404)
        if request.method == 'GET':
               serializer = PostSerializer(post)
               return JSONResponse(serializer.data)
     
        elif request.method == 'PUT':
            data = JSONParser().parse(request)
            serializer = PostSerializer(post, data=data)
            if serializer.is_valid():
                 serializer.save()
                 return JSONResponse(serializer.data)
            return JSONResponse(serializer.errors, status=400)

        elif request.method == 'DELETE':
             post.delete()
             return HttpResponse(status=204)
@csrf_exempt
def post_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)
