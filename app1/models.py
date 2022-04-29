from django.db import models

class Student(models.Model):
    ism = models.CharField(max_length=30)
    yosh = models.PositiveSmallIntegerField()
    nechinchi_kurs = models.PositiveSmallIntegerField()
    student_raqami = models.PositiveSmallIntegerField(unique=True)
    def __str__(self):
        return self.ism

class Reja(models.Model):
    sarlavha = models.CharField(max_length=30)
    sana = models.PositiveSmallIntegerField()
    batafsil = models.CharField(max_length=50, blank=True)
    bajarildi = models.BooleanField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    def __str__(self):
        return self.sarlavha


