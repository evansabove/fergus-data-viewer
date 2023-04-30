from threading import Thread
from data_connector import DataConnector
import obd
from argparse import ArgumentParser
from user_interface import UserInterface

data_points = [obd.commands.COOLANT_TEMP]
live_data = { i.name : None for i in data_points }
ui = UserInterface()

def update_screen():
    print(live_data)

def show_splash_screen():
    ui.write_label("Fergus")

if __name__ == "__main__":
    show_splash_screen()

    parser = ArgumentParser()
    parser.add_argument("--mock", default=False)
    parser.add_argument("--port", default="\\.\\COM3")
    args = parser.parse_args()

    use_mock = args.mock is not None and args.mock == 'True'

    data_connector = DataConnector(live_data, data_points, use_mock, args.port)
    data_connector_thread = Thread(target=data_connector.start)

    try:
        data_connector_thread.start()
    except KeyboardInterrupt:
        data_connector.stop()
    except Exception as e:
        print(e)

    print("Program finished")