import webbrowser
from fpdf import FPDF

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
        # Instantiate PDF file
        pdf = FPDF(unit="pt")
        pdf.add_page()

        # Add content
        ## Add logo
        pdf.image("files/house.png", w=50, h=50)

        ## Insert title
        pdf.set_font(family="Times", size=24, style="B")
        pdf.cell(w=0, h=80, txt="Flatmates Bill", align="C", ln=1)

        ## Insert Period label + value
        pdf.set_font(family="Times", size=14, style="B")
        pdf.cell(w=150, h=40, txt="Period:", border=1)
        pdf.cell(w=200, h=40, txt=bill.period, border=1, ln=1)

        ## Set font for table
        pdf.set_font(family="Times", size=12)

        ## Insert flatmate1 name + due
        pdf.cell(w=150, h=40, txt=f"{flatmate1.name}:", border=1)
        pdf.cell(w=200, h=40, txt=str(flatmate1.pays(bill, flatmate2)), border=1, ln=1)

        ## Insert flatmate2 name + due
        pdf.cell(w=150, h=40, txt=f"{flatmate2.name}:", border=1)
        pdf.cell(w=200, h=40, txt=str(flatmate2.pays(bill, flatmate1)), border=1, ln=1)

        ## Insert Total due
        pdf.set_font(family="Times", size=12, style="B")
        pdf.cell(w=150, h=40, txt="Total due:", border=1)
        pdf.cell(w=200, h=40, txt=str(bill.amount), border=1, ln=1)

        # Export PDF and open file
        pdf.output(self.filename)
        webbrowser.open(self.filename)


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

    pdf_report = PdfReport(filename="bill.pdf")
    pdf_report.generate(flatmate1=john, flatmate2=mary, bill=the_bill)


main()
