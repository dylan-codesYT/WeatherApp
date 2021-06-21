from model.mapbox import MapBox
from view.view import View
from model.weather import Weather
from model.mapbox import MapBox

class Controller:

    def __init__(self) -> None:
        self.view = View(self)
        self.weather = Weather()
        self.mapbox = MapBox()

        self.updateGUI()


    def main(self):
        self.view.main()

    
    def updateGUI(self):
        if 'error' not in self.weather.weatherData:
            self.view.varLocation.set(self.weather.getLocation())
            self.view.varCondition.set(self.weather.getConditionText())
            self.view.varWindSpeed.set(self.weather.getWindSpeedMPH())
            self.view.varWindDir.set(self.weather.getWindDirection())

            if self.view.varUnits.get() == 1:
                self.view.varTemp.set(self.weather.getCurrentTempF())
                self.view.varFeelsLike.set(self.weather.getFeelsLikeF())
            else:
                self.view.varTemp.set(self.weather.getCurrentTempC())
                self.view.varFeelsLike.set(self.weather.getFeelsLikeC())


    def handleButtonSearch(self, event=None):
        location = self.view.varSearch.get()
        if location != '':
            self.weather = Weather(location)
            self.updateGUI()


    def handleComboSearch(self, event=None):
        location = self.view.varSearch.get()
        if len(location) > 3:
            self.mapbox.updateQuery(location)
            self.view.comboSearch.configure(values=self.mapbox.getNames())
        else:
            self.view.comboSearch.configure(values=[])