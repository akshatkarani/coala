from coalib.results.result_actions.ResultAction import ResultAction

from coala_utils.decorators import enforce_signature


class PrintMoreInfoAction(ResultAction):

    def __init__(self, additional_info):
        self.additional_info = additional_info

    @enforce_signature
    def is_applicable(self,
                      original_file_dict,
                      file_diff_dict,
                      applied_actions=()):
        if self.additional_info != '':
            return True
        return 'There is no additional info.'

    def apply(self, original_file_dict, file_diff_dict):
        """
        Print (M)ore info
        """
        print(self.additional_info)

        return file_diff_dict
