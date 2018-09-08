# Item Catalog

_The Item Catalog web application provides a list of items within a variety of categories and integrate third party user registration and authentication. Authenticated users have the ability to post, edit, and delete their own items._


## Demo

_For the live version of this APP click [here](https://itemcatalog.wo984c.net)._


## Frameworks

* _Bootstrap_
* _jQuery_
* _Flask_
* _SQLAlchemy_


## Getting Started

* _Install [VirtualBox](https://www.virtualbox.org/wiki/Downloads)_
* _Install [Vagrant](https://www.vagrantup.com/downloads.html)_
* _Clone the Udacity's VM repo_
    ``` sh
    # git clone https://github.com/udacity/fullstack-nanodegree-vm 
    ```
* _Prepare and Launch the Vagrant VM from terminal_
    ``` sh
    # cd fullstack-nanodegree-vm/vagrant
    # sudo vagrant up
    # sudo vagrant ssh
    ```
* _Clone the item catalog repo into /vagrant_
    ``` sh
    # cd /vagrant
    # git clone https://github.com/wo984c/itemCatalog.git
    ```

### Data Base Setup

_Change user to postgres, create the data base, and db user_

```
# sudo su - postgres
# cd /vagrant/itemCatalog
# psql
postgres=# \i dbinit.sql;
postgres=# \q;
postgres@vagrant:~$ exit
```

_Setup the db schema_ ``` # python create_db_schema.py ```


## How to run the Item Catalog APP

_To launch the application run_ ``` # python catalogo.py ```
_Go to http://localhost:5000/catalog/ to access the application on your web browser._


## JSON EndPoints

_In addition to the GUI, the following JSON Endpoins have been implemented:_ 

* _/catalog/json/ - full catalog with categories, items, and items' description_
* _/catalog/categories/json/ - all the catalog's categories_
* _/catalog/<category_name>/items/json/ - the items for a given category_
* _/catalog/<category_name>/<item_name>/json/ - information about an specific item._


## License

_Multi User Blog is released under the [MIT license](https://github.com/wo984c/itemCatalog/blob/master/LICENSE.txt)._


## References

* _https://www.virtualbox.org/wiki_
* _https://www.vagrantup.com/_
* _https://developers.facebook.com/_
* _https://developers.google.com/_
* _https://www.sqlalchemy.org/_
* _http://book.pythontips.com/en/latest/decorators.html_
