from django.db import models


class Book(models.Model):
    book_name = models.CharField(max_length=200)
    pub_date = models.DateField('date published')
    page_num = models.IntegerField()
    first_print = models.BooleanField()

    def __str__(self):
        return f"name: {self.book_name} \ndate published: {self.pub_date} \nnumber of pages: {self.page_num} \nfirst " \
            f"print: {self.first_print} "
