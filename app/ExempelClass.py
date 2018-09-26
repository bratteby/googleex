from .recommendations import Recommender

class ExempelClass():
	"""docstring for ClassName"""
	def __init__(self):
		self.r = None

	def printhi(self):
		return "Hello this is Adrian's program"
		
	def printho(self):
		self.r = Recommender("testmodel.h5")
		self.r.load_model()
		return r.get_recommendations("13591")
		