import unittest2 as unittest
from optilux.policy.testing import OPTILUX_POLICY_INTEGRATION_TESTING
#from .testing import OPTILUX_POLICY_INTEGRATION_TESTING

class TestSetup(unittest.TestCase):
	layer = OPTILUX_POLICY_INTEGRATION_TESTING
	def test_portal_title(self):
		portal = self.layer['portal']
		self.assertEqual(
				"Optilux Cinemas",
				portal.getProperty('title'))
	def test_portal_description(self):
		portal = self.layer['portal']
		self.assertEqual(
				"Welcome to Optilux Cinemas",
				portal.getProperty('description'))
	def test_rold_added(self):
		portal = self.layer['portal']
		self.assertTrue("StaffMember" in portal.validRoles())
# told to add on page 130. Errors can't find getToolByName
#	def test_workflow_installed(self):
#		portal = self.layer['portal']
#		workflow = getToolByName(portal, 'portal_workflow')
#		self.assertTrue('optilux_sitecontent_workflow' in workflow)
#	def test_workflows_mapped(self):
#		portal = self.layer['portal']
#		workflow = getToolByName(portal, 'portal_workflow')
#		self.assertEqual(('optilux_sitecontent_workflow',),
#				workflow.getDefaultChain())
	def test_view_permission_for_staffmember(self):
		portal = self.layer['portal']
		self.assertTrue('View' in [r['name']
				for r in portal.permissionsOfRole('Reader')
				if r['selected']])
		self.assertTrue('View' in [r['name']
				for r in portal.permissionsOfRole('StaffMember')
				if r['selected']])
	def test_staffmember_group_added(self):
		portal = self.layer['portal']
		acl_users = portal['acl_users']
		self.assertEquals(1,
				len(acl_users.searchGroups(name='Staff')))
