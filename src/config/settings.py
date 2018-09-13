import os

DB_HOST_PATH = "sqlite:///data/db.sqlite3"
OSRM_HOSTPORT = os.getenv("OSRM_HOSTPORT", "localhost:5000")
DEFAULT_LOG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../logs/tmp")
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../data")

CENTER_LATITUDE = 40.75
CENTER_LONGITUDE = -73.90
LAT_WIDTH = 18.0 / 60
LON_WIDTH = 18.0 / 60
MIN_LAT, MIN_LON = CENTER_LATITUDE - LAT_WIDTH / 2.0, CENTER_LONGITUDE - LON_WIDTH / 2.0
MAX_LAT, MAX_LON = CENTER_LATITUDE + LAT_WIDTH / 2.0, CENTER_LONGITUDE + LON_WIDTH / 2.0
BOUNDING_BOX = [[MIN_LAT, MIN_LON], [MAX_LAT, MAX_LON]]
DELTA_LON = 21.0 / 3600
DELTA_LAT = 16.0 / 3600
MAP_WIDTH = int(LON_WIDTH / DELTA_LON) + 1
MAP_HEIGHT = int(LAT_WIDTH / DELTA_LAT) + 1

TIMESTEP = 60
MIN_DISPATCH_CYCLE = 60 * 7.5
MAX_DISPATCH_CYCLE = 60 * 10
GLOBAL_STATE_UPDATE_CYCLE = 60 * 5
OFF_DURATION = 60 * 60
PICKUP_DURATION = 60 * 1
MIN_WORKING_TIME = 3600 * 19
MAX_WORKING_TIME = 3600 * 20
ENTERING_TIME_BUFFER = 3600 * 5

DESTINATION_PROFILE_TEMPORAL_AGGREGATION = 3 #hours
DESTINATION_PROFILE_SPATIAL_AGGREGATION = 5 #(x, y) coordinates

# Not in use for now
DEMAND_AMPLIFICATION_FACTOR = 1.0