#
# The syllables generated from this are not really valid, but the number of
# syllables generated generally is.
#
# TODO:
#  - syllabic 'm' and 'n'
#  - Rules for silent 'i' and 'o'? (eg. business [biz.nis], colonel [kern.el])
#  - Silent 'e' in compound words (eg. whitecap [wait.cap])
#  - favor onset (unless invalid onset/coda generated)
#  - account for sonority sequencing principle and other phonotactic rules
#  - render syllables phonologically
#
def syllabize_en(word):

	# Check if a letter in a word is a phonemic vowel
	def isvowel(word, i):
		# 'y' is consonant at beginning of word or after vowel, otherwise vowel sound
		if word[i] in 'aeiou' or (i > 0 and word[i] == 'y'and (i == 0 or not isvowel(word, i - 1))):
			return True
		return False

	# Special cases
	specials = {
		'': [],
		'colonel': [ 'col', 'nel' ],
		'business': [ 'bus', 'ness' ]
	}
	if word in specials:
		return specials[word]

	# Handle final 'e'
	if word[-1] == 'e' and len(word) > 2:
		if word[-2] == 'l': # e following 'l' demarcates the 'l' as a syllabic consonant, leave 
			pass
		else:
			# Remove final e when it is silent
			word = word[:-1]

	if len(word) > 2:
		# Convert final 'ed' to 'd', 'es' to 's', as they are syllabized as such
		if word[-2:] == 'ed': word = word[:-2] + 'd'
		if word[-2:] == 'es': word = word[:-2] + 's'

	syls = []
	i = 0
	while i < len(word):
		onset = nucleus = coda = ''

		while i < len(word) and not isvowel(word, i): onset   += word[i]; i+=1
		while i < len(word) and     isvowel(word, i): nucleus += word[i]; i+=1
		while i < len(word) and not isvowel(word, i): coda    += word[i]; i+=1

		syl = onset + nucleus + coda
		if syl != '':
			syls += [syl]

	return syls

lang = {
	'en': syllabize_en
}
