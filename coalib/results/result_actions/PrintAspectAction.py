from coalib.results.result_actions.ResultAction import ResultAction

from coala_utils.decorators import enforce_signature


class PrintAspectAction(ResultAction):

    def __init__(self, aspect):
        self.aspect = aspect

    @staticmethod
    @enforce_signature
    def is_applicable(self,
                      original_file_dict,
                      file_diff_dict,
                      applied_actions=()):
        if self.aspect is None:
            return 'There is no aspect associated with the result.'
        return True

    def apply(self, original_file_dict, file_diff_dict):
        """
        Print Aspec(T) Information
        """
        print(type(self.aspect).__qualname__ + '\n' +
              type(self.aspect).docs.definition)

        return file_diff_dict
