import os
from tinydb import TinyDB, where, Query
import sys
import webview
import easygui
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
				easygui.msgbox("You will now enter the characters qualities")
				def getquality(quality):
					qualval=easygui.enterbox("On a scale from 1-10, what is the characters {0}?".format(quality))
					if qualval==None:
						self.__init__()
					else:
						try:
							qualval=int(qualval)
							if qualval > -1:
								if qualval < 11:
									return qualval
								else:
									easygui.msgbox("Must be 10 or less")
							else:
								easygui.msgbox("Must be 0 or greater")
								getquality(quality)
						except TypeError:
							easygui.msgbox("Must be a valid integer")
				strength=getquality('strength')
				intelligence=getquality('intellignece')
				stamina=getquality('stamina')
				speed=getquality('speed')
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
							bio+=biomsg
							addtraits()
					elif trait==tc[3]:
						print powers
						print weaknesses
						print bio
						db.insert({'name': namestr, 'powers': powers, 'weaknesses':weaknesses, 'bio': bio, 'speed':speed, 'stength':strength,'intelligence':intelligence,'stamina':stamina})
						easygui.msgbox("Done")
						self.__init__()
					else:
						self.__init__()
				addtraits()
	def compare(self):
		names=[]
		entries=db.all()
		for item in db[0]:
			names.append(item['name'])
		selected=[]
		def getname():
			namechoice=easygui.choicebox(msg="Please select a character", title="Character Database",choices=names)
			if namechoice==None:
				self.__init__()
			else:
				selected.append(namechoice)
		getname()
		getname()
		if easygui.ynbox("Would you like to compare {0} and {1}?".format(selected[0],selected[1])):
			rules=open('rules.conf').read()
			powerrules=open('powers.conf').read()
		else:
			self.compare()
	def addstuff(self):
		easygui.msgbox("Here you can add rules for powers and weaknesses.")
		options=["Add qualites of powers", "Add rules for powers and weaknesses"]
		option=easygui.choicebox(msg="Please make a selection",title="Character Database",choice=options)
		if option==options[0]:
			powername=easygui.enterbox(msg="Please enter the name of a power you would like to assign traits to.")
			if powername==None:
				self.addstuff()
			else:
				def getquality(quality):
					qualval=easygui.enterbox("On a scale from 1-10, what level of {0} is this power worth? If the power does not affect it, enter 0.".format(quality))
					if qualval==None:
						self.__init__()
					else:
						try:
							qualval=int(qualval)
							if qualval > -1:
								if qualval < 11:
									return qualval
								else:
									easygui.msgbox("Must be 10 or less")
							else:
								easygui.msgbox("Must be 0 or greater")
								getquality(quality)
						except TypeError:
							easygui.msgbox("Must be a valid integer")
				strength=str(getquality('strength'))
				intelligence=str(getquality('intellignece'))
				stamina=str(getquality('stamina'))
				speed=str(getquality('speed'))
				pf=open("powers.conf",'a')
				pf.write('{0}=[{"speed":{1},"strength":{2},"intelligence":{3},"stamina":{4}\n'.format(powername,speed,strength,intelligence,stamina))
				pf.close()
		elif option==options[1]:
			easygui.msgbox("Now you can define which powers trump which weaknesses")
		elif option==None:
			self.__init__()
		else:
			easygui.msgbox("Unrecognized choice {0}. Exiting.".format(option))
			sys.exit()
	def remove(self):
		pass
	def __init__(self):
		initchoices=[
		"Add character",
		"Compare characters",
		"Remove characters",
		"Add powers and weaknesses"
		]
		initchoice=easygui.choicebox(msg="Please make a selection",title="Character Database",choices=initchoices)
		ic=initchoice
		ics=initchoices
		if ic==ics[0]:
			self.addcharacter()
		elif ic==ics[1]:
			self.compare()
		elif ic==ics[2]:
			self.addstuff()
		elif ic==None:
			sys.exit()
		else:
			easygui.msgbox("Unrecognized choices {0}".format(str(ic)))
			sys.exit()
if __name__=="__main__":
	easygui.msgbox("Merry christmas Oliver!")
	main()