# Mineral catalog
This project is a website that displays information about various minerals (AKA rocks). The home page of the site contains a list of all of the minerals in a database (JSON file). Clicking on a mineral’s name opens a page that displays information about the mineral.
The  **provided data** includes:

* A [JSON file](https://github.com/AaronMillOro/Mineral_catalog_Django/blob/master/mineral_catalog/minerals/resources/minerals.json) containing the information of each rock
* HTML examples of the expected result
* The [figures](https://github.com/AaronMillOro/Mineral_catalog_Django/tree/master/mineral_catalog/minerals/statics/img) for each mineral
* [CSS file](https://github.com/AaronMillOro/Mineral_catalog_Django/tree/master/mineral_catalog/static/css) containing the pages style
## Project details

* The minerals data is stored in a database using **SQLite**. A [script](https://github.com/AaronMillOro/Mineral_catalog_Django/blob/master/mineral_catalog/minerals/management/commands/input_data.py) creates the instance for each mineral in from the provided **JSON** file. Each mineral contains some of the following information:

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
* The app contains a template and view to show the names of **all the minerals**: **/index.html**.

* There is a details template and view. The latter displays the details of a selected mineral as showed below:
![Details display](https://github.com/AaronMillOro/Mineral_catalog_Django/blob/master/provided_data/detail-preview.png=200x300) 

* The name of each attribute in the details template is showed in **title case** by using a template filter.

* Unit tests were performed to test that each view is displaying the correct information.

* The templates match the style used in the [example files](https://github.com/AaronMillOro/Mineral_catalog_Django/tree/master/provided_data/example/).

* The **top3** most common features were estimated from the constructed function:

> python3 manage.py statistics_data

![Figure display](https://github.com/AaronMillOro/Mineral_catalog_Django/blob/master/mineral_catalog/minerals/resources/data.png)