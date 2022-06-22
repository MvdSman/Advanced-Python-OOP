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

    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        return round(bill.amount * weight, 2)

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
    the_bill = Bill(amount=120, period="March 2021")
    john = Flatmate(name="John", days_in_house=20)
    mary = Flatmate(name="Mary", days_in_house=25)

    print(
        f"Total bill:\t{the_bill.amount}\n"
        f"John pays:\t{john.pays(bill=the_bill, flatmate2=mary)}\n"
        f"Mary pays:\t{mary.pays(bill=the_bill, flatmate2=john)}"
    )


main()
