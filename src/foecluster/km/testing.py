# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    applyProfile,
    FunctionalTesting,
    IntegrationTesting,
    PloneSandboxLayer,
)
from plone.testing import z2

import foecluster.km


class FoeclusterKmLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=foecluster.km)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'foecluster.km:default')


FOECLUSTER_KM_FIXTURE = FoeclusterKmLayer()


FOECLUSTER_KM_INTEGRATION_TESTING = IntegrationTesting(
    bases=(FOECLUSTER_KM_FIXTURE,),
    name='FoeclusterKmLayer:IntegrationTesting',
)


FOECLUSTER_KM_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FOECLUSTER_KM_FIXTURE,),
    name='FoeclusterKmLayer:FunctionalTesting',
)


FOECLUSTER_KM_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        FOECLUSTER_KM_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='FoeclusterKmLayer:AcceptanceTesting',
)
