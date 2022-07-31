from api.models import Country, City, State

def run():
    Country.objects.all().delete()
    City.objects.all().delete()
    State.objects.all().delete()
    print("Deleted all models.")
    print("Done.")