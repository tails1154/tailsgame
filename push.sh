#!/bin/bash

read -p "Enter commit message: " answer
git init
git add .
git commit -m "$answer"
echo "Pushing to github!"
git push
echo "Done!"

