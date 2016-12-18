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
