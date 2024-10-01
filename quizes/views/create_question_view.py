from django.views.generic import CreateView
from django.urls import reverse_lazy
from questions.models import Question, Answer
from quizes.forms.question_answer_form import QuestionForm, AnswerForm

class QuestionCreateView(CreateView):
    model = Question
    form_class = QuestionForm  
    template_name = 'quizes/teacher_question/create_question.html'
    success_url = reverse_lazy('quizes:list-questions')

    def post(self, request, *args, **kwargs):
        question_form = self.get_form()
        answer_forms = [
            {
                'text': request.POST.get(f'answer_text_{i}'),
                'is_correct': request.POST.get(f'answer_is_correct_{i}') == 'on',  
                'alternative': request.POST.get(f'answer_alternative_{i}')
            }
            for i in range(1, 5)  
        ]

        if question_form.is_valid():
            question = question_form.save()  

            for answer_data in answer_forms:
                if answer_data['text']:  
                    Answer.objects.create(question=question, **answer_data)

            return self.form_valid(question_form)

        return self.form_invalid(question_form)
