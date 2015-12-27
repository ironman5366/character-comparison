import easygui
import os
from tinydb import TinyDB, where, Query
import sys
db = TinyDB('db.json')
class main():
	def addcharacter(self):
		namestr=easygui.enterbox("What is the characters name?")
		if namestr==None:
			self.__init__()
		else:
			Character = Query()
			if db.search(Character.namestr.exists()):
				easygui.msgbox("This name already belongs to another character, please choose another name or remove the character with the same name")
				self.addcharacter()
			else:
				easygui.msgbox("In this screen you can add traits. You can come back here as many times as you wish until you click Done.")
				def addtraits():
					powers=[]
					weaknesses=[]
					bio=''
					traitchoices=[
					"Add powers",
					"Add weaknesses",
					"Add bio",
					"Done"
					]
					tc=traitchoices
					trait=easygui.choicebox(msg="Please select a trait",title="Character Database",choices=traitchoices)
					if trait==tc[0]:
						powersraw=easygui.enterbox("Please enter as many powers as you like, seperated with commas.")
						if powersraw==None:
							addtraits()
						else:
							for power in powersraw.split(','):
								powers.append(power)
							addtraits()
					elif trait==tc[1]:
						weaknessesraw=easygui.enterbox("Please enter as many powers as you like, seperated with commas.")
						if weaknessesraw==None:
							addtraits()
						else:
							for weakness in weaknessesraw.split(','):
								weaknesses.append(weakness)
							addtraits()
					elif trait==tc[2]:
						biomsg=easygui.enterbox("Please enter a bio for the character")
						if biomsg==None:
							addtraits()
						else:
							bio=biomsg
							addtraits()
					elif trait==tc[3]:
						db.insert({'name': namestr, 'powers': powers, 'weaknesses':weaknesses, 'bio': bio})
						easygui.msgbox("Done")
						self.__init__()
					else:
						self.__init__()
				addtraits()
	def __init__(self):
		initchoices=[
		"Add character",
		"Compare characters",
		"Remove characters"
		]
		initchoice=easygui.choicebox(msg="Please make a selection",title="Character Database",choices=initchoices)
		ic=initchoice
		ics=initchoices
		if ic==ics[0]:
			self.addcharacter()
		elif ic==ics[1]:
			pass
		elif ic==ics[2]:
			pass
		elif ic==None:
			sys.exit()
		else:
			easygui.msgbox("Unrecognized choices {0}".format(str(ic)))
			sys.exit()
if __name__=="__main__":
	easygui.msgbox("Merry christmas Oliver!")
	main()