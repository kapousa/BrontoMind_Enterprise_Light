import os

import numpy
import pandas as pd
from flask import render_template, request, current_app, session
from markupsafe import Markup

from app.base.constants.BM_CONSTANTS import progress_icon_path, loading_icon_path, df_location, docs_templates_folder, \
    output_docs
from app.base.db_models.ModelAPIDetails import ModelAPIDetails

from app.base.db_models.ModelProfile import ModelProfile
from bm.apis.v1.APIHelper import APIHelper
from bm.controllers.BaseController import BaseController
from bm.datamanipulation.DataCoderProcessor import DataCoderProcessor
from bm.db_helper.AttributesHelper import get_labels, get_features, get_model_name
from bm.controllers.classification.ClassificationController import ClassificationController
from bm.utiles.Helper import Helper


class ForecastingDirector:

    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['Tiger', 'Elephant', 'Wild Cat']

