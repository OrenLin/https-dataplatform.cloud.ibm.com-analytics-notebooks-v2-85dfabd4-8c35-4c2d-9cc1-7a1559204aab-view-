
!pip install yfinance
#!pip install pandas
#!pip install requests
!pip install bs4
#!pip install plotly

def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
    stock_data_specific = stock_data[stock_data.Date <= '2021--06-14']
    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data_specific.Date, infer_datetime_format=True), y=stock_data_specific.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific.Date, infer_datetime_format=True), y=revenue_data_specific.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=900,
    title=stock,
    xaxis_rangeslider_visible=True)
    fig.show()

tsla = yf.Ticker("TSLA")
 
tesla_data = tsla.history(period="max")

tesla_data.reset_index(inplace=True)
tesla_data.head()
url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"
html_data  = requests.get(url).text


soup = BeautifulSoup(html_data,"html5lib")



tables = soup.find_all('table')
tables[1]
tesla_revenue = pd.DataFrame(columns=["Date", "Revenue"])

for row in tables[1].tbody.find_all("tr"):
    col = row.find_all("td")
    if (col != []):
        date = col[0].text
        revenue = col[1].text
        tesla_revenue = tesla_revenue.append({"Date":date, "Revenue":revenue}, ignore_index=True)

tesla_revenue

Execute the following line to remove the comma and dollar sign from the Revenue column.

tesla_revenue["Revenue"] = tesla_revenue['Revenue'].str.replace(',|\$',"")
tesla_revenue
<ipython-input-38-6d89075fcbd5>:1: FutureWarning: The default value of regex will change from True to False in a future version.
  tesla_revenue["Revenue"] = tesla_revenue['Revenue'].str.replace(',|\$',"")
<ipython-input-38-6d89075fcbd5>:1: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame.
Try using .loc[row_indexer,col_indexer] = value instead

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  tesla_revenue["Revenue"] = tesla_revenue['Revenue'].str.replace(',|\$',"")
Date	Revenue
0	2021-06-30	11958
1	2021-03-31	10389
2	2020-12-31	10744
3	2020-09-30	8771
4	2020-06-30	6036
5	2020-03-31	5985
6	2019-12-31	7384
7	2019-09-30	6303
8	2019-06-30	6350
9	2019-03-31	4541
10	2018-12-31	7226
11	2018-09-30	6824
12	2018-06-30	4002
13	2018-03-31	3409
14	2017-12-31	3288
15	2017-09-30	2985
16	2017-06-30	2790
17	2017-03-31	2696
18	2016-12-31	2285
19	2016-09-30	2298
20	2016-06-30	1270
21	2016-03-31	1147
22	2015-12-31	1214
23	2015-09-30	937
24	2015-06-30	955
25	2015-03-31	940
26	2014-12-31	957
27	2014-09-30	852
28	2014-06-30	769
29	2014-03-31	621
30	2013-12-31	615
31	2013-09-30	431
32	2013-06-30	405
33	2013-03-31	562
34	2012-12-31	306
35	2012-09-30	50
36	2012-06-30	27
37	2012-03-31	30
38	2011-12-31	39
39	2011-09-30	58
40	2011-06-30	58
41	2011-03-31	49
42	2010-12-31	36
43	2010-09-30	31
44	2010-06-30	28
45	2010-03-31	21
47	2009-09-30	46
48	2009-06-30	27
Execute the following lines to remove an null or empty strings in the Revenue column.

tesla_revenue.dropna(inplace=True)

tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]
Display the last 5 row of the tesla_revenue dataframe using the tail function. Take a screenshot of the results.

tesla_revenue.tail()
Date	Revenue
43	2010-09-30	31
44	2010-06-30	28
45	2010-03-31	21
47	2009-09-30	46
48	2009-06-30	27
Question 3: Use yfinance to Extract Stock Data
Using the Ticker function enter the ticker symbol of the stock we want to extract data on to create a ticker object. The stock is GameStop and its ticker symbol is GME.

gme = yf.Ticker("GME")
Using the ticker object and the function history extract stock information and save it in a dataframe named gme_data. Set the period parameter to max so we get information for the maximum amount of time.

