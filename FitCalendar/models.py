from django.db import models

class exercise (models.Model):
    name=models.CharField(max_length=30)
    descriptions=models.TextField(max_length=280)
    group_muscle =models.CharField(max_length=30)
    photo=models.ImageField(upload_to="photos/exercise")
    def __str__(self):
        return self.name
class vitamins(models.Model):
    name=models.CharField(max_length=30)
    role=models.TextField(max_length=280)
    disadvantage=models.TextField(max_length=280)
    def __str__(self):
        return self.name
class food(models.Model):
    name=models.CharField(max_length=30)
    descriptions=models.TextField()
    fats=models.IntegerField()
    proteins=models.IntegerField()
    carbohydrates=models.IntegerField()
    photo=models.ImageField(upload_to="photos/food")
    def __str__(self):
        return self.name
class users(models.Model):
    login=models.CharField(max_length=80)
    email=models.EmailField(max_length=80)
    password=models.CharField(max_length=30)
    weight=models.IntegerField()
    height=models.IntegerField()
    type_body=models.CharField(max_length=30)
    target=models.CharField(blank=True,max_length=30)
    fats=models.IntegerField(blank=True)
    proteins=models.IntegerField(blank=True)
    carbohydrates=models.IntegerField(blank=True)
    sex=models.CharField(max_length=1)
    def __str__(self):
        return self.login
class day(models.Model):
    id_user=models.ForeignKey(users,on_delete=models.CASCADE)
    date=models.DateField()
    day_of_week=models.CharField(max_length=30)
    def __str__(self):
        return self.date
class food_vit(models.Model):
    id_food=models.ForeignKey(food,on_delete=models.CASCADE)
    id_vitamins=models.ForeignKey(vitamins,on_delete=models.CASCADE)

class basket_food(models.Model,):
    id_day=models.ForeignKey(day,on_delete=models.CASCADE)
    id_food_vit=models.ForeignKey(food_vit,on_delete=models.CASCADE,related_name='id_food_vit_fv')
    id_food=models.ForeignKey(food_vit,on_delete=models.CASCADE, related_name='id_food_fv')
    id_vitamins=models.ForeignKey(food_vit,on_delete=models.CASCADE,related_name='id_vitamins_fv')
    id_user=models.ForeignKey(day,on_delete=models.CASCADE,related_name='id_user_day')

    food_weight=models.IntegerField()


class basket_exercise(models.Model):
    id_exercise=models.ForeignKey(exercise,on_delete=models.CASCADE)
    id_day=models.ForeignKey(day,on_delete=models.CASCADE,related_name='id_day_in_be')
    id_user=models.ForeignKey(day,on_delete=models.CASCADE)




