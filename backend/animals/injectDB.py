import json
import os
from django.views import View
from .models import Domain, Kingdom, Phylum, Class, Order, Family, Genus, Species, Animal
from django.shortcuts import render
class Inject(View):
    def get(slef, request, *args, **kwargs): 
        Domain.objects.all().delete()
        Kingdom.objects.all().delete()
        Phylum.objects.all().delete()
        Class.objects.all().delete()
        Order.objects.all().delete()
        Family.objects.all().delete()
        Genus.objects.all().delete()
        Species.objects.all().delete()
        Animal.objects.all().delete()
        print('Database Cleared')
        labels = list(os.walk('animals/animals'))[0][1]
        added = 0
        for label in labels:
            folder = os.path.join('animals/animals/' + label + '/')
            file =  open(os.path.join(folder + label + '.json'), encoding='utf-8')
            js = json.load(file)
            domain = Domain.objects.update_or_create(name='Eukarya')
            domain = Domain.objects.get(name='Eukarya')
            if 'Kingdom' in js:
                kingdom =  Kingdom.objects.update_or_create(name=js['Kingdom'], domain=domain)
                kingdom =  Kingdom.objects.get(name=js['Kingdom'], domain=domain)
                del js['Kingdom']
            else:
                kingdom =  Kingdom.objects.update_or_create(name='NA', domain=domain)
                kingdom =  Kingdom.objects.get(name='NA', domain=domain)
            if 'Phylum' in js:
                phylum = Phylum.objects.update_or_create(name=js['Phylum'], kingdom=kingdom, domain=domain)
                phylum = Phylum.objects.get(name=js['Phylum'], kingdom=kingdom, domain=domain)
                del js['Phylum']
            else:
                phylum = Phylum.objects.update_or_create(name='NA', kingdom=kingdom, domain=domain)
                phylum = Phylum.objects.get(name='NA', kingdom=kingdom, domain=domain)
            if 'Class' in js:
                class_ = Class.objects.update_or_create(name=js['Class'], phylum=phylum, kingdom=kingdom, domain=domain)           
                class_ = Class.objects.get(name=js['Class'], phylum=phylum, kingdom=kingdom, domain=domain)
                del js['Class']           
            else:
                class_ = Class.objects.update_or_create(name='NA', phylum=phylum, kingdom=kingdom, domain=domain)           
                class_ = Class.objects.get(name='NA', phylum=phylum, kingdom=kingdom, domain=domain)           
            if 'Order' in js: 
                order = Order.objects.update_or_create(name=js['Order'], _class=class_, phylum=phylum, kingdom=kingdom, domain=domain)
                order = Order.objects.get(name=js['Order'], _class=class_, phylum=phylum, kingdom=kingdom, domain=domain)
                del js['Order']
            else:
                order = Order.objects.update_or_create(name='NA', _class=class_, phylum=phylum, kingdom=kingdom, domain=domain)
                order = Order.objects.get(name='NA', _class=class_, phylum=phylum, kingdom=kingdom, domain=domain)
            if 'Family' in js:
                family = Family.objects.update_or_create(name=js['Family'] ,order=order, _class=class_, phylum=phylum, kingdom=kingdom, domain=domain)
                family = Family.objects.get(name=js['Family'] ,order=order, _class=class_, phylum=phylum, kingdom=kingdom, domain=domain)
                del js['Family'] 
            else:
                family = Family.objects.update_or_create(name='NA' ,order=order, _class=class_, phylum=phylum, kingdom=kingdom, domain=domain)
                family = Family.objects.get(name='NA' ,order=order, _class=class_, phylum=phylum, kingdom=kingdom, domain=domain)
            if 'Genus' in js:
                genus = Genus.objects.update_or_create(name=js['Genus'], family=family ,order=order, _class=class_, phylum=phylum, kingdom=kingdom, domain=domain)
                genus = Genus.objects.get(name=js['Genus'], family=family ,order=order, _class=class_, phylum=phylum, kingdom=kingdom, domain=domain)
                del js['Genus']
            else:                    
                genus = Genus.objects.get_or_create(name='NA', family=family ,order=order, _class=class_, phylum=phylum, kingdom=kingdom, domain=domain)
                genus = Genus.objects.get(name='NA', family=family ,order=order, _class=class_, phylum=phylum, kingdom=kingdom, domain=domain)
            species = Species.objects.get_or_create(name='NA', genus=genus, family=family ,order=order, _class=class_, phylum=phylum, kingdom=kingdom, domain=domain)
            species = Species.objects.get(name='NA', genus=genus, family=family ,order=order, _class=class_, phylum=phylum, kingdom=kingdom, domain=domain)
            name = js['Name']
            del js['Name']
            status = js['Status']
            del js['Status']
            if 'Scientific Name' in js:
                sciName = js['Scientific Name']
                del js['Scientific Name']                
            else:
                sciName ="N/A"
            description = str(js).replace(',' , ',\n')
            folder = os.path.join('animals/' + label + '/')
            label = label.replace(' ', '_').lower()
            lis = []
            for path in os.listdir('./media/' + folder):
                lis.append(path)
            if len(lis) > 1:
                img = str(os.path.join(folder + label + '0' +'.jpg'))
            else:
                img = str(os.path.join('animals/' + 'animal.jpg'))                   
            user = request.user
            animal = Animal.objects.update_or_create(name=name, user=user ,status=status, image=img, description=description, scientaficName=sciName ,species=species, genus=genus, family=family ,order=order, _class=class_, phylum=phylum, kingdom=kingdom, domain=domain)
            print(name + ' has been added Successfully!')           
            added += 1
            print('Total= ', added)                
        
        return render(request, 'inj.html')


