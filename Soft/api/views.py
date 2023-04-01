from django.shortcuts import render, get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Base, About, Gallery, OurProjects, HomeTitle, OurCoreServis
from rest_framework.views import APIView
from .serializers import BaseSerializer, AboutSerializer, GallerySerializer, OurProjectsSerializer, HomeTitleSerializer, OurCoreSevisSerializer, InfoDevSerializer
from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

# HomeTitle 

class HomeTitleSerializerAPI(APIView, PageNumberPagination):
    page_size = 3
    serializer_class = HomeTitleSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


    def get(self,request,*args,**kwargs):
        res = HomeTitle.objects.all()[:1]
        uzb = self.paginate_queryset(res, request, view=self)
        serializer = self.serializer_class(uzb, many=True)
        return Response(data=serializer.data)
    
    def post(self,request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)



# About
class AboutSerializerAPI(APIView, PageNumberPagination):
    page_size = 3
    serializer_class = AboutSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self,request,*args,**kwargs):
        res = About.objects.all()
        uzb = self.paginate_queryset(res, request, view=self)
        serializer = self.serializer_class(uzb, many=True)
        return Response(data=serializer.data)


    def post(self,request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

#Home Title Update
class HomeTitleUpdateSerializerAPI(APIView):
    serializer_class = GallerySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    

    def get(self, request, pk):
        res = get_object_or_404(HomeTitle, id=pk)
        serializer = self.serializer_class(res)
        return Response(data=serializer.data)
    

    def put(self, request,pk):
        data= request.data
        result = get_object_or_404(HomeTitle, id=pk)
        serializer =self.serializer_class(instance=result, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)
        

    def patch(self, request,pk):
        data= request.data
        a = get_object_or_404(HomeTitle, id=pk)
        serializer = self.serializer_class(instance=a, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)


    def delete(self, request,pk):
        de = get_object_or_404(HomeTitle, id=pk)
        de.delete()
        return Response(data={"deleted":"bases"}, status=status.HTTP_204_NO_CONTENT)
        


# About Update
class AboutUpdatedSerializer(APIView):
    serializer_class = AboutSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request, pk):
        res = get_object_or_404(About, id=pk)
        serializer = self.serializer_class(res)
        return Response(data=serializer.data)
    

    def put(self, request,pk):
        data= request.data
        result = get_object_or_404(About, id=pk)
        serializer =self.serializer_class(instance=result, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)
        

    def patch(self, request,pk):
        data= request.data
        a = get_object_or_404(About, id=pk)
        serializer = self.serializer_class(instance=a, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)


    def delete(self, request,pk):
        de = get_object_or_404(About, id=pk)
        de.delete()
        return Response(data={"deleted":"bases"}, status=status.HTTP_204_NO_CONTENT)
        


class GalerrySerializerAPI(APIView, PageNumberPagination):
    page_size = 3
    serializer_class = GallerySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self,request,*args,**kwargs):
        res = Gallery.objects.all()
        uzb = self.paginate_queryset(res, request, view=self)
        serializer = self.serializer_class(res, many=True)
        return Response(serializer.data)


    def post(self,request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


# Gallery update serializer
class GalleryUpdatedSerializer(APIView):
    serializer_class = GallerySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    

    def get(self, request, pk):
        res = get_object_or_404(Gallery, id=pk)
        serializer = self.serializer_class(res)
        return Response(data=serializer.data)
    

    def put(self, request,pk):
        data= request.data
        result = get_object_or_404(Gallery, id=pk)
        serializer =self.serializer_class(instance=result, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)
        

    def patch(self, request,pk):
        data= request.data
        a = get_object_or_404(Gallery, id=pk)
        serializer = self.serializer_class(instance=a, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)


    def delete(self, request,pk):
        de = get_object_or_404(Gallery, id=pk)
        de.delete()
        return Response(data={"deleted":"bases"}, status=status.HTTP_204_NO_CONTENT)
        


class OurProjectsSerializerAPI(APIView, PageNumberPagination):
    page_size = 3
    serializer_class = OurProjectsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self,request,*args,**kwargs):
        res = OurProjects.objects.all()
        uzb = self.paginate_queryset(res, request, view=self)
        serializer = self.serializer_class(uzb, many=True)
        return Response(data=serializer.data)


    def post(self,request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

class OurUpdatedSerializer(APIView):
    serializer_class = OurProjects
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request, pk):
        res = get_object_or_404(OurProjects, id=pk)
        serializer = self.serializer_class(res)
        return Response(data=serializer.data)
    

    def put(self, request,pk):
        data= request.data
        result = get_object_or_404(OurProjects, id=pk)
        serializer = self.serializer_class(instance=result, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)
        

    def patch(self, request,pk):
        data= request.data
        a = get_object_or_404(OurProjects, id=pk)
        serializer = self.serializer_class(instance=a, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)


    def delete(self, request,pk):
        de = get_object_or_404(OurProjects, id=pk)
        de.delete()
        return Response(data={"deleted":"bases"}, status=status.HTTP_204_NO_CONTENT)
        


class BaseSerializerAPI(APIView, PageNumberPagination):
    page_size = 3
    serializer_class = BaseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self,request,*args,**kwargs):
        res = Base.objects.all()
        uzb = self.paginate_queryset(res, request, view=self)
        serializer = self.serializer_class(uzb, many=True)
        return Response(data=serializer.data)

    def post(self,request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class BaseUpdatedSerializer(APIView):
    serializer_class = BaseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request, pk):
        res = get_object_or_404(Base, id=pk)
        serializer = self.serializer_class(res)
        return Response(data=serializer.data)
    

    def put(self, request,pk):
        data= request.data
        result = get_object_or_404(Base, id=pk)
        serializer =self.serializer_class(instance=result, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)
        

    def patch(self, request,pk):
        data= request.data
        a = get_object_or_404(Base, id=pk)
        serializer = self.serializer_class(instance=a, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)


    def delete(self, request,pk):
        de = get_object_or_404(Base, id=pk)
        de.delete()
        return Response(data={"deleted":"bases"}, status=status.HTTP_204_NO_CONTENT)
        
# OurServis
class OurCoreSevisSerializerAPI(APIView, PageNumberPagination):
    page_size = 3
    serializer_class = OurCoreSevisSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self,request,*args,**kwargs):
        res = OurCoreServis.objects.all()
        uzb = self.paginate_queryset(res, request, view=self)
        serializer = self.serializer_class(uzb, many=True)
        return Response(data=serializer.data)

    def post(self,request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

#OurCoreServisUpdate
class OurCoreSevisUpdateSerializerAPI(APIView):
    serializer_class = OurCoreSevisSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request, pk):
        res = get_object_or_404(OurCoreServis, id=pk)
        serializer = self.serializer_class(res)
        return Response(data=serializer.data)
    

    def put(self, request,pk):
        data= request.data
        result = get_object_or_404(OurCoreServis, id=pk)
        serializer =self.serializer_class(instance=result, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)
        

    def patch(self, request,pk):
        data= request.data
        a = get_object_or_404(OurCoreServis, id=pk)
        serializer = self.serializer_class(instance=a, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)


    def delete(self, request,pk):
        de = get_object_or_404(OurCoreServis, id=pk)
        de.delete()
        return Response(data={"deleted":"Ourcore"}, status=status.HTTP_204_NO_CONTENT)
        