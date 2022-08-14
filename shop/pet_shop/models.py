from django.db import models


class Products(models.Model):
    FOOD = 'Корм'
    TREAT = 'Лакомство'
    HOME = 'Домик'
    BED = 'Лежанка'
    TRANSPORT = 'Переноска'
    CARE = 'Средства по уходу'
    TOILET = 'Лоток'
    FILLER = 'Наполнитель'
    ELSE = 'Другое'

    CHOICE_GROUP = {
        (FOOD, 'Корм'),
        (TREAT, 'Лакомство'),
        (HOME, 'Домик'),
        (BED, 'Лежанка'),
        (TRANSPORT, 'Переноска'),
        (CARE, 'Средства по уходу'),
        (TOILET, 'Лоток'),
        (FILLER, 'Наполнитель'),
        (ELSE, 'Другое'),
    }
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    is_available = models.BooleanField(default=True)
    group = models.CharField(max_length=50, choices=CHOICE_GROUP, default=FOOD)
    image = models.ImageField(default="no_imgage.png", upload_to='product_images')

    def __str__(self):
        return self.name
