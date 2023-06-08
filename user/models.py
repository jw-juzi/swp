from django.db import models


# Create your models here.
class User(models.Model):
    GENERS = (
        ('male', '男性'),
        ('female', '女性')
    )
    LOCATIONS = (
        ('北京', '北京'),
        ('上海', '上海'),
        ('成都', '成都'),
        ('武汉', '武汉'),
    )
    phonenum = models.CharField(max_length=16, unique=True, verbose_name='手机号')
    nickname = models.CharField(max_length=20, db_index=True, verbose_name='昵称')
    gender = models.CharField(max_length=10, choices=GENERS, default='male', verbose_name='性别')
    birthday = models.DateField(default='2000-1-1', verbose_name='出生日')
    avatar = models.CharField(max_length=256, verbose_name='个人形象')
    location = models.CharField(max_length=10, choices=LOCATIONS, default='上海', verbose_name='常居地')
