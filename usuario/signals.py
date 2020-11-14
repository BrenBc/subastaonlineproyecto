from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group
from .models import Cliente

#def crearclienteprofile(sender, instance, created, **kwargs):
    #if created:
        #group = Group.objects.get(name='cliente')
        #instance.groups.add(group)

        #Cliente.objects.create(
            #user=instance,
            #name=instance.username,
        #)

#post_save.connect(crearclienteprofile, sender =User)     