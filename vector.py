import itertools
import requests
import mmh3
from lxml import html
import copy

class Vector:

	def hash01(self,tegol):
		somma = 0
		for t in tegol:
			somma = somma + mmh3.hash(t,111111)
		return int(str(abs(somma))[3:5])

	def hash02(self,tegol):
		somma = 0
		for t in tegol:
			somma = somma + mmh3.hash(t,222222)
		return int(str(abs(somma))[3:5])

	def hash03(self,tegol):
		somma = 0
		for t in tegol:
			somma = somma + mmh3.hash(t,333333)
		return int(str(abs(somma))[3:5])

	def hash04(self,tegol):
		somma = 0
		for t in tegol:
			somma = somma + mmh3.hash(t,444444)
		return int(str(abs(somma))[3:5])

	def hash05(self,tegol):
		somma = 0
		for t in tegol:
			somma = somma + mmh3.hash(t,555555)
		return int(str(abs(somma))[3:5])

	def hash06(self,tegol):
		somma = 0
		for t in tegol:
			somma = somma + mmh3.hash(t,666666)
		return int(str(abs(somma))[3:5])

	def hash07(self,tegol):
		somma = 0
		for t in tegol:
			somma = somma + mmh3.hash(t,777777)
		return int(str(abs(somma))[3:5])

	def hash08(self,tegol):
		somma = 0
		for t in tegol:
			somma = somma + mmh3.hash(t,888888)
		return int(str(abs(somma))[3:5])

	def hash09(self,tegol):
		somma = 0
		for t in tegol:
			somma = somma + mmh3.hash(t,999999)
		return int(str(abs(somma))[3:5])

	def hash10(self,tegol):
		somma = 0
		for t in tegol:
			somma = somma + mmh3.hash(t,101010)
		return int(str(abs(somma))[3:5])

	def vettore(self,elle,indirizzo):
		file = open(indirizzo, "r")
		page = file.read()
		file.close()
		dom_tree = html.fromstring(page)
		all_leaves = dom_tree.xpath("//*")
		S = []
		tegola = []
		i = 0
		diz = {}
		min1 = 999
		min2 = 999
		min3 = 999
		min4 = 999
		min5 = 999
		min6 = 999
		min7 = 999
		min8 = 999
		min9 = 999
		min10 = 999
		for leaf in all_leaves:
			tegola.append(leaf.tag)
			if (i == elle):
				S.append(copy.copy(tegola))
				if self.hash01(tegola) < min1:
					min1 = self.hash01(tegola)
				if self.hash02(tegola) < min2:
					min2 = self.hash02(tegola)
				if self.hash03(tegola) < min3:
					min3 = self.hash03(tegola)
				if self.hash04(tegola) < min4:
					min4 = self.hash04(tegola)
				if self.hash05(tegola) < min5:
					min5 = self.hash05(tegola)
				if self.hash06(tegola) < min6:
					min6 = self.hash06(tegola)
				if self.hash07(tegola) < min7:
					min7 = self.hash07(tegola)
				if self.hash08(tegola) < min8:
					min8 = self.hash08(tegola)
				if self.hash09(tegola) < min9:
					min9 = self.hash09(tegola)
				if self.hash10(tegola) < min10:
					min10 = self.hash10(tegola)
				i = 0
				tegola = []
			i = i+1
		if i > 1:
			S.append(copy.copy(tegola))
			if self.hash01(tegola) < min1:
				min1 = self.hash01(tegola)
			if self.hash02(tegola) < min2:
				min2 = self.hash02(tegola)
			if self.hash03(tegola) < min3:
				min3 = self.hash03(tegola)
			if self.hash04(tegola) < min4:
				min4 = self.hash04(tegola)
			if self.hash05(tegola) < min5:
				min5 = self.hash05(tegola)
			if self.hash06(tegola) < min6:
				min6 = self.hash06(tegola)
			if self.hash07(tegola) < min7:
				min7 = self.hash07(tegola)
			if self.hash08(tegola) < min8:
				min8 = self.hash08(tegola)
			if self.hash09(tegola) < min9:
				min9 = self.hash09(tegola)
			if self.hash10(tegola) < min10:
				min10 = self.hash10(tegola)
		V = [min1,min2,min3,min4,min5,min6,min7,min8]#,min9,min10]
		return V