# import subprocess

from mapreduce import context


def r_mapper_interpreter(entity):
    # @TODO implementation
    # @TODO add conditional imports based on mapper requirements
    ctx = context.get()
    file_blob_key = ctx.mapreduce_spec.mapper.params['mapper']

    # Define command and arguments
    command = 'Rscript'
    path2script = '/serve?blob-key=' + file_blob_key

    # Variable number of args in a list
    args = ['11', '3', '9', '42']

    # Build subprocess command
    cmd = [command, path2script] + args

    # check_output will run the command and store to result
    # x = subprocess.check_output(cmd, universal_newlines=True)

    print('The maximum of the numbers is:', x)
