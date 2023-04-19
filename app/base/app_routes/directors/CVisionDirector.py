from flask import render_template, request

from app.base.constants.BM_CONSTANTS import docs_templates_folder, output_docs
from app.base.db_models.ModelCvisionRun import ModelCvisionRun
from app.base.db_models.ModelProfile import ModelProfile
from app.base.db_models.ModelAPIDetails import ModelAPIDetails
from bm.apis.v1.APIHelper import APIHelper
from bm.controllers.cvision.ObjectDetectionCotroller import ObjectDetectionCotroller


class CVisionDirector:

    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['Tiger', 'Elephant', 'Wild Cat']

    @staticmethod
    def select_cvision_type():
        return render_template('applications/pages/cvision/selectvision.html', message='There is no active model')



