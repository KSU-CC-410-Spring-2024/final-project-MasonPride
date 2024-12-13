This is my final project for CC410 Advanced Programming!

[Documentation](https://ksu-cc-410-spring-2024.github.io/final-project-MasonPride/)

This project is meant to serve as a simple data infrastructure, as well as
a web interface end user experience. The two main components of this project are the use of my data
and web packages.

The data package contains classes that create different vehicle types, as well
as a lot that represents the vehicles currently on our lot.

The web package contains web routing as well as web pages with
functionality. These include a homepage, browse page (browse vehicles on the lot), sell page (list your car 
using year, make, model, mileage, and asking price), and market value page (uses api to market value of car).

Here is a link to my [presentation](https://www.youtube.com/watch?v=StsP1NC3mn4)!

To use:
- Add 'creds.py' file to root of project
- Register for an API-Key from [MarketCheck](https://www.marketcheck.com/apis/?utm_source=google&utm_medium=paid&utm_campaign=API&utm_term=marketcheck%20api&utm_content=1708073986958579827&gad_source=1&gclid=Cj0KCQiAsOq6BhDuARIsAGQ4-ziyXDBJki3XPU5HD-EYnwqeUzbgUtNzmsRIcE1lXYypY16VQSItewUaAmtQEALw_wcB)
- Copy your key into 'creds.py' as 
    -  api_key = "{API-Key}"
- Run "pip3 install tox"
- Run "python3 -m flask run" to run web app
