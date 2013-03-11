from plone.app.testing import PloneWithPackageLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

import degu.forum


DEGU_FORUM = PloneWithPackageLayer(
    zcml_package=degu.forum,
    zcml_filename='testing.zcml',
    gs_profile_id='degu.forum:testing',
    name="DEGU_FORUM")

DEGU_FORUM_INTEGRATION = IntegrationTesting(
    bases=(DEGU_FORUM, ),
    name="DEGU_FORUM_INTEGRATION")

DEGU_FORUM_FUNCTIONAL = FunctionalTesting(
    bases=(DEGU_FORUM, ),
    name="DEGU_FORUM_FUNCTIONAL")
