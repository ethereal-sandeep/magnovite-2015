#! /bin/env bash

if [ "$#" -lt 2 ]; then
    echo "Usage: <production|staging> <commit message> [--no-dist]"
    exit 1
fi

echo ">>>> Env: $1"
echo ">>>> Message: $2"


if echo $* | grep -e "--no-dist" -q
then
    echo ">>>> Skipping Dist step"
else
    git checkout "$1"
    gulp dist
    git add .
    git commit -m "$1: $2"
fi

if [ "$1" == "production" ]
then
    echo ">>>> pushing [production] -> heroku[master]"
    git push heroku production:master
    APP=magnovite
else
    echo ">>>> pushing [staging] -> staging[master]"
    git push staging staging:master
    APP=magnovite-staging
fi

echo ">>>> Migrationg heroku app $APP"
heroku run ./manage.py migrate --app="$APP"
