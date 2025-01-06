from rest_framework import serializers
from questions.models import Question, Answer

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'  

class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, write_only=True)  

    class Meta:
        model = Question
        fields = '__all__' 

    def create(self, validated_data):
        answers_data = validated_data.pop('answers', []) 
        question = Question.objects.create(**validated_data)
        for answer_data in answers_data:
            Answer.objects.create(question=question, **answer_data)
        return question
