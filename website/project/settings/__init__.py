from split_settings.tools import optional, include
import os

try:
    site_domain = os.environ['SITE']
except:
    site_domain = None


if not site_domain:

    include(
        'components/base.py',
        'components/media.py',
        'components/template_cms.py',
        #'components/ecommerce.py',

        os.path.join(os.getcwd(), 'project/local_settings.py'),
        scope=locals()
    )