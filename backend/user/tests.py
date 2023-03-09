from django.test import TestCase
from django.core import mail


class MailTestCase(TestCase):
    def setUp(self):
        self.email_to = "test@shoppe.com"
        self.email_from = "noreply@shoppe.com"
        self.subject = 'Subject here'
        self.message = 'Here is the message.'

    def test_send_email(self):
        self.assertEqual(
            mail.send_mail(
                self.subject,
                self.message,
                self.email_from,
                [self.email_to],
                fail_silently=False
            ), 1
        )
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(
            mail.outbox[0].subject, self.subject
        )
