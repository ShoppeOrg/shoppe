from django.conf import settings
from django.contrib.auth import get_user_model
from django.core import mail
from django.template import loader
from django.test import TestCase
from drfpasswordless.models import CallbackToken
from drfpasswordless.views import ObtainAuthTokenFromCallbackToken
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase


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


class AuthTestCase(APITestCase):
    fixtures = ["fixture.json"]

    @classmethod
    def setUpTestData(cls):
        cls.factory = APIRequestFactory()
        cls.user = get_user_model().objects.filter(is_staff=False).first()

    def test_auth_token_response(self):
        print("hello?", self.user)
        callback_token = CallbackToken.objects.create(
            user=self.user, to_alias_type="EMAIL", to_alias=self.user.email, type="AUTH"
        )
        request = self.factory.post(
            "/auth/token/", {"email": self.user.email, "token": callback_token.key}
        )
        response = ObtainAuthTokenFromCallbackToken.as_view()(request)
        self.assertIn("username", response.data)
        self.assertIn("token", response.data)
