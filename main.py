from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

class AntiEstafaApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        self.input_text = TextInput(hint_text="Pegá mensaje sospechoso")
        layout.add_widget(self.input_text)

        btn = Button(text="Analizar")
        btn.bind(on_press=self.analizar)
        layout.add_widget(btn)

        self.resultado = Label(text="Resultado aparecerá aquí")
        layout.add_widget(self.resultado)

        return layout

    def analizar(self, instance):
        texto = self.input_text.text.lower()

        if "gana dinero" in texto or "urgente" in texto or "link" in texto:
            self.resultado.text = "⚠️ Posible estafa detectada"
        else:
            self.resultado.text = "✅ Mensaje parece seguro"

AntiEstafaApp().run()
