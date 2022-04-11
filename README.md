# minimal-python-server

## Installation

### Prerequisites

Ubuntu:

```bash
sudo apt-get install apache2
sudo apt-get install libapache2-mod-wsgi-py3
```

```bash
cd /var/www/html
sudo git clone https://github.com/shaunharker/minimalpythonserver
cd minimalpythonserver
sudo cp site.conf /etc/apache2/sites-available/site.conf
sudo a2dissite 000-default
sudo a2ensite site
```
