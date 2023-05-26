# Copyright (c) 2023 kk
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

task default: %w[push]

task :push do
  sh 'black .'
  sh 'git add .'
  sh 'git pull'
  # sh 'git rebase'
  sh 'git commit -m "update"'
  sh 'git push'
end