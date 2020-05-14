from django.core.management.base import BaseCommand, CommandError
import json
from uactivity.models import User,Activity
from django.db import IntegrityError

class Command(BaseCommand):
    help = 'vishant'

    def handle(self, *args, **options):

         f = open('dummy.json',)
         data = json.load(f)

         for i in data['members']:
             id=i['id']
             real_name=i['real_name']
             tz=i['tz']
             start_time=i['activity_periods'][0]['start_time']
             end_time=i['activity_periods'][0]['end_time']

         f.close()

         if User.objects.filter(id=id).count()==0:
             u=User.objects.create(id=id,real_name=real_name,tz=tz)
             Activity.objects.create(user=u,start_time=start_time,end_time=end_time)
             print("New User Created with activities")

         else:
             print(User.objects.get(id=id))
             u=User.objects.get(id=id)
             try:
                 Activity.objects.create(user=u,start_time=start_time,end_time=end_time)
                 print("New start_time and end_time time added for existing user ",u.id)
             except IntegrityError as e:
                 print("Please enter again,Make Sure real_name, start_time, end_time are unique together, there combination shouldn't be same as of old data ")
