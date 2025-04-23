from django.db import models


class marital_status(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 20, blank = False, null = False)

    def __str__(self):
        return self.name



class cities(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 200)
    uf = models.CharField(max_length = 2)

    def __str__(self):
        return self.name


class status(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name



# Create your models here.
class beneficiary(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 200)
    cpf = models.CharField(max_length = 20)
    id_doc = models.CharField(max_length = 13)
    issuing_authority = models.CharField(max_length = 20)
    issuing_date = models.DateField()
    marital_status = models.ForeignKey(marital_status, on_delete = models.PROTECT, related_name = 'marital_status')
    profession = models.CharField(max_length = 50, blank = True, null = True)
    cep_address = models.CharField(max_length = 9)
    street = models.CharField(max_length = 200)
    address = models.CharField(max_length = 200)
    number_address = models.CharField(max_length = 10)
    city = models.ForeignKey(cities, on_delete = models.PROTECT, related_name = 'cities_name')
    main_phone = models.CharField(max_length = 13)
    other_phone = models.CharField(max_length = 13, blank = True, null = True)
    email = models.CharField(max_length = 100)
    status_person = models.ForeignKey(status, on_delete = models.PROTECT, related_name = 'status_person')
    date_of_birth = models.DateField()
    reg_date = models.DateField(null=True, blank=True)
    del_date = models.DateField(null=True, blank=True)
    mod_date = models.DateField(null=True, blank=True)
    registration_user = models.CharField(max_length = 200,null=True,blank=True)

    def __str__(self):
        return self.name








