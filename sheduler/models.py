# -*- coding: utf-8 -*-

from django.db import models


class Faculty_Type(models.Model):
    faculty_type = models.CharField(max_length=250)

    def __str__(self):
        return self.faculty_type


class Faculty(models.Model):
    name = models.CharField(max_length=200)
    Qualification = models.CharField(max_length=300, default='MCA')
    faculty_type = models.ForeignKey(Faculty_Type)

    def __str__(self):
        return self.name


class Semester(models.Model):
    sem_no = models.IntegerField()
    division = models.CharField(max_length=1)
    class_location = models.CharField(max_length=50)

    def __str__(self):
        return 'Semester-'+str(self.sem_no) + ', ' + 'Division-' + str(self.division) + ', ' + str(self.class_location)


class Subject(models.Model):
    subject_code = models.CharField(max_length=50)
    subject_name = models.CharField(max_length=250)
    semester = models.ForeignKey(Semester)
    faculty = models.ForeignKey(Faculty)
    credits = models.IntegerField(default=0)

    def __str__(self):
        return self.subject_code + ' - ' + self.subject_name


class Lecture(models.Model):
    lecture_no = models.IntegerField()
    from_time = models.TimeField()
    to_time = models.TimeField()

    def __str__(self):
        return str(self.from_time) + '-  to  -' + str(self.to_time)


class Timetable(models.Model):
    Monday = 'Monday'
    Tuesday = 'Tuesday'
    Wednesday = 'Wednesday'
    Thursday = 'Thursday'
    Friday = 'Friday'
    Saturday = 'Saturday'
    Sunday = 'Sunday'

    day_choice = (
        (Monday, 'Monday'),
        (Tuesday, 'Tuesday'),
        (Wednesday, 'Wednesday'),
        (Thursday, 'Thursday'),
        (Friday, 'Friday'),
        (Saturday, 'Saturday'),
    )
    day = models.CharField(
        choices=day_choice,
        max_length=10,
    )
    lecture = models.ForeignKey(Lecture)
    semester = models.ForeignKey(Semester)
    subject = models.ForeignKey(Subject)

    def __str__(self):
        return str(self.semester)
