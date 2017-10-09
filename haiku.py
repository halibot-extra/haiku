from .syllabizer import lang
from halibot import HalModule

class Haiku(HalModule):

	topics = {
		'haiku': 'Watches for when someone bequeths a haiku, unbeknowst to themself.'
	}

	def init(self):
		pass

	# Checks if a poem matches the given syllabic meter
	# Returns the poem if yes, None otherwise
	def syllabic_poem(self, words, syls, expect):
		poem = ''
		count = 0
		line = 0
		for i in range(0, len(words)):
			# Too many lines?
			if line >= len(expect):
				return None

			count += syls[i]
			poem += words[i]

			if count == expect[line]:
				# Got a line as expected!
				line += 1
				poem += '\n'
				count = 0
			elif count > expect[line]:
				# Too many syllables in a line :(
				return None
			else:
				poem += ' '

		return poem if count == 0 and line == len(expect) else None

	def haiku(self, words, syls):
		return self.syllabic_poem(words, syls, [5, 7, 5])

	def receive(self, msg):
		# Get the words of the message and the syllables for those words
		words = [x for x in ''.join(filter(lambda x: x.isalpha() or x == ' ', msg.body)).split(' ') if x != '']

		syls = []
		for w in words:
			syls += [len(lang[self.config.get('lang', 'en')](w.lower()))]

		# Have a haiku?
		haiku = self.haiku(words, syls)
		if haiku != None:
			self.reply(msg, body='I proffer that your prose is a poem, a haiku:\n' + haiku)

