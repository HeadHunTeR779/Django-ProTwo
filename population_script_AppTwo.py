import os
#path to settings.py in kingpin
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')

import django
django.setup()

#####################ABOVE STUFF IS REPETITIVE LOL <3 :* ############################

from faker import Faker
from AppTwo.models import User

fakegen = Faker()   #Object of Class Faker() gotta love OOP

def populater(N=10):
    for _ in range(N):
        full_name = fakegen.name()
        fake_first, fake_last = full_name.split(" ")
        fake_email = fakegen.email()
        substrate = User.objects.get_or_create(first_name=fake_first,
                                                    last_name=fake_last,
                                                    email=fake_email)[0]
        substrate.save()



if __name__ == '__main__':
    print("Populating User")
    populater(30)
    print("Finished Populating")
