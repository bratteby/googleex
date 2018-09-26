import pandas as pd
import os.path


#LOOKUP_PATH = model_path = os.path.join("..","data","misc","lookup.h5")

class Recommender():
	"""Provide recommendations from a pre-trained apriori alogirthm model"""
	def __init__(self,model_path):
		self.rules = None
		self.lookup_table = None
		self.load_model(model_path)

	def load_model(self, model_path):
		'''Loads recommendation rules from hdf5-file format and sets internal variable

		Args:
			- model_path: os.path object of joined pathway to the model

		Returns:
			- nothing
		'''
		
		#Read model from file
		rules = pd.read_hdf(model_path, 'df')
		#rules = pd.read_pickle(model_path)
		self.rules = rules

		#Could also return rules here if we don't want to encapsulate in a class

	def get_recommendations(self, sku, n_recommendations=3):
		'''Given a list of sku: (product id) return list of n_recommendations items to recommend

		Args:
			- sku: list of string SKUs to make a recommendation from 
			- n_recommendations: int describing nr of rules to make recommendations from 
				(could  be changed to nr of returned recommendations)

		Returns:
			- List of unique string SKUs to recommend
		'''

		#Filter rules based on antecedents that contains SKUs
		#sort on highest confidence and pick top n
		results = self.rules[self.rules['antecedents'] == 
			frozenset(sku)].sort_values("confidence").iloc[:n_recommendations]


		recommendations = []
		for _,row in results.iterrows():
		    recommendations.extend(list(row['consequents']))

		return self.unique(recommendations)

	def unique(self,seq):
		#Inputs sequence and returns a order preserved set
		seen = set()
		seen_add = seen.add
		return [x for x in seq if not (x in seen or seen_add(x))]


def main():
	model_path = os.path.join("testmodel.h5")
	r = Recommendations(model_path)	

	sku = ["13591"]
	recommendations = r.get_recommendations(sku)

	print(recommendations)

if __name__ == '__main__':
	main()



