from flask import render_template
from markupsafe import Markup


class ForecastingDirector:

    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['Tiger', 'Elephant', 'Wild Cat']

    def specify_forecating_properties(self, file_location, headersArray, message):
        time_forecasting_controller = "TimeForecastingController()"
        forecasting_columns, depended_columns, datetime_columns = time_forecasting_controller.analyize_dataset(
            file_location)
        message = (message if ((len(forecasting_columns) != 0) and (
                len(datetime_columns) != 0) and (
                                       len(depended_columns) != 0)) else 'Your data file doesn not have one or more required fields to build the timeforecasting model. The file should have:<ul><li>One or more ctaegoires columns</li><li>One or more time series columns</li><li>One or more columns with numerical values.</li></ul><br/>Please check your file and upload it again.')
        return render_template('applications/pages/forecasting/dsfileanalysis.html',
                               headersArray=headersArray,
                               segment='createmodel', message=Markup(message),
                               forecasting_columns=forecasting_columns,
                               depended_columns=depended_columns,
                               datetime_columns=datetime_columns)