from django.db import models

class Publisher(models.Model):
    publisherName = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.publisherName


class Comic(models.Model):
    comicName = models.CharField(max_length=100, unique=True)
    writer = models.CharField(max_length=100, default='null')
    issuesNumber = models.IntegerField(default=0)
    beginDate = models.DateField(default='00-00-0000')
    endDate = models.DateField(default='00-00-0000')
    comicPublisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    def __str__(self):
        return self.comicName
