import unittest,sys
from os.path import expanduser
sys.path.append(expanduser('~'))


class TestStorage(unittest.TestCase):

    def test_storage(self):
        from node.storage.storage import storage_read_only
        s = storage_read_only(dbfile='/home/nuc/node/www/poh/storage/sensor_data.db')
        print s.read_latest_non_null('node-008','ReceptionTime','d2w')
        #self.assertTrue(parse_SeaFET(m) is not None)


if __name__ == '__main__':
    unittest.main()
