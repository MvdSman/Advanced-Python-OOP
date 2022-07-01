import pandas as pd


class DictionaryFunc:
	"""
	Object that contains a dictionary of words.

	Can also return definition(s) using `get_definition(term)`.
	"""
	def __init__(self, definitions='data.csv'):
		try:
			self.definitions = pd.read_csv(definitions)
		except:
			print('Error loading the definition list!')

	def get_definition(self, term):
		"""
		Gets the definition(s) of `term`.

		:param term: term to find the definition(s) for.
		:return: tuple of all definitions found for term.
		"""
		return tuple(self.definitions.loc[self.definitions['word'] == term]['definition'])


if __name__ == "__main__":
	dictionary = DictionaryFunc('data.csv')
	print(dictionary.get_definition('acid'))
