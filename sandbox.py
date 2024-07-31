from models.state import State
from models import storage

states = storage.all(State)

print(states)
