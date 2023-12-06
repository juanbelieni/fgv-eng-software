import PySimpleGUIQt as sg

sg.theme_background_color("#FFF7E7")

layout = [[sg.Text("What's your name?")],
          [sg.Input()],
          [sg.Button('Ok')]]

window = sg.Window(
    'Sorvil',
    layout,
    font=("Arial", 12),
)

event, values = window.read()

# print('Hello', values[0], "! Thanks for trying PySimpleGUI")

window.close()

# from models.user import UserRepository

# user_repository = UserRepository()

# print(user_repository.get_user_from_id("123"))
