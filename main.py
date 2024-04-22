import redis

import connect
from models import Authors, Quotes

r_client = redis.StrictRedis(host='localhost', port=6379, db="cache")

def main():
    while True:
        command, *details = input(">>>: ").split(":")
        if command == "exit":
            break

        list_quotes = []

        match command:
            case "name":
                name, = details
                author_id, = [auth.id for auth in Authors.objects() if auth.fullname == name]
                list_quotes = [q.quote for q in Quotes.objects() if q.author.id == author_id]
            case "tag":
                tag, = details
                list_quotes = []
                for q in Quotes.objects():
                    if tag in [tag.name for tag in q.tags]:
                        list_quotes.append(q.quote)
            case "tags":
                tags = set(details[0].split(","))
                list_quotes = [q.quote for q in Quotes.objects() if tags.intersection(set(tag.name for tag in q.tags))]

        print(list_quotes)


if __name__ == '__main__':
    main()
