from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class TraductorRoot(BoxLayout):
	pass

class Proyecto(BoxLayout):
	palabra = ObjectProperty()
	traduccion = ObjectProperty()

	def traductor(self):
		dicc = {"gato":"cat","lobo":"wolf","perro":"dog","zorro":"fox","pájaro":"bird","gallina":"hen","pato":"duck","rata":"rat","cordero":"lamb","serpiente":"snake","vaca":"cow","mariposa":"butterfly","caballo":"horse","mosquito":"mosquito","elefante":"elephant","ballena":"whale","araña":"spider","gallo":"cock","abeja":"bee","águila":"eagle","pollito":"chick","mono":"monkey","caracol":"snail","camello":"camel","pez":"fish","conejo":"rabbit","toro":"bull","chancho":"pig","jirafa":"giraffe","hormiga":"ant","tigre":"tiger","león":"lion","pantera":"panther","hornero":"baker","burro":"donkey","luciérnaga":"firefly","ganso":"goose","ardilla":"squirrel","canguro":"kangaroo","hipopótamo":"hippopotamus","insecto":"insect","rinoceronte":"rhinoceros","pulpo":"octopus","cebra":"zebra","langosta":"crab","cocodrilo":"crocodile","oso":"bear","cabra":"goat","pingüino":"penguin","coala":"koala","pavo":"turkey","sapo":"toad","pavo real":"peacock","rana":"frog","paloma":"pigeon or dove","cisne":"swan" }
		for k,v in dicc.items():
			if k == self.palabra.text:
				self.traduccion.text = dicc[self.palabra.text]
			if v == self.palabra.text:
				self.traduccion.text = k

class TraductorApp(App):
	pass
		

if __name__ == '__main__':
	TraductorApp().run()
