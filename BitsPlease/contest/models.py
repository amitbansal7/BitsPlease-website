from django.db import models
from django.urls import reverse

LEVEL_CHOICES = (
    ('easy', "Easy"),
    ('medium', "Medium"),
    ('hard', "Hard")
)

DIVISION_CHOICES = (
    ('div1', "Div 1"),
    ('div2', "Div 2")
)


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Contest(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    division = models.CharField(max_length=20, choices=DIVISION_CHOICES)
    winners = models.TextField(blank=True, default=None)
    publish = models.BooleanField(default=False)
    contest_date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("contest:contest_detail", kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class Question(models.Model):
    contest = models.ForeignKey('contest.Contest', blank=True, null=True, related_name='questions')
    tag = models.ForeignKey(Tag, blank=True, null=True, related_name='problems')
    name = models.CharField(max_length=200)
    description = models.TextField()
    level = models.CharField(max_length=50, choices=LEVEL_CHOICES)
    publish = models.BooleanField(default=False)
    answer = models.URLField(max_length=500, blank=True, default=None)
    add_date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("contest:problem_detail", kwargs={'pk': self.pk})

    def __str__(self):
        return self.name
