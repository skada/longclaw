from wagtail.core.models import Site

from longclaw.configuration.models import Configuration


def currency(request):
    config = Configuration.for_site(Site.find_for_request(request))
    return {
        'currency_html_code': config.currency_html_code,
        'currency': config.currency
    }
