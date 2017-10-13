from github3 import GitHubEnterprise, GitHubError
from os import path, chdir, makedirs
from datetime import datetime
from subprocess import Popen, PIPE

# access token stored in file in home directory called .gt_git_credentials
CREDENTIALS_FILE = path.expanduser("~") +"/.gt_git_credentials"
SRC_DIR = path.expanduser("~/src/gt-github")
ERROR_LOG = SRC_DIR + "/gt_git_error.log"

with open(CREDENTIALS_FILE, 'r') as fd:
    token = fd.readline().strip()
error_log = open(ERROR_LOG, 'a+')

gt_gh = GitHubEnterprise('https://github.gatech.edu')
gt_gh.login('grome3', token=token)
repos = gt_gh.repositories()
chdir(SRC_DIR)

try:
    for r in repos:
        output, err = "", ""
        repo_path = SRC_DIR + '/' + str(r).split('/')[-1]
        if not path.isdir(repo_path):
            makedirs(repo_path)
            chdir(SRC_DIR)
            process = Popen(['git', 'clone', 'https://github.gatech.edu/' + str(r)], stdout=PIPE, stderr=PIPE)
            output, err = process.communicate()
        else:
            chdir(repo_path)
            process = Popen(['git', 'pull'], stdout=PIPE, stderr=PIPE)
            output, err = process.communicate()
        if output or err:
            error_log.write("\n" + datetime.now().strftime('%Y-%m-%d %H:%M') + " -- " + str(r) + "\n")
            error_log.write(output)
            error_log.write(err)
except GitHubError as error:
    print("GitHub Error:" + str(error))
except OSError as error:
    print("OSError:" + str(error))