class Bill:
    """
    Object that contains data about a bill, such as the total amount and the period of the bill.
    """
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Object that describes a person who pays a share of the bill.
    """
    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill):
        pass


class PdfReport:
    """
    Generates a PDF file which contains data regarding the flatmates, their due amount and the period of the bill.
    """
    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pass


def main():
    """
    Main function that runs on execution.
    :return:
    """


main()
