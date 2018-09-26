from .recommendations import Recommender
import os.path
import sys

class ExempelClass():
	"""docstring for ClassName"""
	def __init__(self):
		self.r = None

	def printhi(self):
		return "Hello this is Adrian's program"
		
	def printho(self):
		MODEL_PATH = os.path.join(sys.path[0],"app","testmodel.h5")

		self.r = Recommender(MODEL_PATH)
		return self.r.get_recommendations(["13591"])
		