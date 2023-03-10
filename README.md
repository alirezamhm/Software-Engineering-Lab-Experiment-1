# Software-Engineering-Lab-Experiment-1
---
## Report
This is a script to download all video files in a given web page.

The project is sepereated into three branches. Main branch is where all offical releases will be kept. Dev branch is for development and all new features will be experimented and added. If these new features were functional, dev branch will be merged with the main branch to create a new release. Finally, bugfix branch is for resolving any existing bugs in the project.

The main branch is protected so that a merge can only happen with opening a new pull request.

Two conflicts happened while merging the bugfix branch with the dev branch. These conflicts were handled and pull requests were approved.


---
## Questions 

1. The `.git` folder is a directory that contains all the information about git project, such as commits or log history. It can be created by using `git init` command.

2. An atomic commit is a commit that only contains one logical change. It can’t be split into smaller parts. An atomic pull request is a pull request that only contains one atomic commit.

3. `fetch` downloads changes from a remote repository to local branch. `merge` combines two branches together by creating new commits. `pull` is a combination of `fetch` and `merge`. It fetches changes and then merges them into the current branch.

4. `reset` moves the branch pointer to a different commit and optionally changes the staging area or the working directory. `revert` creates a new commit that undoes the changes of a previous commit. `rebase` moves a series of commits to a new base commit. `restore` restores specific files or paths from another commit or stage.

5. Stage is used to describe the process of adding files or changes to a staging area. A staging area is a place where files and cahnges can be prepared before committing.
`stash` command saves local changes away and reverts the working directory to match the HEAD commit. It can be used when you want to switch context and work on something else without committing your changes. You can use `stash apply` or `stash pop` to re-apply your stashed changes later.

1. A snapshot is a term used to describe the state of the project at a certain point in time. Git takes snapshots of the entire project on every commit. `snapshot` can be used to create or update another branch with a snapshot of a directory.