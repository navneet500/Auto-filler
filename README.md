# Filler - Automatic Web Form Filler <br/>

## Working Video <br/>

https://user-images.githubusercontent.com/74672126/182907543-3a5f37b5-e9fd-4e3f-b2c7-c6ca2926d189.mp4

>* A Software which fills the respective fields of the form **automatically** when the **URL** of the form is provided. <br/>
>* User has to add the details only once after that every time corresponding fields will get filled up automatically. And, the user can edit them afterwards. <br/>
>* Technologies used to built this software are: **Python, Selenium, MySQL**. <br/>
>* The form gets filled on Microsoft Edge with the help of **Edge Driver**. <br/>

## How to Run? <br/>

>* Install Python, SQL, Edge Driver, and XAMPP in your PC. <br/>
>* Add the path of the edge driver in environment variables and also change it in your python file as shown below. <br/>
###### Path in Environment Variable Like this: <br/>
          C:\Users\krish\OneDrive\Documents\Desktop\Filler\edgedriver_win64 <br/>
###### Path in the Code Like this: <br/>
          C:\\Users\\krish\\OneDrive\\Documents\\Desktop\\formfiller\\edgedriver_win64\\msedgedriver.exe <br/>
<img width="664" alt="image" src="https://user-images.githubusercontent.com/74672126/182042359-d2b34f49-2382-47d2-a2e6-fe8fa802c287.png">
<br/>

>* Look msedgedriver.exe added in the path of the code. <br/>
>* Create a database named **formfiller** in XAMPP. <br/>
>* Create a table in formfiller having necessary fields as required and do the changes in the code as needed in SQL Query only. <br/>
>* Install Selenium and MySQL connector in python using **pip** commands. <br/>

###### To install Selenium: <br/>
          pip install selenium <br/>
          
###### To install MySQL Connector: <br/>
          python -m pip install mysql-connector-python <br/>

>* Run the Python code. <br/>

