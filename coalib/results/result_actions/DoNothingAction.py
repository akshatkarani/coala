from coalib.results.result_actions.ResultAction import ResultAction


class DoNothingAction(ResultAction):

    SUCCESS_MESSAGE = ''

    is_applicable = lambda *args: True

    def apply(self,
              original_file_dict,
              file_diff_dict):
        """
        Do (N)othing
        """
