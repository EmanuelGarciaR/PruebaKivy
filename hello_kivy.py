from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class Saludo(App):

    def build(self):
        #Creamos la caja donde vamos a contener los widgets
        layout = BoxLayout(orientation='vertical')

        #Creamos widget para ingresar nombre
        self.name_user = TextInput()
        self.name_user.text = "Ingresa tu nombre: "
        
        #Boton
        greet = Button()
        greet.text = "Click"
        greet.bind(on_press = self.mostrar_interfaz)
        
        #Label
        self.label_user = Label(text = "Hola")

        #Los añadimos al layout
        layout.add_widget(self.name_user)
        layout.add_widget(greet)
        layout.add_widget(self.label_user)
        #Caja de texto
        return layout
    
    def mostrar_interfaz(self, sender):
        print("El usuario hizo click en el boton")
        self.label_user.text = "Hola " + self.name_user.text
    
    
mi_app = Saludo()
#En lugar de poner build (el método que hicimos) llamamos run que es de la clase kivy
mi_app.run()