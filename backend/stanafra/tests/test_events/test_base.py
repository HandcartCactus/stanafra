from unittest import TestCase
from fastapi.testclient import TestClient
from stanafra.app.application import create_application


class TestBaseEventHandler(TestCase):
    def test_startup_handler(self):
        app = create_application()
        with self.assertLogs('stanafra', level='INFO') as cm:

            with TestClient(app):
                pass
            self.assertEqual(cm.output,
                             ['INFO:stanafra:Starting up ...',
                              'INFO:stanafra:Shutting down ...'])
