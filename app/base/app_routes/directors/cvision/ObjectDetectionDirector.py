from flask import render_template, request

from app.base.constants.BM_CONSTANTS import docs_templates_folder, output_docs
from app.base.db_models.ModelAPIDetails import ModelAPIDetails
from app.base.db_models.ModelCvisionRun import ModelCvisionRun
from app.base.db_models.ModelProfile import ModelProfile
from bm.apis.v1.APIHelper import APIHelper


class ObjectDetectionDirector:

    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['Tiger', 'Elephant', 'Wild Cat']

    def createobjectdetection(self, ds_goal, ds_source):
        return 0

    def showobjdetectrmodeldashboard(self,profile):
        page_url = "{0}cvision/{1}/objtdetect/detect".format(request.host_url, str(profile['model_id']))
        page_embed = "<iframe width='500' height='500' src='" + page_url + "'></iframe>"
        run_history = ModelCvisionRun.query.filter_by( model_id = str(profile['model_id'])).all()
        return render_template('applications/pages/cvision/objectdetection/dashboard.html',
                               message='No', run_history=run_history,
                               fname=profile['model_name'],page_url=page_url, page_embed=page_embed,
                               segment='showdashboard', created_on=profile['created_on'],
                               ds_goal=profile['ds_goal'],model_id=profile['model_id'],
                               updated_on=profile['updated_on'], last_run_time=profile['last_run_time'])

    def detect_object(self, model_id, runid, desc, host, uname, pword, webcam=31):
        try:
            objectdetectioncontroller = "ObjectDetectionCotroller()"
            run_identifier = "%s%s%s" % (model_id, '_', runid)
            labelfileslink, labeled = objectdetectioncontroller.labelfiles(run_identifier, desc, host, uname, pword, webcam, 27)

            return render_template('applications/pages/cvision/objectdetection/labelfiles.html',
                                   message='No', labeled = labeled, model_id=model_id, run_id=runid,
                                   downloadlink= labelfileslink)
        except Exception as e:
            print(e)
            return 0



