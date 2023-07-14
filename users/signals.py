from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from Departments.models import Students

def createuser(sender,instance,created,**kwargs):
    if created:
        group=Group.objects.get(name='student')
        instance.groups.add(group)
        Students.objects.create(
            user=instance,
            )
post_save.connect(createuser,sender=User)

# from django.contrib.auth.models import Group
# from django.contrib.auth.models import User
# from django.db.models.signals import post_save

# def assign_user_to_student_group(sender, instance, created, **kwargs):
#     if created:
#         group = Group.objects.get(name='student')
#         instance.groups.add(group)

# post_save.connect(assign_user_to_student_group, sender=User)
