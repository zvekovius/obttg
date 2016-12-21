# obttg
My following through obeying the testing goat http://www.obeythetestinggoat.com/

Provisioning a new site
=======================

##Required packages:
	*nginx
	*Python 3
	*git
	*pip
	*virtualenv
	*gunicorn

## On ubuntu
	sudo apt-get install nginx git python3 python3-pip
	sudo pip3 install virtualenv

##Nginx Virtual Host Config
	*see site-config template
	*replace USER and SITENAME with your linux user and name of site. 

##Systemd Service
	*See service-template
	*replace USER and SITENAMe with user and name of site.

##Folder structure:
Assume we have a non-root user at /home/username

/home/username
|____sites
	|____SITENAME
		|--database
		|--source
		|--static
		|--virtualenv

## General Django / Fab Things
==============================

# To run unit tests:
python3 manage.py tests lists

# To run functional tests:
python3 manage.py functional_tests --liveserver=serverurl.server.com
~or~
python3 manage.py functional_tests
^ Use a local server instead of staing server. 

#Deploying
Under deploy_tools there is a fab file. Run
fab deploy:host=user@host
-i can be passed if you need to give it a private key. Should default if you have your ssh user setup for remote host.
That takes care of everything except:
--> web server config (sites-available & sites-enabled)
--> service configuration for gunicorn. 
