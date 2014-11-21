Provisioning a new site
=======================

## Required paackages:

* nginx
* Python
* Git
* pip
* virtualenv

eg, on Ubuntu:

	sudo apt-get install nginx git python python-pip
	sudo pip install virtualenv

## Nginx Virtual Host Config

* see nginx.template.conf
* replace SITENAME with, eg. staging.domain.com

## Upstart job

* see gunicorn-upstart.template.conf
* replace SITENAME with, eg. staging.domain.com

## Folder structure: 

/home/username
|__sites
   |__SITENAME
	|__database
	|__source
	|__static
	|__virtualenv 
