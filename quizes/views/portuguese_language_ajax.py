from django.http import JsonResponse
from django.views.generic import ListView
from django.db.models import Q
from django.core.paginator import Paginator
from questions.models import Question
from quizes.forms.enem_quiz_question_form import QuestionExamForm

class PortugueseLanguageQuizAjaxListView(ListView):
    model = Question
    quiz_subject_id = 5
    template_name = 'quizes/exams/portuguese_language_quiz_ajax.html'
    paginate_by = 50

    def get_queryset(self):
        queryset = Question.objects.filter(quiz_subject=self.quiz_subject_id)
        form = QuestionExamForm(self.request.GET)
        if form.is_valid():
            filter_by = form.cleaned_data.get("filter_by")
            search_term = form.cleaned_data.get("search_term")

            if filter_by == "examining_board":
                queryset = queryset.filter(examining_board__icontains=search_term)
            elif filter_by == "word":
                queryset = queryset.filter(
                    Q(context__icontains=search_term) |
                    Q(question__icontains=search_term)
                )
            elif filter_by == "id":
                queryset = queryset.filter(id=search_term)
        return queryset

    def render_to_response(self, context, **response_kwargs):
        if self.request.headers.get("x-requested-with") == "XMLHttpRequest":
            questions = context["object_list"]

            page = self.request.GET.get("page", 1)  
            paginator = Paginator(questions, self.paginate_by)
            page_obj = paginator.get_page(page)

            questions_data = []
            for question in page_obj.object_list:
                answers = question.get_answers()
                question_image_url = question.question_image.url if question.question_image else None

                questions_data.append({
                    "id": question.id,
                    "context": question.context,
                    "question": question.question,
                    "year": question.year,
                    "examining_board": question.examining_board,
                    "question_image": question_image_url,  # Adiciona a URL da imagem
                    "answers": [
                 
                        
                        {
                            "id": answer.question_id,
                            "text": answer.text,
                            "is_correct": answer.is_correct,
                            "alternative": answer.alternative,
                            "answer_image": answer.answer_image.url if answer.answer_image else None,
                        }
                        for answer in answers
                    ],
                })

            return JsonResponse(
                {
                    "questions": questions_data,
                    "current_page": page_obj.number,
                    "total_pages": paginator.num_pages,
                    "total_questions": paginator.count,
                },
                status=200,
            )

        return super().render_to_response(context, **response_kwargs)
