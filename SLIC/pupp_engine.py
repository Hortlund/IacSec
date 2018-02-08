'''
Akond Rahman
Feb 08, 2018
Puppet Lint Engine
'''
import constants
import subprocess
import os

def generateOutput(path2file):
    ## Add rules to check automatically here
    rulesToCheck = [constants.PP_RULE_HARDCODE, constants.PP_RULE_SUSP_COMM]
    for rule_ in rulesToCheck:
        ##
        command2exec = constants.PP_LINT_TOOL + ' ' + rule_ + ' ' + path2file + ' ' + constants.REDIRECT_APP + ' ' + constants.OUTPUT_TMP_LOG
        try:
           # print command2exec
           subprocess.check_output(['bash','-c', command2exec])
        except subprocess.CalledProcessError as e_:
           print constants.EXCEPTION + str(e_)
        # raise RuntimeError("command '{}' return with error (code {}): {}".format(e_.cmd, e_.returncode, e_.output))

def getOutputLines():
    file_ = open(constants.OUTPUT_TMP_LOG, 'rU', errors='ignore'):
    file_str = file_.read()
    file_lines = file_str.split(constants.NEWLINE)
    return file_lines

def getHardCodeCount():
    file_lines = getOutputLines()
    cnt2ret = sum(constants.PUPP_HARD in s_ for s_ in file_lines)
    return cnt2ret

def getSuspCommCount():
    file_lines = getOutputLines()
    cnt2ret = sum(constants.PUPP_SUSP in s_ for s_ in file_lines)
    return cnt2ret

def parseOutput():
    rul_hardcode_cnt, rul_susp_comm_cnt = 0, 0
    num_lines = sum(1 for line_ in open(constants.OUTPUT_TMP_LOG))
    print 'Genrated a log file of {} lines'.format(num_lines)
    if num_lines > 0:
        rul_hardcode_cnt  = getHardCodeCount()
        rul_susp_comm_cnt = getSuspCommCount()

    output2ret = (rul_hardcode_cnt, rul_susp_comm_cnt)
    return output2ret
def runLinter(full_path_file):
    #1. run linter with custom rules
    generateOutput(full_path_file)
    #2. parse output
    all_rul_cnt_out = parseOutput()
    #3. delete temp file
    os.remove(constants.OUTPUT_TMP_LOG)
    return all_rul_cnt_out
