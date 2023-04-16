from django.db import models


# Create your models here.
class ToDo(models.Model):
    title = models.CharField('Topshiriq nomi', max_length=500)
    is_complete = models.BooleanField('Yakunlandi', default=False)
    info = models.TextField()
    bowlaniwi = models.DateTimeField(auto_now_add=True)
    yakunlaniwi = models.DateTimeField()
    # user = models.ForeignKey('user.User', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Topshiriq'
        verbose_name_plural = 'Topshiriq'

    def __str__(self):
        return self.title

