from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import StringField, ReferenceField, ListField, EmbeddedDocumentField


class Tag(EmbeddedDocument):
    name = StringField()


class Authors(Document):
    fullname = StringField()
    born_date = StringField()
    born_location = StringField()
    description = StringField()


class Quotes(Document):
    tags = ListField(EmbeddedDocumentField(Tag))
    author = ReferenceField(Authors)
    quote = StringField()
