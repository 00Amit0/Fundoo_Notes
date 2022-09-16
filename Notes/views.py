import logging
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Note
from .serializers import NoteSerializer
from rest_framework import status

logging.basicConfig(filename='note_views.log', filemode='a', level=logging.DEBUG)


class NoteApp(APIView):

    def get(self, request):
        try:
            # notes = Note.objects.all()
            notes = Note.objects.filter(user_id=request.data.get("user_id"))
            serializer = NoteSerializer(notes, many=True)
            return Response({'data': serializer.data}, status.HTTP_200_OK)
        except Exception as e:
            logging.exception(e)
            return Response({'message': 'unexpected error'}, status=400)

    def post(self, request):
        try:
            serializer = NoteSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"message": "Data save successfully",
                             "data": serializer.data}, status.HTTP_201_CREATED)
        except Exception as e:
            logging.exception(e)
            return Response({"message": str(e)}, status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        try:
            notes = Note.objects.get(id=request.data.get('id'))
            print(notes)
            serializer = NoteSerializer(notes, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'data': serializer.data}, status.HTTP_201_CREATED)
        except Exception as e:
            logging.exception(e)
            return Response({'message': 'unexpected error'}, status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            notes = Note.objects.get(id=request.data.get('id'))
            notes.delete()
            return Response({'data': 'deleted'}, status.HTTP_204_NO_CONTENT)
        except Exception as e:
            logging.exception(e)
            return Response({'message': 'unexpected error'}, status.HTTP_400_BAD_REQUEST)
