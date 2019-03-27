# **Currency Conversion API**

This application has been developed to receive the exchange rates valid for a maximum of ten days from the last year.
- The application provides a dynamically generated REST API.
- The application makes use of an external REST service to complement its functionality.
- The application uses a cloud database for accessing persistent information.
- Implemented user accounts and access management.
 
## **Installation Prerequisites**

1. Installing Python:
```
sudo apt-get install python3
```
2. Create our virtual environment with your preferred name (I chose flask_venv):
```
python3 -m venv flask_venv
```
3. Activate virtual environment:
```
source flask_venv/bin/activate
```
4.Now, switch to your terminal. From your app directory (the same directory thathas your requirements.txt) run the following:
```
python -m pip install -U -r requirements.txt
```
## **Running the Application**

1. Run the conversion application:
```
python app.py
```
2. Open our browser and navigate to localhost:8080
3. Enter user name:cloudcomputing and password:ecs781
4. Access the page and enter information.
5. Currency:Euro(it just provides Euro for now)
6. Enter start date((yyyy-mm-dd) and end date((yyyy-mm-dd).

###### Note:
The year must be the last one year from today and must be a maximum of 10 days between the start and end dates.



