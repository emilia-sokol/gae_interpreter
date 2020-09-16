import datetime

import unittest

from google.appengine.api import memcache
from google.appengine.ext import ndb
from google.appengine.ext import testbed

from src.model import Data, File, Output


class TestEntityGroupRoot(ndb.Model):
    """Entity group root"""
    pass


def get_entity_via_memcache(entity_key):
    """Get entity from memcache if available, from datastore if not."""
    entity = memcache.get(entity_key)
    if entity is not None:
        return entity
    key = ndb.Key(urlsafe=entity_key)
    entity = key.get()
    if entity is not None:
        memcache.set(entity_key, entity)
    return entity


class DatastoreTestCase(unittest.TestCase):

    def setUp(self):
        # First, create an instance of the Testbed class.
        self.testbed = testbed.Testbed()
        # Then activate the testbed, which prepares the service stubs for use.
        self.testbed.activate()
        # Next, declare which service stubs you want to use.
        self.testbed.init_datastore_v3_stub()
        self.testbed.init_memcache_stub()
        self.testbed.init_blobstore_stub()
        # Clear ndb's in-context cache between tests.
        # This prevents data from leaking between tests.
        # Alternatively, you could disable caching by
        # using ndb.get_context().set_cache_policy(False)
        ndb.get_context().clear_cache()

    def tearDown(self):
        self.testbed.deactivate()

    def testInsertEntity(self):
        Data().put()
        File().put()
        Output().put()

        self.assertEqual(1, len(Data.query().fetch(2)))
        self.assertEqual(1, len(File.query().fetch(2)))
        self.assertEqual(1, len(Output.query().fetch(2)))

    def testFilterByNumber(self):
        root = TestEntityGroupRoot(id="root")
        Data(parent=root.key).put()
        Data(id="9", type="number", value="200", time=datetime.datetime.utcnow(), parent=root.key).put()
        query = Data.query(ancestor=root.key).filter(
            Data.value == "200")
        results = query.fetch(2)
        self.assertEqual(1, len(results))
        self.assertEqual("200", results[0].value)

    def testGetEntityViaMemcache(self):
        data_key = Data(id="10", type="number", value="100", time=datetime.datetime.utcnow()).put().urlsafe()
        output_key = Output(id="4504699138998272", text="/blobstore/encoded_gs_file:test", timestamp=datetime.datetime.utcnow()).put().urlsafe()

        retrieved_data_entity = get_entity_via_memcache(data_key)
        self.assertNotEqual(None, retrieved_data_entity)
        self.assertEqual("number", retrieved_data_entity.type)

        retrieved_output_entity = get_entity_via_memcache(output_key)
        self.assertNotEqual(None, retrieved_output_entity)
        self.assertEqual("/blobstore/encoded_gs_file:test", retrieved_output_entity.text)
