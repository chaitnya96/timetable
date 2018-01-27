# -*- coding: utf-8 -*-

from django.db import models


class FType(models.Model):
    faculty_type = models.CharField(max_length=250)

    def __str__(self):
        return self.faculty_type


class Faculty(models.Model):
    Name = models.CharField(max_length=200)
    Qualification = models.CharField(max_length=300)
    faculty_type = models.ForeignKey(FType)

    def __str__(self):
        return self.Name
