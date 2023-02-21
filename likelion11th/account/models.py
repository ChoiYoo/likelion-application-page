from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)


'''학년 정보 선택 상자'''
GRADE_CHOICES = (
    ("1","1학년"),
    ("2","2학년"),
    ("3","3학년"),
    ("4","4학년"),
)


class UserManager(BaseUserManager):
    def create_user(self, email, password, name, student_num, phone_num, first_major):
        if not email:
            raise ValueError(("Users must have an email address"))
        user = self.model(
            email=self.normalize_email(email),
            name=name, 
            student_num=student_num, 
            phone_num=phone_num, 
            first_major=first_major,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password, name, student_num, phone_num, first_major):
        user = self.create_user(
            email=email,
            password=password,
            name=name, 
            student_num=student_num, 
            phone_num=phone_num, 
            first_major=first_major,

        )

        user.is_superuser = True
        user.save()

        return user

class User(AbstractBaseUser, PermissionsMixin):
    """Model definition for User."""

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ['name','student_num','phone_num','first_major']

    objects = UserManager()

    email = models.EmailField(
        verbose_name=("email"),
        max_length=200,
        unique=True,
    )

    name = models.CharField(
        max_length=20,
        verbose_name="이름",
    )

    student_num = models.CharField(
        verbose_name="학번",
        max_length=30,
        unique=True,
    )

    grade = models.CharField(
        max_length=10,
        choices = GRADE_CHOICES,
        default="1",
        verbose_name="학년",
    )
    phone_num = models.CharField(
        max_length=20,
        verbose_name="휴대폰 번호",
    )

    first_major = models.CharField(
        max_length=30,
        verbose_name="본전공",
    )

    second_major = models.CharField(
        max_length=30,
        verbose_name="이중전공",
        null=True,
        blank=True,
    )

    is_accepted = models.BooleanField(
        default = False,
        verbose_name="합격 여부",
    )

    is_active = models.BooleanField(
        verbose_name=("Is active"),
        default=True,
    )

    # email field와 역할이 겹치는 면이 있는 것 같아 임시로 주석처리 하였습니다.
    # 기능상으로는 username이나 email중 어느 쪽을 사용해도 동일하니, 혹시라도 username이 꼭 필요한 것 같다는 의견이 있을시 수정하겠습니다.

    # username = models.CharField(
    #     verbose_name=("username"),
    #     max_length=50,
    #     unique=True,
    # ) 

    #class User(AbstractBaseUser, PermissionsMixin) 에서의 permissionmixin 에서 가져온 것입니다.
    # 이 부분은 그냥 넘기는게 나을 것 같습니다.
    @property
    def is_staff(self):
        return self.is_superuser

    class Meta:
        db_table = 'user'