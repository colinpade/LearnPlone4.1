from plone.app.testing import (
    PloneSandboxLayer,
    applyProfile,
    PLONE_FIXTURE,
    IntegrationTesting,
)

from zope.configuration import xmlconfig

class OptiluxPolicy(PloneSandboxLayer):
	defaultBases = (PLONE_FIXTURE,)
	def setUpZope(self, app, configurationContext):
                 # Load ZCML
		import optilux.policy
		xmlconfig.file('configure.zcml',
				optilux.policy,
				context=configurationContext
			      )
	def setUpPloneSite(self, portal):
		applyProfile(portal, 'optilux.policy:default')
OPTILUX_POLICY_FIXTURE = OptiluxPolicy()
OPTILUX_POLICY_INTEGRATION_TESTING = IntegrationTesting(
		bases=(OPTILUX_POLICY_FIXTURE,),
		name="Optilux:Integration"
		)
