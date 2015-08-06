from plone.app.testing import (
    PloneSandboxLayer,
    applyProfile,
    PLONE_FIXTURE,
    IntegrationTesting,
)

from zope.configuration import xmlconfig

from plone.testing import z2

class OptiluxPolicy(PloneSandboxLayer):
	defaultBases = (PLONE_FIXTURE,)
	def setUpZope(self, app, configurationContext):
                 # Load ZCML
		import optilux.policy
		xmlconfig.file('configure.zcml',
				optilux.policy,
				context=configurationContext
			      )
		# Install products that use an old-style initialize()
		# function
		z2.installProduct(app, 'Products.PythonField')
		z2.installProduct(app, 'Products.TALESField')
		z2.installProduct(app, 'Products.TemplateFields')
		z2.installProduct(app, 'Products.PloneFormGen')

	def tearDownZope(self, app):
		z2.uninstallProduct(app, 'Products.PloneFormGen')
		z2.uninstallProduct(app, 'Products.TemplateFields')
		z2.uninstallProduct(app, 'Products.TALESField')
		z2.uninstallProduct(app, 'Products.PythonField')
	
	def setUpPloneSite(self, portal):
		applyProfile(portal, 'optilux.policy:default')
OPTILUX_POLICY_FIXTURE = OptiluxPolicy()
OPTILUX_POLICY_INTEGRATION_TESTING = IntegrationTesting(
		bases=(OPTILUX_POLICY_FIXTURE,),
		name="Optilux:Integration"
		)
