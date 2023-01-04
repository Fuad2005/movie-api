from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import Movie, MovieSerializer, Review, ReviewSerializer
from rest_framework import status, generics
from django.shortcuts import get_object_or_404

@api_view(['GET', 'POST'])
def movie_list(request):
    movies = Movie.objects.all()
    if request.method == 'GET':
        serializer = MovieSerializer(instance=movies, many=True, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE',])
def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'GET':
        serializer = MovieSerializer(instance=movie, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = MovieSerializer(instance=movie, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class ReviewListAV(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()

class ReviewDetailAV(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()