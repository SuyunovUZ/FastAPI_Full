from tortoise import models, fields


class Author(models.Model):
    id = fields.IntField(pk=True, generated=True)
    first_name = fields.CharField(max_length=212)
    last_name = fields.CharField(max_length=212)

    def __str__(self):
        return self.first_name


class Post(models.Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=212)
    body = fields.TextField()
    # author = fields.ForeignKeyField('Author', on_delete=fields.CASCADE)
    author = fields.ForeignKeyField('models.Author', related_name='posts')
    image = fields.CharField(max_length=212)

    def __str__(self):
        return self.title
