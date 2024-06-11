#!/bin/sh

# Build the project
hugo -t "hugo-theme-learn"

# Go To Public folder
cd public

# Add changes to git.
git add .

# Commit changes.
msg="rebuilding site $(date)"
if [ -n "$*" ]; then
    msg="$*"
fi
git commit -m "$msg"

# Push source and build repos.
git push origin gh-pages

# Come Back up to the Project Root
cd ..
