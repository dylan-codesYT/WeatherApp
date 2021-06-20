from controller.controller import Controller

from model.weather import Weather

if __name__ == '__main__':
    #Controller().main()

    w = Weather()
    print(w.getCurrentTempF()) 