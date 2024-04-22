from django.db import models # type: ignore

# Create your models here.
    
class JobPost(models.Model):
    JOB_TYPE_CHOICES = [
        ('weekday', 'Padrão'),
        ('sunday_holiday', 'Domingo/Feriado'),
        ('night', 'Noturno'),
    ]     
    JOB_TITLE_CHOICES = [
        ('installation', 'Instação'),
        ('support', 'Suporte'),
        ('additional', 'Adicional')
    ]

    title = models.CharField(max_length=100, choices=JOB_TITLE_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES)
    date = models.DateField()
    WO = models.CharField(max_length=20)
   
   
    @property
    def amount(self):
        if self.title == 'installation':
            if self.type == 'night':
                return 60
            elif self.type == 'sunday_holiday':
                return 37 * 2
            else:
                return 37
        elif self.title in ['support', 'additional']:
            if self.type == 'night' or self.type == 'sunday_holiday':
                return 10 * 2
            else:
                return 10
        return 0  # Default to 0 if title or type is not recognized

    def __str__(self):
        return self.title
