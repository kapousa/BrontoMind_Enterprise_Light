import json

import numpy

from bm.apis.v1.APIsPredictionServices import NpEncoder
from bm.controllers.classification.ClassificationController import ClassificationController
from bm.db_helper.AttributesHelper import get_model_name, get_features, get_labels


class APIsClusteringServices:

    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['Tiger', 'Elephant', 'Wild Cat']

    def cluster_data_list(self, content):
        cluster_data_json = {}
        for i in range(len(content)):
            class_item = self.cluster_data(content[i])
            cluster_data_json[i] = class_item
        json_data = json.dumps(cluster_data_json, cls=NpEncoder)

        return json_data
