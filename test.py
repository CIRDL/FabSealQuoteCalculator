import PySimpleGUI as sg


sg.theme("dark grey 14")

layout = [[sg.Text("Enter diameter of tank:")],
          [sg.InputText(enable_events=True, size=(5, 2), key="tank_dm_ft"), sg.Text("ft."),
           sg.InputText(enable_events=True, size=(3, 2), key="tank_dm_in"), sg.Text("in.")],
          [sg.Text(size=(40, 2))],
          [sg.Text("Enter depth of tank:")],
          [sg.InputText(enable_events=True, size=(5, 2), key="tank_dp_ft"), sg.Text("ft."),
           sg.InputText(enable_events=True, size=(3, 2), key="tank_dp_in"), sg.Text("in.")],
          [sg.Text("Please enter any extensions to depth:"),
           sg.InputText(enable_events=True, size=(3, 2), key="tank_dp_ex_in"), sg.Text("in.")],
          [sg.Text(size=(40, 2))],
          [sg.Button("Next", size=(6, 1))]]

window = sg.Window("Quote Calculator", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break

    if event == "Next":
        diameter_ft = values["tank_dm_ft"]
        diameter_inch = values["tank_dm_in"]
        depth_ft = values["tank_dp_ft"]
        depth_inch = values["tank_dm_in"]
        depth_extensions = values["tank_dp_ex_in"]

window.close()
