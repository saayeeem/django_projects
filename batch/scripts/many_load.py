import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import Site, Category,State,Region,Iso


def run():
    fhand = open('unesco/whc-sites-2018-clean.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    Site.objects.all().delete()
    Category.objects.all().delete()
    State.objects.all().delete()
    Region.objects.all().delete()
    Iso.objects.all().delete()


    # Format
    # email,role,course
    # jane@tsugi.org,I,Python
    # ed@tsugi.org,L,Python

    for row in reader:
        print(row)

        c, created = Category.objects.get_or_create(name=row[7])
        s, created = State.objects.get_or_create(name=row[8])
        r, created = Region.objects.get_or_create(name=row[9])
        i, created = Iso.objects.get_or_create(name=row[10])

        try:
            y=int(row[3])
        except:
            y=None

        try:
            lo=float(row[4])
        except:
            lo=None

        try:
            la=float(row[5])
        except:
            la=None
        try:
            ah=float(row[6])
        except:
            ah=None


        site = Site(name=row[0], description=row[1], justification=row[2],  year=y, longitude=lo, latitude=la, area_hectares= ah, category=c, state=s, region=r, iso=i)
        site.save()