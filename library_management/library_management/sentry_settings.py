import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="https://f594938a6b7647c6bd0baef9e1fc9a9d@o1324204.ingest.sentry.io/6582244",
    integrations=[
        DjangoIntegration(),
    ],
    traces_sample_rate=1.0,
    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True,
)
