from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Blog
from .serializers import BlogSerializer
from .permissions import BlogPermission


class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated, BlogPermission]

    def get_queryset(self):
        user = self.request.user

        if user.is_admin:
            return Blog.objects.all()

        if user.is_author:
            return Blog.objects.filter(author=user)

        if user.is_reader:
            return Blog.objects.filter(is_published=True)

        return Blog.objects.none()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=["post"])
    def publish(self, request, pk=None):
        blog = self.get_object()

        if not request.user.is_admin and blog.author != request.user:
            return Response({"error": "Not allowed"}, status=403)

        blog.is_published = True
        blog.save()

        return Response({"message": "Blog published successfully"})

    @action(detail=False, methods=["get"])
    def my_blogs(self, request):
        blogs = Blog.objects.filter(author=request.user)
        serializer = self.get_serializer(blogs, many=True)
        return Response(serializer.data)
