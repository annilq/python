from collections import OrderedDict

def showFavorite():
	favorite_language=OrderedDict()
	favorite_language["leter"]="java"
	favorite_language["moon"]="android"
	favorite_language["annilq"]="frontEnd"
	for name,language in favorite_language.items():
		print(name,"favorite_language is",language)
showFavorite()

		