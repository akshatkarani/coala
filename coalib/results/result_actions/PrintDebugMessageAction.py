from coalib.results.result_actions.ResultAction import ResultAction

from coala_utils.decorators import enforce_signature


class PrintDebugMessageAction(ResultAction):

    def __init__(self, debug_msg):
        self.debug_msg = debug_msg

    @enforce_signature
    def is_applicable(self,
                      original_file_dict,
                      file_diff_dict,
                      applied_actions=()):
        if self.debug_msg != '':
            return True
        return 'There is no debug message.'

    def apply(self, original_file_dict, file_diff_dict):
        """
        Print (D)ebug message
        """
        print(self.debug_msg)

        return file_diff_dict
