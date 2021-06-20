from view.view import View


class Controller:

    def __init__(self) -> None:
        self.view = View()

    def main(self):
        self.view.main()