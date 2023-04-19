from flask import render_template, session

from app.base.app_routes.directors.CVisionDirector import CVisionDirector
from app.base.app_routes.directors.cvision.ObjectDetectionDirector import ObjectDetectionDirector


class CVisionFactory:

    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['Tiger', 'Elephant', 'Wild Cat']

    def selectcvisiontype(self, request):
        session['ds_goal'] = request.args.get("t")
        return CVisionDirector.select_cvision_type()