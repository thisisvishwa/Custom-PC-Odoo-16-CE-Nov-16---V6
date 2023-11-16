```python
from odoo.tests import common

class TestPcBuild(common.TransactionCase):

    def setUp(self):
        super(TestPcBuild, self).setUp()
        self.PcBuild = self.env['pc.build']

    def test_create_pc_build(self):
        """
        Test the creation of a PC build
        """
        pc_build = self.PcBuild.create({
            'name': 'Test PC Build',
            # Add other necessary fields
        })
        self.assertEqual(pc_build.name, 'Test PC Build')

    def test_update_pc_build(self):
        """
        Test the update of a PC build
        """
        pc_build = self.PcBuild.create({
            'name': 'Test PC Build',
            # Add other necessary fields
        })
        pc_build.write({
            'name': 'Updated PC Build',
        })
        self.assertEqual(pc_build.name, 'Updated PC Build')

    def test_delete_pc_build(self):
        """
        Test the deletion of a PC build
        """
        pc_build = self.PcBuild.create({
            'name': 'Test PC Build',
            # Add other necessary fields
        })
        pc_build.unlink()
        self.assertEqual(len(self.PcBuild.search([])), 0)
```