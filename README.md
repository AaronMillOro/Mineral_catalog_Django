# Mineral catalog
This project is a website that displays information about various minerals (AKA rocks). The home page of the site contains a list of all of the minerals in a database (JSON file). Clicking on a mineral’s name opens a page that displays information about the mineral.
The repertory **'provided_data'** contains:

* A JSON file containing the information of each rock
* HTML files as examples of the expected final output
* CSS file containing the pages style
## Project details

* The minerals data is stored in a database using **SQLite**. A script creates the instance for each mineral in from the provided **JSON** file. Each mineral contains the following information:

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
	
* There is a layout template for the app.
* The app contains a template and view to show the names of **all the minerals**.

* There is a details template and view. The latter displays the details of a selected mineral as showed below:
![Details display](https://github.com/AaronMillOro/Mineral_catalog_Django/blob/master/provided_data/detail-preview.png) 

* The name of each attribute in the details template is showed in **title case** by using a template filter.

* Unit tests were performed to test that each view is displaying the correct information.

* The templates match the style used in the [example files](https://github.com/AaronMillOro/Mineral_catalog_Django/tree/master/provided_data/example/).