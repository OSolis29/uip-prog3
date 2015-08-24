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
		dicc = {'perro': 'dog', 'carro': 'car', 'agua': 'water'}
		for k,v in dicc.items():
			if k == self.palabra.text:
				self.traduccion.text = dicc[self.palabra.text]
			if v == self.palabra.text:
				self.traduccion.text = k

class TraductorApp(App):
	pass
		

if __name__ == '__main__':
	TraductorApp().run()