gme_data = gme.history(period="max")
Reset the index using the reset_index(inplace=True) function on the gme_data DataFrame and display the first five rows of the gme_data dataframe using the head function. Take a screenshot of the results and code from the beginning of Question 3 to the results below.

gme_data.reset_index(inplace=True)
gme_data.head()
level_0	index	Date	Open	High	Low	Close	Volume	Dividends	Stock Splits
0	0	0	2002-02-13	6.480513	6.773399	6.413183	6.766666	19054000	0.0	0.0
1	1	1	2002-02-14	6.850831	6.864296	6.682506	6.733003	2755400	0.0	0.0
2	2	2	2002-02-15	6.733001	6.749833	6.632006	6.699336	2097400	0.0	0.0
3	3	3	2002-02-19	6.665671	6.665671	6.312189	6.430017	1852600	0.0	0.0
4	4	4	2002-02-20	6.463681	6.648838	6.413183	6.648838	1723200	0.0	0.0
Question 4: Use Webscraping to Extract GME Revenue Data
Use the requests library to download the webpage https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue. Save the text of the response as a variable named html_data.

url = "https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue"
html_data  = requests.get(url).text
Parse the html data using beautiful_soup.

soup = BeautifulSoup(html_data, 'html5lib')
Using BeautifulSoup or the read_html function extract the table with GameStop Quarterly Revenue and store it into a dataframe named gme_revenue. The dataframe should have columns Date and Revenue. Make sure the comma and dollar sign is removed from the Revenue column using a method similar to what you did in Question 2.

Click here if you need help locating the table
tables = soup.find_all('table')
tables[1]
gme_revenue = pd.DataFrame(columns=["Date", "Revenue"])

for row in tables[1].tbody.find_all("tr"):
    col = row.find_all("td")
    if (col != []):
        date = col[0].text
        revenue = col[1].text
        gme_revenue = gme_revenue.append({"Date":date, "Revenue":revenue}, ignore_index=True)

gme_revenue["Revenue"] = gme_revenue['Revenue'].str.replace(',|\$',"")
gme_revenue.dropna(inplace=True)
gme_revenue = gme_revenue[gme_revenue['Revenue'] != ""]
gme_revenue
<ipython-input-35-029009e4005a>:12: FutureWarning: The default value of regex will change from True to False in a future version.
  gme_revenue["Revenue"] = gme_revenue['Revenue'].str.replace(',|\$',"")
Date	Revenue
0	2021-04-30	1277
1	2021-01-31	2122
2	2020-10-31	1005
3	2020-07-31	942
4	2020-04-30	1021
...	...	...
61	2006-01-31	1667
62	2005-10-31	534
63	2005-07-31	416
64	2005-04-30	475
65	2005-01-31	709
66 rows × 2 columns

Display the last five rows of the gme_revenue dataframe using the tail function. Take a screenshot of the results.

gme_revenue.tail()
Date	Revenue
61	2006-01-31	1667
62	2005-10-31	534
63	2005-07-31	416
64	2005-04-30	475
65	2005-01-31	709
Question 5: Plot Tesla Stock Graph
Use the make_graph function to graph the Tesla Stock Data, also provide a title for the graph. The structure to call the make_graph function is make_graph(tesla_data, tesla_revenue, 'Tesla'). Note the graph will only show data upto June 2021.

make_graph(tesla_data, tesla_revenue, 'Tesla')
Question 6: Plot GameStop Stock Graph
Use the make_graph function to graph the GameStop Stock Data, also provide a title for the graph. The structure to call the make_graph function is make_graph(gme_data, gme_revenue, 'GameStop'). Note the graph will only show data upto June 2021.

make_graph(gme_data, gme_revenue, 'GameStop')
About the Authors:
Joseph Santarcangelo has a PhD in Electrical Engineering, his research focused on using machine learning, signal processing, and computer vision to determine how videos impact human cognition. Joseph has been working for IBM since he completed his PhD.

Azim Hirjani

Change Log
| Date (YYYY-MM-DD) | Version | Changed By | Change Description | | ----------------- | ------- | ------------- | ------------------------- | | 2020-11-10 | 1.1 | Malika Singla | Deleted the Optional part | | 2020-08-27 | 1.0 | Malika Singla | Added lab to GitLab |

© IBM Corporation 2020. All rights reserved.
