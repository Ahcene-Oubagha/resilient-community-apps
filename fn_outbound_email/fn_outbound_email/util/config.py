# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

"""Generate a default configuration-file section for fn_outbound_email"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """ 
    return u"""[fn_outbound_email]
# SMTP SERVER (IP ADDRESS or FQDN)
smtp_server=xxx.xxx.xxx.xxx

#Blank for initial selftest, both required for TLS 
smtp_user=
smtp_password=

#If smtp_user is not an email address then from_email_address should equal the email address
from_email_address=

# SMTP PORT NUMBER, 25 or 587/2525
smtp_port=587

# SMTP CONNECTION TIMEOUT IN SECONDS
smtp_conn_timeout=20

# SMTP SSL MODE = (starttls, ssl, None)
smtp_ssl_mode=starttls

# SSL Cert (not supported)
#smtp_ssl_cafile=
# Optional - Path to a custom template file for formatting HTML email.
# The integration will use this template out of the box. If removed, it will default to the pre-processing script.
# template_file=data/templates/example_send_email.jinja
template_file=data/templates/example_send_email.jinja
    """
