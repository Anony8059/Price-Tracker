# Price-Tracker
Price-Tracker notifies you about the prices of your desired product being fell down by sending an email. Used web srcaping with the help of python programming to made this app.

### requests
requests library is used to access the particular web page after which we can extract the desired data from it.

### BeautifulSoup
BeautifulSoup is a library from bs4 which is used to extract individual item data from web page.

### Prettify()
The prettify() method will turn a Beautiful Soup parse tree into a nicely formatted Unicode string.

### Explanation
First we are requesting the desired page by requests.get() method. Inside check_price() function, we extract the individual item data from the webpage like in our case we are extracting price and title through their ids. 
Then we use conditional statement to check whether the prices have been fell down. If yes then send email.
Inside send_mail() function, first we are creating the connection with gmail by smtplib.SMTP() method. ehlo() method is used by email server to identify itself when connecting the another email server. starttls() method is used to encrpyt the connection. Finally we login to our accounts with the help of login() method and then sending the email to the destination specified under dest_mail variable.

### Final Output
![Screenshot from 2019-12-22 14-03-33](https://user-images.githubusercontent.com/59021952/71319441-831b0f00-24c4-11ea-905e-5bd56c4dcfb8.png)
![Screenshot from 2019-12-22 14-05-45](https://user-images.githubusercontent.com/59021952/71319442-83b3a580-24c4-11ea-96d0-da64629c7774.png)
