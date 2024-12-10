from django.http import JsonResponse
from django.views.generic import ListView
from django.db.models import Q
from django.core.paginator import Paginator
from questions.models import Question
from quizes.forms.enem_quiz_question_form import QuestionForm

class EnemMathQuizAjaxListView(ListView):
    model = Question
    quiz_subject_id = 2
    template_name = 'quizes/enem/enem_math_ajax.html'
    paginate_by = 50

    def get_queryset(self):
        queryset = Question.objects.filter(quiz_subject=self.quiz_subject_id)
        form = QuestionForm(self.request.GET)
        if form.is_valid():
            filter_by = form.cleaned_data.get("filter_by")
            search_term = form.cleaned_data.get("search_term")

            if filter_by == "year":
                queryset = queryset.filter(year__icontains=search_term)
            elif filter_by == "word":
                queryset = queryset.filter(
                    Q(context__icontains=search_term) |
                    Q(question__icontains=search_term)
                )
            elif filter_by == "id":
                queryset = queryset.filter(id=search_term)
        return queryset

    def render_to_response(self, context, **response_kwargs):
        # Verifica se a requisição é AJAX
        if self.request.headers.get("x-requested-with") == "XMLHttpRequest":
            questions = context["object_list"]

            # Paginação
            page = self.request.GET.get("page", 1)  # Obtém a página atual
            paginator = Paginator(questions, self.paginate_by)
            page_obj = paginator.get_page(page)

            questions_data = []
            for question in page_obj.object_list:
                answers = question.get_answers()
                question_images = question.get_image_urls()  # Lista de URLs das imagens da pergunta

                # Adicionando os dados de cada pergunta no JSON
                questions_data.append({
                    "id": question.id,
                    "context": question.context,
                    "question": question.question,
                    "year": question.year,
                    "images": question_images,  # Imagens da pergunta
                    "answers": [
                        {
                            "id": answer.question_id,
                            "text": answer.text,
                            "is_correct": answer.is_correct,
                            "images": [answer.answer_image] if answer.answer_image else [],
                            "alternative": answer.alternative
                        }
                        for answer in answers
                    ],
                })

     
            # Retorna os dados paginados no JSON
            return JsonResponse(
                {
                    "questions": questions_data,
                    "current_page": page_obj.number,
                    "total_pages": paginator.num_pages,
                    "total_questions": paginator.count,
                },
                status=200,
            )

        # Resposta padrão para requisições não-AJAX
        return super().render_to_response(context, **response_kwargs)
