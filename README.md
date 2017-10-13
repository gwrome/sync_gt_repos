sync_gt_repos
=============
Script to automatically sync all a user's github repositories to a local machine. Can be run by hand or automated as a cron job or the like in order to keep a current local copy of everything pushed to GT's GitHub Enterprise server.

Setup
-----
* Clone the repo to your local machine
* Install github3.py library (pip install -r requirements.txt)
* Create a personal access token in GitHub's [Settings | Personal Access Tokens](https://github.gatech.edu/settings/tokens) menu
* Copy the token to your computer (by default in ~/.gt_git_credentials)

Usage
-----
* Run sync_repos.py
