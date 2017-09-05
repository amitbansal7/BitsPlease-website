from django.db import models

LEVEL_CHOICES = (
    ("easy", "Easy"),
    ("medium", "Medium"),
    ("hard", "Hard")
)

DIVISION_CHOICES = (
    ('div1', "Div 1"),
    ('div2', "Div 2")
)

STATUS_CHOICES = (
    ('public', "Public"),
    ('private', "Private")
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
    status = models.CharField(max_length=20, default="Private", choices=STATUS_CHOICES)
    contest_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Question(models.Model):
    contest = models.ForeignKey(Contest, blank=True, null=True, related_name='questions')
    tag = models.ManyToManyField(Tag, blank=True, null=True, related_name='problems')
    name = models.CharField(max_length=200)
    description = models.TextField()
    level = models.CharField(max_length=50, choices=LEVEL_CHOICES)
    status = models.CharField(max_length=20, default="Private", choices=STATUS_CHOICES)
    answer = models.URLField(max_length=500, blank=True, default=None)
    add_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
