from flask import render_template, request, send_file

from flask import render_template, request, send_file

from app.base.constants.BM_CONSTANTS import labeled_data_filename, labeled_data_filename_download_path
from bm.controllers.BaseController import BaseController


class ClusteringDirector:

    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['Tiger', 'Elephant', 'Wild Cat']

    def prepare_date_files(self):
        # 1. Collect uploaded data files
        # 1. Collect uploaded data files
        return 0


    def show_model_status(self):
        try:
            model_profile = BaseController.get_model_status()
            page_url = request.host_url + "getdatacluster?" + + "&m=" + str(model_profile['model_id'])

            page_embed = "<iframe width='500' height='500' src='" + page_url + "'></iframe>"

            return render_template('applications/pages/clustering/modelstatus.html',
                                       train_precision=model_profile['train_precision'],
                                       train_recall=model_profile['train_recall'],
                                       train_f1=model_profile['train_f1'],
                                       test_precision=model_profile['test_precision'],
                                       test_recall=model_profile['test_recall'],
                                       test_f1=model_profile['test_f1'],
                                       segment='createmodel', page_url=page_url, page_embed=page_embed,
                                       created_on=model_profile['created_on'],
                                       updated_on=model_profile['updated_on'],
                                       last_run_time=model_profile['last_run_time'],
                                       fname=model_profile['file_name'])

        except Exception as e:
            return render_template('page-501.html', error=e, segment='message')

    def show_text_model_dashboard(self):
        profile = BaseController.get_model_status()
        page_url = request.host_url + "getdatacluster?t=" + str(profile['ds_goal']) + "&s=" + str(profile['ds_source'])  + "&m=" + str(profile['model_id'])
        page_embed = "<iframe width='500' height='500' src='" + page_url + "'></iframe>"

        return render_template('applications/pages/classification/textdashboard.html',
                               train_precision=profile['train_precision'],
                               train_recall=profile['train_recall'],
                               train_f1=profile['train_f1'],
                               test_precision=profile['test_precision'],
                               test_recall=profile['test_recall'],
                               test_f1=profile['test_f1'],
                               message='No',
                               fname=profile['model_name'], page_url=page_url, page_embed=page_embed,
                               segment='showdashboard', created_on=profile['created_on'],
                               ds_goal=profile['ds_goal'],
                               updated_on=profile['updated_on'], last_run_time=profile['last_run_time'],
                               plot_image_path = profile['plot_image_path'])


    @staticmethod
    def download_labeled_datafile():
        """
        Download the labeled data file
        @param request:
        @return:
        """
        try:
            path = "%s%s" %  (labeled_data_filename_download_path, labeled_data_filename)
            return send_file(path, as_attachment=True)

        except Exception as e:
            return render_template('page-501.html', error=e, segment='message')
