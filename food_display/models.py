from django.db import models

# model called Food to store the food details.

class Food_Category(models.Model):
    category = models.CharField(max_length =100)
    about = models.CharField(max_length = 400)
    
    def __str__(self):
            return self.category

class Food(models.Model):
    name = models.CharField(max_length=50)
    description =models.TextField(max_length=1000)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image =models.ImageField(upload_to ='media/',default="media/default.jpeg")
    choice = (("Veg", "Veg"),
                 ("Non-Veg", "Non-veg"),
                 ("Vegan", "Vegan"),
                 )
    food_type = models.CharField(choices=choice,max_length = 20)
    category = models.ForeignKey(Food_Category, on_delete=models.CASCADE,related_name='food_category',null=True)

    def __str__ (self):
        return self.name


