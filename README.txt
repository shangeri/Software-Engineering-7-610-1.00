1. How to run the applications

To parse the file from IFTTT
Set up Python as an environment variable in your computers settings (for Windows under “system”)
Go to your console
Type cd and the path to the folder where the file is stored (you can copy/paste the path or use tabulator if you know where it is)
If in the folder you  type the application name (parse_file.py), space, and then the name of the .csv file you want to convert 
(if the .csv file name contains spaces itself add the file name in quotation marks) a converted file will be generated in the same folder 
The old file will still exist.
If you haven’t set up Python as an environment variable, use your terminal to navigate to the folder where Python is installed. 
Then type python.exe <path to the program> <path to the .csv file you want to convert> 
(again use quotation marks if the .csv file name contains spaces itself)

To display the graph:
Again go to your console
Type pip install matplotlib
Type pip install numpy
If any error occurs, most likely the issue is that a package is not installed. 
Try pip install <package name>
Type python app.py
Type python app.py
-> Graph should appear

2. Difficulties

I.	File parsing
In the sample csv file we used to get an impression about what the final file from the IFTTT app would look like,  
the column separator wasn’t unique and some lines were corrupted. 
Regular expressions helped to identify the columns if no space was used as a separator but if the line was broken even this turned out to 
be too difficult. Especially in a form that allows to parse not just the specific sample file. 
To convert the date format could be done relatively straightforwardly. 
Since we did not know "whether" oder "that" the final file would look totally different, a lot of time was spent trying to find a way to 
recover the columns in the corrupted csv file with inconsistent separators and randomly split lines.
One benefit of the situation was, however, that with all the previous experience gained while working on the corrupted file it was pretty 
easy to write an application that deletes retweets, counts the number of unique tweets per day and adjusts the date to the standard used 
by Yahoo Finance in the clean file we finally got via IFTTT. Retweets are now identified by the RT prefix in the second column 
and the tweet is not counted. Skipping to the fourth column is followed by an automatic adjustment of the date and a check if the day 
is a weekday. If not, the tweet is not counted because the stock exchanges are closed in the weekend therefore we don't have any market data.
Unfortunately holidays and other trading free days have to be adjusted manually.  
Output starts with the latest date,  like the Yahoo Finance data, and inverse to the dates of input file with the Twitter data.

II.	2. Displaying the graph
The initial stages of setting up the programs to use Python and build an application were pretty confusing. There were so many ways to build a web application and display a graph in Python.
The graph was initially supposed to be displayed on a localhost HTML webpage with interactive labels and scales, but since 2 graphs have to be overlapped, matplotlib had to be used instead. This makes the UI not as interactive as it was planned to be. Matplotlib.pyplot is a Python library used to display graphs. It was a lot easier to code using matplotlib. However, given the short timeframe of this project, it was difficult to beautify the graph and make it more appealing.

3. Conclusion
This project is clearly a test project to learn basics in Python coding and get used to Git as the preferred working environment 
for software engineering projects. But with more time and an advanced understanding of Python and Git the project could be extended 
to produce some reliable scientific results by running different regression models. 
Regression models based on time series data are especially susceptible to the condition that residuals are independent. 
Key independent variables that have not been included in the model are likely to be related to time and the omission of one or more of 
these independent variables will tend to yield residuals that are also related to time. 
Therefore besides tests for normality and factor analysis a Durbin-Watson test must be conducted to identify autocorrelation in time series. 
A test for our data in Wolfram Mathematica resulted in a very low d statistic of around 0.15.
For a two-tail-test at the 0.05 level with n=17 observations and k=1 independent variables in the regression equation, the calculated value lies
well below the range of 1.13-1.38, implicating strong positive autocorrelation. 
With a bigger amount of data this test would have to be carefully replicated.

As far as the results of our visualization approach are concerned, it is easy to see that the amount of tweets and the trading volume 
for the Tesla stock show no correlation over the observed time span. 
(As a quick reference look up the results in the final_results.png stored in the Data Files folder of this repository)
But of course this is not enough to reject our hypothesis that the amount of tweets about a stock and its trading volume could be correlated. 
Researchers at the Norwegian Central Bank recently found a close correlation between news and economic developments. 
 
https://www.bloomberg.com/news/articles/2017-01-16/big-data-experiment-tests-central-banking-assumptions-in-norway 

The testing of a similar hypothesis with the help of big data amounts, extended to non-newspaper-related information like social media contents, 
could become a field of bigger interest in the near future, especially for researchers trying to forecast the economy and financial markets.
If the actual project is to be extended for example as a master thesis, data regarding tweets on Twitter should be collected directly via 
the Twitter API. The API just allows to collect data published over the 7 preceding days, but if a data crawler (PHP could be used here) was 
already written, the data could be collected on a regular basis just as with the IFTTT app. 
Also the data format should, for example, be in JSON to make the processing of the files easier and more flexible. 
Besides the steep learning curve in introductory Python, one of the main outcomes of the project was that Excel/csv is the wrong format for 
such a project. 
Also the benefits of Git became clearer and clearer while working with it. The hundreds of slightly differing versions of a file
each with its own slightly differing name, will most definitely be a thing of the past now that Git has been introduced to the authors. 
Still a lot more routine is needed especially to be aware of the impact only locally made Git commands can have once they are pushed online.


