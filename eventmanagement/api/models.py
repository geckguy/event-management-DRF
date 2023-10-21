from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _

class College(models.Model):
    code = models.CharField(max_length=20, unique=True, default='')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Student(models.Model):
    user = models.OneToOneField('api.CustomUser', on_delete=models.CASCADE,default=1)
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20)
    college = models.ForeignKey(College, on_delete=models.CASCADE)

class Event(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    college = models.ForeignKey(College, on_delete=models.CASCADE)

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    college = models.ForeignKey(College, on_delete=models.CASCADE)  # Link user to College
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Define related_name to avoid clashes
    groups = models.ManyToManyField(Group, blank=True, related_name='customuser_set')
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='customuser_set',
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'college']

    def __str__(self):
        return self.email
