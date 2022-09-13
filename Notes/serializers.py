from rest_framework import serializers
from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    models = Note
    fields = '__all__'
