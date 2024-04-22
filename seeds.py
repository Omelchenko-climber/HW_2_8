import json

import connect
from models import Tag, Authors, Quotes

files = ["authors.json", "quotes.json"]

with open("authors.json", "r", encoding="utf-8") as f_a:
    data = json.load(f_a)
    for author in data:
        author_class = Authors(fullname=author["fullname"], born_date=author["born_date"], born_location=author[
            "born_location"], description=author["description"])
        author_class.save()

        with open("quotes.json", "r", encoding="utf-8") as f_q:
            quotes = json.load(f_q)

            for record in quotes:
                if record["author"] == author_class.fullname:
                    Quotes(tags=[Tag(name=tag) for tag in record["tags"]], author=author_class, quote=record[
                        "quote"]).save()
