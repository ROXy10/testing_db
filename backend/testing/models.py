from datetime import date

from django.db import models
from django.conf import settings


class Test(models.Model):
    test_title = models.CharField(max_length=255, verbose_name="Тема тестування")
    is_active = models.BooleanField(default=False, verbose_name="Активний")

    class Meta(object):
        verbose_name = "Тема тестування"
        verbose_name_plural = "Теми тестування"

    def __str__(self):
        return self.test_title


class Question(models.Model):
    question_title = models.TextField(verbose_name="Запитання")
    test = models.ForeignKey(Test, on_delete=models.CASCADE, null=True, verbose_name="Тема тестування")
    multi = models.BooleanField(default=False, verbose_name="Кілька відповідей")

    class Meta(object):
        verbose_name = "Запитання"
        verbose_name_plural = "Запитання"

    def __str__(self):
        return self.question_title


class Answer(models.Model):
    answer_title = models.TextField(verbose_name="Відповідь")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, verbose_name="Запитання")
    correct = models.BooleanField(default=False, verbose_name="Правильність")

    class Meta(object):
        verbose_name = "Відповідь"
        verbose_name_plural = "Відповіді"

    def __str__(self):
        return self.answer_title


class Testing(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False,  default=date.today, verbose_name="Дата")
    test = models.ForeignKey(Test, on_delete=models.CASCADE, null=True, verbose_name="Тема тестування")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, null=True, verbose_name="Користувач")
    result = models.BooleanField(default=False, verbose_name="Результат")

    class Meta(object):
        verbose_name = "Тестування"
        verbose_name_plural = "Результати тестів"

    def __str__(self):
        return '%s %s %s' % (self.date.strftime("%d.%m.%Y"), self.test, self.user)


class UserAnswer(models.Model):
    testing = models.OneToOneField(Testing, n_delete=models.CASCADE, null=True, verbose_name="Тестування")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, null=True, verbose_name="Користувач")
    question = models.ForeignKey(Question, n_delete=models.CASCADE, null=True, verbose_name="Запитання")
    answer = models.ForeignKey(Answer, n_delete=models.CASCADE, null=True, verbose_name="Відповідь")
    value = models.BooleanField(default=False, verbose_name="Значення відповіді")

    class Meta(object):
        verbose_name = "Відповіді користувача"
        verbose_name_plural = "Відповіді користувачів"

    def __str__(self):
        return self.testing