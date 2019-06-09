from coalib.misc.Shell import run_shell_command
from coalib.results.result_actions.ResultAction import ResultAction


class AddNewLineAction(ResultAction):

    SUCCESS_MESSAGE = 'New Line added successfully.'

    def __init__(self, message, shortlog, body):
        self.message = message
        self.shortlog = shortlog
        self.body = body

    def is_applicable(self,
                      original_file_dict,
                      file_diff_dict,
                      applied_actions=()):
        return 'AddNewLineAction' not in file_diff_dict

    def apply(self, original_file_dict, file_diff_dict, **kwargs):
        """
        Add (N)ewline
        """
        new_commit_message = '{}\n\n{}'.format(self.shortlog, self.body)
        command = 'git commit --amend -m "{}"'.format(new_commit_message)
        stdout, err = run_shell_command(command)
        file_diff_dict['AddNewLineAction'] = True
        return file_diff_dict
