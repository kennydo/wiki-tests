#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from page import Page
import personal_tools_region


class BasePage(Page):

    _page_title_locator = (By.CSS_SELECTOR, "#page-title")

    @property
    def personal_tools_region(self):
        return personal_tools_region.PersonalToolsRegion(self.testsetup)

    @property
    def page_title(self):
        return self.selenium.find_element(*self._page_title_locator).text
