Provisioning a new site
=====

## Required packages

* nginx
* python 3.6
* anaconda (deviates from the book, which uses virtualenv)
* pip
* git

Install in Conda environment tdd-book

## NginxVirtual Host Config
* See nginx.template.conf
* Replace DOMAIN by e.g. staging.domain.com
## Systemd service
* see gunicorn-systemd.template.service
* replace DOMAIN by e.g. staging.domain.com

## folder structure

Assume we are onaccount /home/username 	 	

Within that we have 
/home/username/sites/DOMAIN1
.
├── functional_tests
│   └── __pycache__
├── lists
│   ├── migrations
│   │   └── __pycache__
│   ├── __pycache__
│   ├── static
│   │   ├── bootstrap
│   │   │   ├── css
│   │   │   ├── fonts
│   │   │   └── js
│   │   └── static
│   │       ├── admin
│   │       │   ├── css
│   │       │   ├── fonts
│   │       │   ├── img
│   │       │   │   └── gis
│   │       │   └── js
│   │       │       ├── admin
│   │       │       └── vendor
│   │       │           ├── jquery
│   │       │           └── xregexp
│   │       └── bootstrap
│   │           ├── css
│   │           ├── fonts
│   │           └── js
│   └── templates
├── static
│   ├── admin
│   │   ├── css
│   │   ├── fonts
│   │   ├── img
│   │   │   └── gis
│   │   └── js
│   │       ├── admin
│   │       └── vendor
│   │           ├── jquery
│   │           └── xregexp
│   ├── bootstrap
│   │   ├── css
│   │   ├── fonts
│   │   └── js
│   └── static
│       ├── admin
│       │   ├── css
│       │   ├── fonts
│       │   ├── img
│       │   │   └── gis
│       │   └── js
│       │       ├── admin
│       │       └── vendor
│       │           ├── jquery
│       │           └── xregexp
│       └── bootstrap
│           ├── css
│           ├── fonts
│           └── js
├── superlists
│   └── __pycache__
└── testdb
    └── migrations
