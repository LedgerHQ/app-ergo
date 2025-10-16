import random
from ragger.conftest import configuration

###########################
### CONFIGURATION START ###
###########################

configuration.OPTIONAL.CUSTOM_SEED = "jaguar swallow dinner course lend surround warm robot grape pear skate relief"

#########################
### CONFIGURATION END ###
#########################

# Pull all features from the base ragger conftest using the overridden configuration
pytest_plugins = ("ragger.conftest.base_conftest", )

random.seed(0)
