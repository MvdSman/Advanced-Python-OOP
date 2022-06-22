from flat import Bill, Flatmate
from reports import PdfReport


def main():
    """
    Main function that runs on execution.
    :return:
    """

    # Get user inputs
    bill_amount = float(input("Enter the bill amount: "))
    bill_period = input("Enter the bill period (e.g. December 2020): ")
    fm1_name = input("Enter the name of the first flatmate: ")
    fm1_days = int(input(f"How many days did {fm1_name} stay in the house during the bill period of {bill_period}? "))
    fm2_name = input("Enter the name of the second flatmate: ")
    fm2_days = int(input(f"How many days did {fm2_name} stay in the house during the bill period of {bill_period}? "))

    # Create instances
    the_bill = Bill(bill_amount, bill_period)
    flatmate1 = Flatmate(name=fm1_name, days_in_house=fm1_days)
    flatmate2 = Flatmate(name=fm2_name, days_in_house=fm2_days)

    print(
        f"Total bill:\t{the_bill.amount}\n"
        f"{flatmate1.name} pays:\t{flatmate1.pays(bill=the_bill, flatmate2=flatmate2)}\n"
        f"{flatmate2.name} pays:\t{flatmate2.pays(bill=the_bill, flatmate2=flatmate1)}"
    )

    pdf_report = PdfReport(filename=f"{the_bill.period}.pdf")
    pdf_report.generate(flatmate1, flatmate2, bill=the_bill)


main()
