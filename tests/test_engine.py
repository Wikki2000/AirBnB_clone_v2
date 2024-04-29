from models import storage
from models.base_model import BaseModel
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.place import Place
from models.city import City
from models.user import User
import unittest
from models.engine.file_storage import FileStorage

obj_storage = storage.all()
class TestFileStorage(unittest.TestCase):
    '''this will test the FileStorage'''

    @classmethod
    def setUpClass(self):
        """ Set up for test """
        self.user = User()
        self.user.first_name = "wisdom"
        self.user.last_name ="Okposin"
        self.user.email = "wisdomokposin@gmail.com"
        self.storage = FileStorage()

