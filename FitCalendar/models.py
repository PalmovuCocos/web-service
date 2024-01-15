from django.db import models
from django.contrib.auth.models import User


class Exercise (models.Model):
    name = models.CharField(max_length=30, verbose_name='Название: ')
    descriptions = models.TextField(max_length=280, verbose_name='Описание: ')
    group_muscle = models.CharField(max_length=30, verbose_name='Группа мышц: ')
    photo = models.ImageField(upload_to="photos/exercise", verbose_name='Фото: ')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Упражнения'


class Vitamins(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название: ')
    role = models.TextField(max_length=280, verbose_name='Роль: ')
    disadvantage = models.TextField(max_length=280, verbose_name='Недостаток: ')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural='Витамины'


class Food(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название: ')
    vitamins = models.ForeignKey(Vitamins, on_delete=models.PROTECT)
    descriptions = models.TextField(verbose_name='Описание: ')
    fats = models.IntegerField(verbose_name='Жиры: ')
    proteins = models.IntegerField(verbose_name='Белки: ')
    carbohydrates = models.IntegerField(verbose_name='Углеводы: ')
    photo = models.ImageField(upload_to="photos/food", verbose_name='Фото: ')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Еда'


class Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    weight = models.IntegerField(blank=True)
    height = models.IntegerField(blank=True)
    type_body = models.CharField(max_length=30, blank=True)
    target = models.CharField(blank=True, max_length=30)
    fats = models.IntegerField(blank=True)
    proteins = models.IntegerField(blank=True)
    carbohydrates = models.IntegerField(blank=True)
    sex = models.CharField(max_length=1, blank=True)

    def __str__(self):
        return self.login

    class Meta:
        verbose_name_plural='Пользователи'


class Day(models.Model):
    id_user = models.ForeignKey(Users, on_delete=models.CASCADE)
    date = models.DateField(verbose_name='Дата: ')
    day_of_week = models.CharField(max_length=30, verbose_name='День недели: ')

    def __str__(self):
        return self.date

    class Meta:
        verbose_name_plural = 'Дни'


class BasketFood(models.Model, ):
    id_day = models.ForeignKey(Day, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='id_food_vit_fv')
    id_user = models.ForeignKey(Day, on_delete=models.CASCADE, related_name='id_user_day')
    food_weight = models.IntegerField(verbose_name='Вес еды: ')

    class Meta:
        verbose_name_plural='Корзина еды'


class BasketExercise(models.Model):
    id_exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    id_day = models.ForeignKey(Day, on_delete=models.CASCADE, related_name='id_day_in_be')
    id_user = models.ForeignKey(Day, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Корзина упражнений'




