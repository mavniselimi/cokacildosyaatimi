from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.app import App
import webbrowser
a=0.0
b="?"
n=0.0
k=""
g=""
class ghetto(GridLayout):
    def matCallback(self,a):
        webbrowser.open_new("https://us05web.zoom.us/j/2688374138?pwd=ekJpMnJsdWkyTWdGcE0zMEZzdjFydz09")
    def biyoCallback(self,a):
        webbrowser.open_new("https://us04web.zoom.us/j/8651192984?pwd=cFV0bUNPTXRUOGVPZWw4dEhDQm0vUT09")
    def edebCallback(self,a):
        webbrowser.open_new("https://us04web.zoom.us/j/4724567240?pwd=MzIzam5jcE9MeEkxTkVnR1plVVZ6dz09")
    def kimyaCallback(self,a):
        webbrowser.open_new("https://us04web.zoom.us/j/8080079163?pwd=UitJVWs4Y0dOU2ZjbHMvZUVBQVZXdz09")
    def tarihCallback(self,a):
        webbrowser.open_new("https://us04web.zoom.us/j/7045543550?pwd=yPBZGImZndgSF-Mj4JRTaFTq2Oh94Bs")
    def bilisiCallback(self,a):
        webbrowser.open_new("https://us02web.zoom.us/j/3469922894")
    def muzCallback(self,a):
        webbrowser.open_new("https://us04web.zoom.us/j/7411417677?pwd=K1A5czBGWWlnRzdBOWs0VEJQaUloUT09")
    def ingCallback(self,a):
        webbrowser.open_new("https://us04web.zoom.us/j/6712002142?pwd=azFMYjljb3lPOVBoTXdYT3FabmpIUT09")
    def felCallback(self,a):
        webbrowser.open_new("https://us04web.zoom.us/j/8358223221?pwd=eTlXcm4vc3RVUnNOSzV0UmhqM1ZEZz09")

    
        
    def __init__(self,**kwargs):
        super(ghetto, self).__init__(**kwargs)
        self.cols = 3
        self.btn1 = Button(text='MATEMATİK')
        self.btn1.bind(on_press=self.matCallback)
        self.btn2 = Button(text='KİMYA')
        self.btn2.bind(on_press=self.kimyaCallback)
        self.btn3 = Button(text='BİYOLOJİ')
        self.btn3.bind(on_press=self.biyoCallback)
        self.btn4 = Button(text='FELSEFE')
        self.btn4.bind(on_press=self.felCallback)
        self.btn6 = Button(text='EDEBİYAT')
        self.btn6.bind(on_press=self.edebCallback)
        self.btn7 = Button(text='BİLİŞİM')
        self.btn7.bind(on_press=self.bilisiCallback)
        self.btn5 = Button(text='TARİH')
        self.btn5.bind(on_press=self.tarihCallback)
        self.btn8 = Button(text='MÜZİK')
        self.btn8.bind(on_press=self.muzCallback)
        self.btn9 = Button(text='İNGİLİZCE')
        self.btn9.bind(on_press=self.ingCallback)
        self.add_widget(self.btn1)
        self.add_widget(self.btn2)
        self.add_widget(self.btn3)
        self.add_widget(self.btn4)
        self.add_widget(self.btn5)
        self.add_widget(self.btn6)
        self.add_widget(self.btn7)
        self.add_widget(self.btn8)
        self.add_widget(self.btn9)
        
    

class main(App):
    def build(self):
        return ghetto()

if __name__ == "__main__":
    main().run()
