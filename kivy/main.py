from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
import instructions

class CustomButton(Button):
    def __init__(self, screen = "MainScreen", goal = "FirstScreen", direction="up", **kwargs):
        super().__init__(**kwargs)
        self.screen = screen
        self.goal = goal
        self.direction = direction
 
    def on_press(self):
        self.screen.manager.transition.direction = self.direction
        self.screen.manager.current = self.goal

# def checkNumber(n):
#     if n.isdigit()==True:
#         b=int(n)
#         #digits=set([char for char in n])
#         if (b>=7):
#             return True
#         else:
#             return False
#     else:
#         return False

# def next():
#     global age_input
#     age = age_input.text
#     try:
#         age = int(age)
#         return True
#     except ValueError:
#         return False
#     retur
# def check_int(value):
#     if isinstance(value, int):
#         return True
#     else:
#         return False

# def next():
#     assert check_int(self.age_input.text) or text

class InstructionScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
 
        inrtuction = Label(text=instructions.txt_instruction, size_hint=(1, 4))
 
        main_layout = BoxLayout(orientation="vertical", spacing = 5)
        main_layout.add_widget(inrtuction)
 
        name_layout = BoxLayout(pos_hint={'center_x': 0.5, 'center_y': 0.5})
        age_layout = BoxLayout(pos_hint={'center_x': 0.5, 'center_y': 0.5})
 
        name_label = Label(text="Введіть ваше ім'я:", size_hint=(0.5, 0.3))
        age_label = Label(text="Введіть ваш вік:", size_hint=(0.5, 0.3))
 
        name_input = TextInput(multiline=False, size_hint=(2, 0.3))
        # def getNumber02 ():
        #     while True:
        #         age_input1 = TextInput(multiline=False, size_hint=(2, 0.3))
        #         if age_input.isdigit():
        #             return age_input1
        # age_input = age_input1
        age_input = TextInput(multiline=False, size_hint=(2, 0.3))
 
        name_layout.add_widget(name_label)
        name_layout.add_widget(name_input)
 
        age_layout.add_widget(age_label)
        age_layout.add_widget(age_input)
 
        main_layout.add_widget(name_layout)
        main_layout.add_widget(age_layout)

        self.next_screen_button = CustomButton(screen=self, goal="PulseScreen", direction="left", text="Почати", size_hint=(0.5, 0.3), pos_hint={'center_x': 0.5})
 
        main_layout.add_widget(self.next_screen_button)
 
        self.add_widget(main_layout)
        return age_input

class PulseScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
 
        self.instr = Label(text = instructions.txt_test1)
 
        line = BoxLayout(size_hint=(0.8, None), height='30sp')
 
        lbl_result = Label(text='Введите результат:', halign='right')
        self.in_result = TextInput(text='0', multiline=False)
 
        line.add_widget(lbl_result)
        line.add_widget(self.in_result)

        self.btn = CustomButton(screen=self, goal="SitUpsScr", direction="left", text="Продолжить", size_hint=(0.5, 0.3), pos_hint={'center_x': 0.5})
 
        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(self.instr)
        outer.add_widget(line)
        self.line3 = BoxLayout(size_hint=(0.8, None), height='80sp', pos_hint={'center_x': 0.5})
        self.line3.add_widget(self.btn)
        outer.add_widget(self.line3)
 
        self.add_widget(outer)

class SitUpsScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
 
        self.instr = Label(text = instructions.txt_test2)
 
        line = BoxLayout(size_hint=(0.8, None), height='30sp')

        self.btn = CustomButton(screen=self, goal="PulseScr", direction="left", text="Продолжить", size_hint=(0.5, 0.3), pos_hint={'center_x': 0.5})
 
        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(self.instr)
        outer.add_widget(line)
        self.line3 = BoxLayout(size_hint=(0.8, None), height='80sp', pos_hint={'center_x': 0.5})
        self.line3.add_widget(self.btn)
        outer.add_widget(self.line3)
 
        self.add_widget(outer)

class PulseScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
 
        inrtuction = Label(text=instructions.txt_test3, size_hint=(1, 4))
 
        main_layout = BoxLayout(orientation="vertical", spacing = 5)
        main_layout.add_widget(inrtuction)
 
        name_layout = BoxLayout(pos_hint={'center_x': 0.5, 'center_y': 0.5})
        age_layout = BoxLayout(pos_hint={'center_x': 0.5, 'center_y': 0.5})
 
        name_label = Label(text="Результат:", size_hint=(0.5, 0.3))
        age_label = Label(text="Результат після відпочинку:", size_hint=(0.5, 0.3))
 
        name_input = TextInput(multiline=False, size_hint=(2, 0.3))
        age_input = TextInput(multiline=False, size_hint=(2, 0.3))
 
        name_layout.add_widget(name_label)
        name_layout.add_widget(name_input)
 
        age_layout.add_widget(age_label)
        age_layout.add_widget(age_input)
 
        main_layout.add_widget(name_layout)
        main_layout.add_widget(age_layout)
        
        if age:
            self.next_screen_button = CustomButton(screen=self, goal="EndScreen", direction="left", text="Завершити", size_hint=(0.5, 0.3), pos_hint={'center_x': 0.5})
        else:
            Label(text="jjh")
        main_layout.add_widget(self.next_screen_button)
 
        self.add_widget(main_layout)

class EndScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        global age
        name = Label(text="Олександр \nВаш індекс Руф'є: ")
        index = Label(text="fglkhj")
 
        line = BoxLayout(size_hint=(0.8, None), height='30sp')

        #self.btn = CustomButton(screen=self, goal="LastScr", direction="left", text="Продолжить", size_hint=(0.5, 0.3), pos_hint={'center_x': 0.5})
 
        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(name)
        outer.add_widget(index)
        #outer.add_widget(index)
        #outer2 = BoxLayout(orientation='vertical', padding=8, spacing=8)
        #outer.add_widget(self.index)
        outer.add_widget(line)
        self.line3 = BoxLayout(size_hint=(0.8, None), height='80sp', pos_hint={'center_x': 0.5})
        #self.line3.add_widget(self.btn)
        outer.add_widget(self.line3)
 
        self.add_widget(outer)

'''class LastScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
 
        self.instr = Label(text = instructions.txt_test2)
 
        line = BoxLayout(size_hint=(0.8, None), height='30sp')
 
        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(self.instr)
        outer.add_widget(line)
        self.line3 = BoxLayout(size_hint=(0.8, None), height='80sp', pos_hint={'center_x': 0.5})
        self.line3.add_widget(self.btn)
        outer.add_widget(self.line3)
 
        self.add_widget(outer)'''

class MyApp(App):
    def build(self):     
        sm = ScreenManager()
        sm.add_widget(InstructionScreen(name="InstructionScreen"))
        sm.add_widget(PulseScr(name="PulseScr"))
        sm.add_widget(SitUpsScr(name="SitUpsScr"))
        sm.add_widget(PulseScreen(name="PulseScreen"))
        sm.add_widget(EndScreen(name="EndScreen"))
        
        return sm

 
app = MyApp()
app.run()
 