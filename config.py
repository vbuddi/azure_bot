#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "f8e62c91-e626-468e-81d3-18493f4112f5")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "e3v8Q~94~YDyGdvXxAh_XmdfZVJQ3lRep4vIkbH0")
