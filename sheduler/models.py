# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from rest_framework.authtoken.models import Token


# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("User must have an email")

        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)
        Token.objects.create(user=user)
        return user

    def create_superuser(self, email, password):

        if not (email or password):
            raise ValueError("Super user must have an email and password")
        user = self.create_user(email, password)
        user.is_admin = True
        user.save()


class User(AbstractBaseUser):
    """this class represents the user Model.
    """

    class Meta:
        db_table = 'users'
        managed = True

    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=254, unique=True)
    country_code = models.IntegerField(blank=True, null=True)
    contact_no = models.BigIntegerField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    is_password_changed = models.BooleanField(default=False)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)

    USERNAME_FIELD = 'email'
    objects = UserManager()

    def __unicode__(self):
        return self.email

    def get_my_token(self):
        return Token.objects.get(user=self.objects)

    my_token = property(get_my_token)


class UserResetPassword(models.Model):
    class Meta:
        db_table = 'user_reset_password'

    users = models.OneToOneField(User)
    is_valid_key = models.BooleanField(default=False)
    key = models.CharField(max_length=40, blank=True)
    key_expires = models.DateTimeField()

    def __unicode__(self):
        return self.email


class FacultyType(models.Model):
    faculty_type = models.CharField(max_length=250)

    def __str__(self):
        return self.faculty_type


class Faculty(models.Model):
    name = models.CharField(max_length=200)
    Qualification = models.CharField(max_length=300, default='MCA')
    faculty_type = models.ForeignKey(FacultyType)

    def __str__(self):
        return self.name


class Semester(models.Model):
    semester_number = models.IntegerField()
    division = models.CharField(max_length=1)
    class_location = models.CharField(max_length=50)

    def __str__(self):
        return 'Semester-'+str(
            self.semester_number) + ', ' + 'Division-' + str(
            self.division) + ', ' + str(self.class_location)


class Subject(models.Model):
    subject_code = models.CharField(max_length=50)
    subject_name = models.CharField(max_length=250)
    semester = models.IntegerField()
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
    MONDAY = 'Monday'
    TUESDAY = 'Tuesday'
    WEDNESDAY = 'Wednesday'
    THURSDAY = 'Thursday'
    FRIDAY = 'Friday'
    SATURDAY = 'Saturday'
    SUNDAY = 'Sunday'

    day_choice = (
        (MONDAY, 'Monday'),
        (TUESDAY, 'Tuesday'),
        (WEDNESDAY, 'Wednesday'),
        (THURSDAY, 'Thursday'),
        (FRIDAY, 'Friday'),
        (SATURDAY, 'Saturday'),
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
