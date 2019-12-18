# -*- coding: utf-8 -*-
import warnings

from urllib3.exceptions import SNIMissingWarning

warnings.simplefilter("always", SNIMissingWarning)
