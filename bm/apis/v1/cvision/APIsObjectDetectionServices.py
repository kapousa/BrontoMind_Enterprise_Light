import json

import numpy
from flask import request

from bm.apis.v1.APIsPredictionServices import NpEncoder
from bm.db_helper.AttributesHelper import get_model_name, get_features, get_labels
from bm.utiles.Helper import Helper


class APIsObjectDetectionServices:

    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['Tiger', 'Elephant', 'Wild Cat']
