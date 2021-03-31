# -*- coding: utf-8 -*-
from foecluster.km.behaviors.focus_area import IFocusAreaMarker
from foecluster.km.testing import FOECLUSTER_KM_INTEGRATION_TESTING  # noqa
from plone.app.testing import setRoles, TEST_USER_ID
from plone.behavior.interfaces import IBehavior
from zope.component import getUtility

import unittest


class FocusAreaIntegrationTest(unittest.TestCase):

    layer = FOECLUSTER_KM_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_behavior_focus_area(self):
        behavior = getUtility(IBehavior, 'foecluster.km.focus_area')
        self.assertEqual(
            behavior.marker,
            IFocusAreaMarker,
        )
