from datetime import date

from django.db import models
from django.conf import settings


class Test(models.Model):
    test_title = models.CharField(max_length=512, verbose_name="Тема тесту")
    is_active = models.BooleanField(default=False, verbose_name="Активний")

    class Meta(object):
        verbose_name = u"Тема тестування"
        verbose_name_plural = u"Теми тестування"

    def __str__(self):
        return self.test_title


class Question(models.Model):
    question_title = models.CharField(max_length=512, verbose_name="Питання")
    multi = models.BooleanField(default=False, verbose_name="Кілька відповідей")
    test = models.ForeignKey(Test, on_delete=models.CASCADE, null=True, verbose_name="Тема теставання")

    class Meta(object):
        verbose_name = u"Питання"
        verbose_name_plural = u"Питання"

    def __str__(self):
        return self.question_title


class Answer(models.Model):
    answer_title = models.CharField(max_length=512, verbose_name="Відповідь")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, verbose_name="Питання")
    correct = models.BooleanField(default=False, verbose_name="Правильність")

    class Meta(object):
        verbose_name = u"Відповіді"
        verbose_name_plural = u"Відповіді"

    def __str__(self):
        return self.answer_title


class Testing(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False,  default=date.today, verbose_name="Дата")
    test = models.ForeignKey(Test, on_delete=models.CASCADE, null=True, verbose_name="Тема тесту")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, null=True, verbose_name="Користувач")
    result = models.BooleanField(default=False, verbose_name="Результат")

    class Meta(object):
        verbose_name = u"Результати теста"
        verbose_name_plural = u"Результати тестів"

    def __str__(self):
        return '%s %s %s' % (self.date.strftime("%d.%m.%Y"), self.test, self.user)