from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Posts
from .serializers import PostsSerializer
from rest_framework import status
from . models import Posts
from rest_framework.pagination import PageNumberPagination

# Create your views here.

@api_view(['GET'])
def home(request):
    print(request.method)
    return Response({'name': 'Nairaland'})

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def testing(request):
    if request.method == 'GET':
        return Response({'message': 'Hello, this ia a get request'})
    elif request.method == 'POST':
        return Response({'message': 'Hello, this ia a post request'})

    return Response({'Info': 'Welcome'})

@api_view(['GET'])
def all_posts(request):
    posts = Posts.objects.all()
    paginator = PageNumberPagination()
    paginator.page_size = 10
    paginated_posts = paginator.paginate_queryset(posts, request)
    serializer = PostsSerializer(paginated_posts, many=True)
    # return Response(data=serializer.data, status=status.HTTP_200_OK)
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def create_post(request):
    if request.method == 'GET':
        return Response({'message': 'Daniel Provide Information'})
    elif request.method == 'POST':
        post = request.data
        author = request.user
        serializer = PostsSerializer(data=post, many=False)
        if serializer.is_valid():
            serializer.save(author=author)
            return Response({'message': 'Post Created Successfully!', 'status': True},status=status.HTTP_201_CREATED)
        else:
            return Response({
                'message': 'Something Went Wrong', 'status': False}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def edit_post(request, id):
    if request.method == 'GET':
        post = Posts.objects.get(id=id)
        serializer = PostsSerializer(post, many=False)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        post = Posts.objects.get(id=id)
        serializer = PostsSerializer(instance=post, data=request.data, many=False)
        if serializer.is_valid():
            serializer.save()
        return Response({
            'message': 'Post Updated Successfully', 'status': True}, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        post = Posts.objects.get(id=id)
        post.delete()
        return Response({
            'message': 'Post Deleted Successfully', 'status': True}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserPosts(request):
    author = request.user
    getUser = Posts.objects.filter(author=author)
    serializer = PostsSerializer(getUser, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def trendingView(request):
    if request.method == 'GET':
        post = Posts.objects.filter(trending=True)
        serializer = PostsSerializer(post, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    

@api_view(['GET'])
def latestPosts(request):
    if request.method == 'GET':
        post = Posts.objects.all().order_by('-created_at')
        serializer = PostsSerializer(post, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)   


#imports all the photos and save it on the database

@api_view(['GET'])
def images(request):
    photo = Posts.objects.all()
    cloudinary_img = {'photo':photo}
    return render(request, '', cloudinary_img)
    
@api_view(['GET'])
def Post_tags(request, tag):
    Posttags = Posts.objects.filter(tags=tag)
    paginator=PageNumberPagination()
    paginator.page_size=5
    tagger=paginator.paginate_queryset(Posttags, request)
    serializer= PostsSerializer(tagger, many=True)
    return paginator.get_paginated_response(serializer.data)











