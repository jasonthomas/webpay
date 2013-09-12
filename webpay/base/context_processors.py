from django.conf import settings
from webpay.pay.constants import PIN_ERROR_CODES


def defaults(request):
    return {'session': request.session,
            'STATIC_URL': settings.STATIC_URL,
            'PIN_ERROR_CODES': PIN_ERROR_CODES}
