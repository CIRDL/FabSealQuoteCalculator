import PySimpleGUI as sg


def empty_response(response, empty_field):
    if response == "":
        sg.theme("dark grey 14")
        layout = [[sg.Text("Enter missing value for ", empty_field, ":")],
                  [sg.InputText(enable_events=True, key="event")]]

        window = sg.Window("Quote Calculator", layout)

        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                break

            if event == "Next":
                response = values[event]

        window.close()

    return response

