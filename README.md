# minimal-python-server

## Installation

### Prerequisites

Here are roughly the instructions that worked for me on Ubuntu 20.04:

```bash
# Install prerequisites
sudo apt-get install apache2
sudo apt-get install libapache2-mod-wsgi-py3
sudo apt-get install python-dev-is-python3
sudo apt install certbot python3-certbot-apache
sudo pip install flask # some recommend virtualenv

# Download this repository
cd /var/www/html
sudo git clone https://github.com/shaunharker/minimalpythonserver
cd minimalpythonserver

# Fix the permissions so group is www-data with same
# privileges as user
bash ./permissions.sh

# Set up apache2
sudo ufw allow 'Apache Full'
sudo a2enmod ssl
sudo certbot --apache # and handle matters according to https://www.digitalocean.com/community/tutorials/how-to-secure-apache-with-let-s-encrypt-on-ubuntu-20-04
sudo a2enmod wsgi
sudo cp site.conf /etc/apache2/sites-available/site.conf
sudo emacs /etc/apache2/sites-available/site.conf # fix domain name by hand
sudo a2dissite 000-default
sudo a2ensite site
sudo systemctl restart apache2

# Restart apache2 web server
sudo systemctl restart apache2
```

## Acknowledgments

* <https://python.plainenglish.io/how-to-securely-deploy-flask-with-apache-in-a-linux-server-environment-7eacd4c69a73>
* <https://www.codementor.io/@abhishake/minimal-apache-configuration-for-deploying-a-flask-app-ubuntu-18-04-phu50a7ft>
* <https://flask.palletsprojects.com/en/2.1.x/quickstart/>
* <https://www.digitalocean.com/community/tutorials/how-to-secure-apache-with-let-s-encrypt-on-ubuntu-20-04>
* <https://www.digitalocean.com/community/tutorials/how-to-install-the-apache-web-server-on-ubuntu-20-04#step-5-%E2%80%94-setting-up-virtual-hosts-(recommended)>
