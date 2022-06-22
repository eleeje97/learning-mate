from django.contrib import admin
from .models import QnA, QnA_answer, Quiz, result

admin.site.register(QnA)
admin.site.register(QnA_answer)
admin.site.register(Quiz)
admin.site.register(result)

