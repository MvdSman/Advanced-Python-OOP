import yagmail

class Mailer:
    """

    """
    def __init__(self):
        user = 'YOUR-GMAIL-ADDRESS'
        password = 'YOUR-GMAIL-PASSWORD'
        self.email = yagmail.SMTP(user=user, password=password)

    def send(self, to, subject, contents, attachments=None):
        """
        Send an email with an optional attachment.

        NOTE: An `yagmail.error.YagAddressError` might occur,
        but the email would still send.

        :param to: email recipient.
        :param subject: email subject.
        :param contents: email contents.
        :param attachments: email attachments (optional).
        :return: None
        """
        if attachments:
            self.email.send(
                to=to,
                subject=subject,
                contents=contents,
                attachments=attachments
            )
        else:
            self.email.send(
                to=to,
                subject=subject,
                contents=contents
            )
        print(f'Email sent to {to}.')


if __name__ == "__main__":
    emailer = Mailer()
    emailer.send(
        to='aegxhpzio@yomail.info',
        subject='Daily NewsFeed test',
        contents='Test'
    )

