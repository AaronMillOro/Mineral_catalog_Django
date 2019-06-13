# Mineral catalog
This project is a website that displays information about various minerals (AKA rocks). The home page of the site contains a list of all of the minerals in a database (JSON file). Clicking on a mineral’s name opens a page that displays information about the mineral.
The  **provided data** includes:

* A [JSON file](https://github.com/AaronMillOro/Mineral_catalog_Django/blob/master/mineral_catalog/minerals/resources/minerals.json) containing the information of each rock
* HTML examples of the expected result
* The [figures](https://github.com/AaronMillOro/Mineral_catalog_Django/tree/master/mineral_catalog/minerals/statics/img) for each mineral
* [CSS file](https://github.com/AaronMillOro/Mineral_catalog_Django/tree/master/mineral_catalog/static/css) containing the pages style
## Project details

* The minerals data is stored in a database using **SQLite**. A [script](https://github.com/AaronMillOro/Mineral_catalog_Django/blob/master/mineral_catalog/minerals/management/commands/input_data.py) creates the instance for each mineral from the provided **JSON** file. Each mineral contains some of the following information:

	* name
	* image filename
	* image caption
	* category
	* formula
	* strunz classification (method of categorizing minerals based on their chemical composition)
	* color
	* crystal system
	* unit cell
	* crystal symmetry
	* cleavage
	* mohs scale hardness
	* luster
	* streak
	* diaphaneity
	* optical properties
	* refractive index
	* crystal habit
	* specific gravity
	* group
	
* There is a layout template for the app.
* Additional **CSS** styles were added in th file [mineral.css](https://github.com/AaronMillOro/Mineral_catalog_Django/blob/master/mineral_catalog/static/css/mineral.css)
* The app contains a template and view to show the names of **all the minerals**: **/index.html**.

* There is a details template/view. The latter displays the details of a selected mineral as showed below:
![Details display](https://github.com/AaronMillOro/Mineral_catalog_Django/blob/master/provided_data/detail-preview.png) 

* The name of each attribute in the details template is showed in **title case** by using a template filter added to the code.

* Unit tests were performed to test that each view is displaying the correct information ( >50% [coverage](https://github.com/AaronMillOro/Mineral_catalog_Django/blob/master/mineral_catalog/htmlcov/index.html) ).

* The templates match the style provided in the [example files](https://github.com/AaronMillOro/Mineral_catalog_Django/tree/master/provided_data/example/).

* The most common features (**name, group, category, formula**) were estimated, and displayed first in **mineral_details** page, from the following constructed function:

> python3 manage.py statistics_data

![Figure display](https://github.com/AaronMillOro/Mineral_catalog_Django/blob/master/mineral_catalog/minerals/resources/data.png)

## Test the application in terminal

1. Set the repertory **mineral_catalog/**, install and run 'pipenv' 

		1 pipenv install
		2 pipenv shell

2. Download the corresponding dependencies in the virtual environment 

		3 pip install -r requirements.txt
		4 pipenv graph

3. In the root directory (Mineral_Catalog_Django/mineral_catalog/) run the application
		
		5 python3 manage.py runserver 0.0.0.0:5000

4. Open your favorite web browser and type

		http://localhost:5000/index

Enjoy! :shipit: