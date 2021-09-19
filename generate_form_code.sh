#!/bin/bash

app_name=$1
form_name=$2

ROOT_PATH=`pwd`
APP_PATH="$ROOT_PATH/$1"
FORMS_PATH="$APP_PATH/forms/uis"
PYTHON_FORMS_PATH="$APP_PATH/src/delegates"

python_form_name=$form_name
python_form_name=${python_form_name/".ui"/".py"}
form_path="$FORMS_PATH/$form_name"

python_form_path="$PYTHON_FORMS_PATH/$python_form_name"
pyuic5 $form_path -o $python_form_path
