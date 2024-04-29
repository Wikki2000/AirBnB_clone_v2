#!/usr/bin/python3

from models import storage

val = storage.all()
for key, obj in val.copy().items():
    print(f"An object: {obj} with key: {key} is about to be deleted")
    storage.delete(obj)
