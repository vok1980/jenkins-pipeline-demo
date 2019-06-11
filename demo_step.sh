git checkout $(git rev-list --topo-order HEAD..origin/master | tail -1)
git push -f origin HEAD:refs/heads/demo
git show HEAD
