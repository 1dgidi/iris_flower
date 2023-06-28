
class DefaultMLModelException(Exception):
    '''
    Exception raised if the latest ml model is a default model, i.e. MLModel_instance.model_file == 'NA'
    '''
    def __init__(self, message='Latest model created is a default model'):
        self.message = message
        super().__init__(self.message)