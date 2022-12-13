from pyctuator.health.db_health_provider import DbHealthProvider
from pyctuator.health.redis_health_provider import RedisHealthProvider
from pyctuator.pyctuator import Pyctuator


class ActuatorAPI:
    """
        This class provides the information to activate https://pypi.org/project/pyctuator/
    """
    def __init__(self, app):
        self.pyctuator = Pyctuator(
            app,
            "FastAPI Pyctuator",
            app_url="http://0.0.0.0:8000",
            pyctuator_endpoint_url="http://0.0.0.0:8000/actuator",
            registration_url=None,
            # logger=logging.getLogger("uvi")  #  Add loggers
        )

    def register_sql_db_health_provider(self, engine):
        """Register SQL DB"""
        self.pyctuator.register_health_provider(DbHealthProvider(engine))

    def register_redis_db_health_provider(self, engine):
        """Register Redis DB"""
        self.pyctuator.register_health_provider(RedisHealthProvider(engine))
