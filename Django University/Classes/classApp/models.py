from django.db import models

class djangoClasses(models.Model):
    title = models.CharField(max_length=60, default="", blank=True, null=False)
    course_number = models.IntegerField(max_length=60, default="", blank=True)
    instructor_name = models.CharField(max_length=60, default="", blank=True, null=False)
    duration = models.FloatField(null=True, blank=True, default=0.0)

obj1 = djangoClasses(title="School",course_number=203,instructor_name="Darren",duration=1.90)
obj1.save()
obj2 = djangoClasses(title="College", course_number=333, instructor_name="Tiny", duration=2.03)
obj2.save()
obj3 = djangoClasses(title="Yard", course_number=456, instructor_name="Lovell", duration=1.20)
obj3.save()