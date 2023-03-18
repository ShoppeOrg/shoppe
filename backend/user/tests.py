from django.conf import settings
from django.core import mail
from django.template import loader
from django.test import TestCase


class MailTestCase(TestCase):
    def setUp(self):
        self.email_to = "test@shoppe.com"
        self.email_from = "noreply@shoppe.com"
        self.subject = "Subject here"
        self.message = "Here is the message."
        self.email_template = settings.PASSWORDLESS_AUTH.get(
            "PASSWORDLESS_EMAIL_TOKEN_HTML_TEMPLATE_NAME"
        )

    def test_send_email(self):
        self.assertEqual(
            mail.send_mail(
                self.subject,
                self.message,
                self.email_from,
                [self.email_to],
                fail_silently=False,
            ),
            1,
        )
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, self.subject)

    def test_email_template(self):
        template_str = loader.render_to_string(
            self.email_template, {"callback_token": 485929}
        )
        self.assertIn("485929", template_str)
