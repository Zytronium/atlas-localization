#!/usr/bin/env python3
"""
todo
"""

from babel import Babel, _
from flask_babel import ngettext

greeting = _("Hello, World!")

message = ngettext("You have one message", "You have %(num)d messages", num)
