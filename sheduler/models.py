# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import (AbstractBaseUser,
                                        BaseUserManager,
                                        PermissionsMixin)
from django.db import models
from rest_framework.authtoken.models import Token
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


# Create your models here.

class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        now = timezone.now()
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False,
                                 **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True,
                                 **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
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
    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Designates whether the user'
                                               ' can log into this admin '
                                               'site.'))
    is_active = models.BooleanField(_('active'), default=True,
                                    help_text=_('Designates whether this user'
                                                ' should be treated as '
                                                'active. Unselected this '
                                                'instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    #
    # def get_absolute_url(self):
    #     return "/users/%s/" % urlquote(self.email)

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Returns the short name for the user."""
        return self.first_name

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
