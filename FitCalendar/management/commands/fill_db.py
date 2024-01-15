from django.core.management import BaseCommand

from FitCalendar.models import Exercise, Vitamins, VitaminsInFood, Food


class Command(BaseCommand):
    help = 'Команда для заполнения базы данных'

    def handle(self, *args, **options):
        exercise_template = {
            'descriptions': 'test description',
            'group_muscle': 'test group',
        }

        exercise_list = [Exercise(
            name=f'Упражнение {i}',
            **exercise_template
        ) for i in range(100)]
        Exercise.objects.bulk_create(exercise_list)

        vitamins_list = [Vitamins(
            name=f'Витамины {i}',
            role='test role',
            disadvantage='test disadvantage'
        ) for i in range(100)]
        Vitamins.objects.bulk_create(vitamins_list)

        food_list = [Food(
            name=f'food {i}',
            descriptions='test description',
            fats=i,
            proteins=i,
            carbohydrates=i
        ) for i in range(100)]
        Food.objects.bulk_create(food_list)

        vitamins_in_food_list = [VitaminsInFood(
            vitamins=vitamins_list[i],
            food=food_list[i],
            quantity=i
        ) for i in range(100)]
        VitaminsInFood.objects.bulk_create(vitamins_in_food_list)
