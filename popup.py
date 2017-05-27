from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button 
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty
from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.event import EventDispatcher
from kivy.uix.behaviors import ButtonBehavior
from kivy.graphics import Rectangle

scoreInc = 0

class BG(BoxLayout):

    def __init__(self,**kwargs):
        super(BG,self).__init__(**kwargs)
        #self.launchPopup(self)

    def popupClose(self,obj):
        try:
            Clock.unschedule(self.incrementerFnc)
        except Exception: 
            pass

    def launchPopup(self,obj):
            global scoreInc

            scoreInc = 0
            
            content = BoxLayout(orientation='vertical')
            
            self.incrementerFnc = Clock.schedule_interval(self.incrementer, .005)

            app = App.get_running_app()
        
            app.scoreLabel = Label(text=str(ins.a), id='scorelabel', font_size='100sp', color=(1.0, 0.0, 0.0, 1.0))

            content.add_widget(app.scoreLabel)

            btn1 = Button(text='Close', size_hint=(1, 1), background_color = (1.0, 0.0, 0.0, 1.0), background_normal = '', border=(8, 8, 8, 8), keep_ratio=True, font_size='24sp')
            
            content.add_widget(btn1)

            popup = Popup(title='Winner!', title_align='center', title_size='40sp', title_color=(1.0, 0.0, 0.0, 1.0), background_color = (0.0, 0.0, 0.0, 0.6), size_hint=(.8, .5), border=(0,0,0,0), separator_height=0, content=content, size_hint_max_y=300, size_hint_max_x=150, background = 'images/track/popup_background.jpg')
            
            btn1.bind(on_press = popup.dismiss)
            
            popup.bind(on_dismiss=lambda *_: self.popupClose(self))
            
            popup.open()
            

    def incrementer(self, dt):
        global scoreInc
        
        scoreInc += 3

        ins.a = scoreInc

        if(scoreInc >= 3000):
            ins.a = 3000
            Clock.unschedule(self.incrementerFnc)

class MyClass(EventDispatcher):
    a = NumericProperty(0)
    def on_a(self, instance, value):
        app = App.get_running_app()
        app.scoreLabel.text = str(value)

ins = MyClass()

root = Builder.load_string('''

BoxLayout:
    orientation: 'horizontal'
    size_hint: (1, 0)
    BG:
        orientation: 'vertical'
        id: bg
        canvas.before:
            Color:
                rgb: 1, 1, 1
            Rectangle:
                pos: self.pos
                size: self.size
        Button:
            text: "Launch Popup"
            size_hint: (1, 1)
            id: start_action
            on_press: root.ids.bg.launchPopup(self)
            font_size: '24sp'
            background_color: (0.0, 0.0, 0.0, 0.3)
            background_normal: ''
 ''')


class MyApp(App):

    def build(self):
        return root

MyApp().run()