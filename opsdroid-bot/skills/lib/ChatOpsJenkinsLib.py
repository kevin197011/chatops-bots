# Copyright (c) 2023 kk
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import jenkins
import time

# pip install python-jenkins


class ChatOpsJenkinsLib:
    def __init__(self, username="bot", token="xxxxxxxxxxxxxxxxxxxxxxxx"):
        self.username = username
        self.token = token
        self.host = "http://jenkins.devops.io:8080"
        self.jenkins_instance = jenkins.Jenkins(
            url=self.host, username=self.username, password=self.token
        )

    def run_job(self, job_name, job_params):
        self.jenkins_instance.build_job(job_name, job_params)

    def get_job_lastBuild_id(self, job_name):
        return self.jenkins_instance.get_job_info(job_name)["lastBuild"]["number"]

    def get_job_status(self, job_name, last_build_id):
        val = None
        while True:
            print("checking job ...")
            build_info = self.jenkins_instance.get_build_info(job_name, last_build_id)
            if build_info["result"] != None:
                val = build_info["result"]
                break
            time.sleep(2)
        return val
