# FINAL-CRICKET-API-PROJECT


![image](https://user-images.githubusercontent.com/38343820/117118946-0a61dd80-adaf-11eb-877c-691c52a1393e.png)


### THIS PROJECT IS RESPONSIBLE FOR SCRAPPING CRICKET DATA AND THEN BUILDING AN API THAT LETS USERS SOLVE SOME ANALYTICAL QUERIES PERTAINING TO THE GIVEN SCRAPPED DATA. THE GIVEN TASK IS ACCOMPLISHED IN TWO PARTS AND THE FILES FOR THESE TWO PARTS HAVE BEEN UPLOADED SEPERATELY.THROUGH THIS PARTICULAR DOCUMENTATION, WE WILL TALK ABOUT THE METHODOLOGY AND DIFFICULTIES THAT CAME ACROSS WHILE MAKING THE PROJECT TO COME INTO THE PICTURE.


# INTRODUCTION:

THE PROJECT IS DONE IN TWO PARTS. 

## WEB SCRAPPING:

THE FIRST PART INVOLVES SCRAPPING THE DATA FROM THE GIVEN WEBSITE:

### SOURCE:

[WEBSITE USED FOR SCRAPPING THE DATA][https://www.espncricinfo.com/].

THE WEBSITE INCLUDES ALL THE STATS AVAILABLE ABOU CRICKET. IN THIS PROJECT, WE WILL BE LOOKING AT CRICKET PLAYER'S RECORDS OF ALL POTENTIAL COUNTRIES. THE WEBSITE CONTAINS DATA OF THE FOLLOWING COUNTRIES:

- AFGHANISTAN
- AUSTRALIA
- BANGLADESH
- ENGLAND
- ICC WORLD XI
- INDIA
- IRELAND
- NEW ZEALAND
- PAKISTAN
- SOUTH AFRICA
- SRI LANKA
- WEST INDIES
- ZIMBABWE

### AUTHENCITY OF THE DATA:
THE DATA IS COLLECTED BY THE OFFICIAL BODY OF THE CRICKET ICC WORLD CRICKET. SO, THE DATA COLLECTED IS ACCURATE AND AUTHENTIC.

### SOME INFORMATION ABOUT THE DATA COLLECTED:

THE DATA IS COLLECTED FOR ALL PLAYERS OF ALL COUNTRIES MENTIONED ABOVE WHO ARE BATSMAN AND BOWLERS ALIKE IN ALL THREE MAIN FORMATS OF THE CRICKET. THE MAIN IDEOLOGY BEHIND THE SCRAPPING OF THE DATA IS DISCUSSED BELOW IN THE FOLLWING STEPS:

- The website contains all stats that are available. Under the stats data, open all records to fetch data under records by teams.

![image](https://user-images.githubusercontent.com/38343820/117127825-3c2c7180-adba-11eb-81e0-bda1bcbacb68.png)

- Now, we can access records of all countries indivisually

- We can see on the left side, we have batting and bowling records for the indivisual country.

![image](https://user-images.githubusercontent.com/38343820/117127599-e8ba2380-adb9-11eb-8389-f92c32d03bfd.png)

- For the batting records, we will scrape most runs for all the given three formats.

- For the bowling records, we will scrape most wickets for all given formats.

### What can the scrapped data help us learn?

***Cricket is a sport that is held in following three formats namely – T20(Twenty 20), ODI (One Day International) and Test Matches. All these formats pose a very different challenge for the players to showcase their talents and abilities. Cricket being a very popular sport has encouraged countries to bring in their best talentedplayer. This particular fact is the very reason why scrapping the indivisual player’s record of every country makes a statement for a countries progress in this particular sport.***

## BUILDING AN API:

THE SECOND PART OF OUR PROJECT COVERS BUILDIND AN API THAT WILL LET US ANSWER SOME ANALYTICAL QUERIES. THE QUERIES ARE GIVEN IN THE TABLE BELOW AND THEN ARE ADDRESSED UPON SEPERATELY FOR MORE DETAILS.

### ERROR TESTING:

|  COLUMN NUMBER   |    URLS COVERING THE API     | ERROR TESTING    |  
|-----------------|-----------------| -----------------| 
|    1             | http://127.0.0.1:5000/getBestBatsman?key=123  |{ "code": 2, "msg": "Country not specified.", "req": "getBestBatsman" } |
|    2             | http://127.0.0.1:5000/getBestBatsman?key=345 |{ "code": 0, "msg": "Bad key given", "req": "getBestBatsman" } |
|    3             |http://127.0.0.1:5000/getBestBatsman?key=123&Country=AllCoun| { "code": 2, "msg": "Country not specified.", "req": "getBestBatsman" } |
|    4             |http://127.0.0.1:5000/getBestBatsman?key=123&Country=AllCountry&| { "code": 2, "msg": "Format not specified.", "req": "getBestBatsman" }|
|    5             |http://127.0.0.1:5000/getBestBatsman?key=123&Country=AllCountry&Formrat=TestMatches| { "code": 2, "msg": "Format not specified.", "req": "getBestBatsman" }|
|    6             | http://127.0.0.1:5000/getBestBatsman?key=123&Country=AllCountry&Format=TestMatches | { "code": 1, "msg": "Request:OK", "req": "getBestBatsman", "data":etc}|

***THIS TABLE SHOWS THE ERROR MESSAGES OF ALL THE ENDPOINTS WHICH IS ILLUSTRATED USING JUST ONE ENDPOINT.AS SHOWN BY THE TABLE, THE ERROR MESSAGES COVERED IN THE API ARE AS FOLLOWS:***

- INCORRECT KEY
- FIELD COUNTRY TYPE NOT SPECIFIED
- USED INCORRECT COUNTRY TYPE
- FIELD FORMAT NOT SPECIFIED
- USED INCORRECT FORMAT TYPE

### API ENDPOINTS THAT ARE COVERED AND WHAT ANALYTICAL QUERIES DO THEY SOLVE:

- http://127.0.0.1:5000/getBestBatsman?key=123&Country=AllCountry&Format=OdiMatches
- http://127.0.0.1:5000/getBestBatsman?key=123&Country=AllCountry&Format=TestMatches
- http://127.0.0.1:5000/getBestBatsman?key=123&Country=AllCountry&Format=Twenty20Matches

THIS URL RETURNS BEST BATSMAN AVAILABLE IN ALL THREE FORMAT WHEN ALL COUNTRIES ARE COMBINED TOGETHER. A BEST BATSMAN IS DEFINED BY THE NUMBER OF RUNS HE HAS SCORED IN HIS CAREER. THE QUERY WILL RETURN ALL THE AVAILABLE INFORMATION ABOUT THE PLAYERS AND THE PLAYERS WILL BE ARRANGED FROM TOP PLAYERS TO WORST PLAYER. HERE, THE QUERY ONLY RETURNS FEW PLAYERS ONLY DUE TO A VERY LARGE DATASET


- http://127.0.0.1:5000/getBestBowler?key=123&Country=AllCountry&Format=OdiMatches
- http://127.0.0.1:5000/getBestBowler?key=123&Country=AllCountry&Format=TestMatches
- http://127.0.0.1:5000/getBestBowler?key=123&Country=AllCountry&Format=Twenty20Matches

THIS URL RETURNS BEST BOWLERS AVAILABLE IN ALL THREE FORMAT WHEN ALL COUNTRIES ARE COMBINED TOGETHER. A BEST BOWLER IS DEFINED BY THE NUMBER OF WICKETS HE HAS TAKEN IN HIS CAREER. THE QUERY WILL RETURN ALL THE AVAILABLE INFORMATION ABOUT THE PLAYERS AND THE PLAYERS WILL BE ARRANGED FROM TOP PLAYERS TO WORST PLAYER. HERE, THE QUERY ONLY RETURNS FEW PLAYERS ONLY DUE TO A VERY LARGE DATASET


- http://127.0.0.1:5000/getHighestStrikeRate?key=123&Country=AllCountry&Format=OdiMatches
- http://127.0.0.1:5000/getHighestStrikeRate?key=123&Country=AllCountry&Format=TestMatches
- http://127.0.0.1:5000/getHighestStrikeRate?key=123&Country=AllCountry&Format=Twenty20Matches

THIS URL RETURNS BEST BATSMAN WITH HighestStrikeRate AVAILABLE IN ALL THREE FORMAT WHEN ALL COUNTRIES ARE COMBINED TOGETHER. A BEST BATSMAN IS DEFINED BY THE NUMBER OF RUNS HE HAS SCORED IN HIS CAREER. THE QUERY WILL RETURN ALL THE AVAILABLE INFORMATION ABOUT THE PLAYERS AND THE PLAYERS WILL BE ARRANGED FROM TOP PLAYERS TO WORST PLAYER. HERE, THE QUERY ONLY RETURNS FEW PLAYERS ONLY DUE TO A VERY LARGE DATASET


***HIGHEST STRIKE RATE BATSMAN IS REQUIRED FOR FINDING BATSMAN WHO CAN SCORE IN MIDDLE ORDER. BEST BATSMAN ARE USUALLY THE ONE THAT ARE POSTIONED AS EITHER CAPTAINS OR THEY COME WHEN A TEAM NEEEDS STABILITY. SOMETIMES, SPECIALLY IN TWENTY20 FORMAT, YOU NEED PLAYERS WHO WILL GET OUT EARLY BUT THEIR FORM ALLOWS THEM TO SCORE MOST RUNS IN AN OVER BY HITTING MORE SIXES AND FOURS. SUCH PLAYERS ARE ALSO GOODD BATSMAN BUT JUST USE DIFFERENT STRATEGY AND EQUALLY CRUCIAL TO THE TEAM***


- http://127.0.0.1:5000/getLowestEcomyRate?key=123&Country=AllCountry&Format=OdiMatches
- http://127.0.0.1:5000/getLowestEcomyRate?key=123&Country=AllCountry&Format=TestMatches
- http://127.0.0.1:5000/getgetLowestEcomyRate?key=123&Country=AllCountry&Format=Twenty20Matches

THIS URL RETURNS BEST BOWERS WITH getLowestEcomyRate AVAILABLE IN ALL THREE FORMAT WHEN ALL COUNTRIES ARE COMBINED TOGETHER. A BEST BOWLER IS DEFINED BY THE NUMBER OF WICKETS HE HAS  TAKEN IN HIS CAREER. THE QUERY WILL RETURN ALL THE AVAILABLE INFORMATION ABOUT THE PLAYERS AND THE PLAYERS WILL BE ARRANGED FROM TOP PLAYERS TO WORST PLAYER. HERE, THE QUERY ONLY RETURNS FEW PLAYERS ONLY DUE TO A VERY LARGE DATASET


***LOWEST ECONOMY RATE BOWLERS ARE REQUIRED FOR WHEN TEAM WANTS TO PLAY WITH A DEFENSE STRATEGY. BEST BOWLERS ARE WICKET TAKERS BUT THERE IS NEED FOR SOME BOWLERS WHO ARE SPECIALISED IN GIVING AWAY MINIMUM RUNS IN AN OVER. SOMETIMES, SPECIALLY IN TEST FORMAT, YOU NEED BOWLERS THOSE CAN GIVE AWAY LESS RUNS. SOMETIMES WHEN AGAINST TEAMS LIKE AUSTRALIA, ALL PLAYERS ARE EQUALLY GOOD BATSMAN. THEIR BOWLER ARE EVEN GOOD BATSMAN. SO, IN THAT CASE SOMETIMES YOU HOLD YOUR RUN RATE RATHER THATN TAKING AWAY WICKETS BY GIVING AWAY CHANCE OF HITTING MORE SIXES OR WIDES.SUCH PLAYERS ARE ALSO GOOD BOWLERS BUT JUST USE DIFFERENT STRATEGY AND EQUALLY CRUCIAL TO THE TEAM***


- http://127.0.0.1:5000/getgetBestCountriesBatting?key=123&Country=AllCountry&Format=OdiMatches
- http://127.0.0.1:5000/getgetBestCountriesBatting?key=123&Country=AllCountry&Format=TestMatches
- http://127.0.0.1:5000/getgetBestCountriesBatting?key=123&Country=AllCountry&Format=Twenty20Matches
- http://127.0.0.1:5000/getgetBestCountriesBowling?key=123&Country=AllCountry&Format=OdiMatches
- http://127.0.0.1:5000/getgetBestCountriesBowling?key=123&Country=AllCountry&Format=TestMatches
- http://127.0.0.1:5000/getgetBestCountriesBowling?key=123&Country=AllCountry&Format=Twenty20Matches



***THIS URL RETURNS BEST COUNTRIES IN BOWLING AND BATTING IN ALL FORMATS. THE VALUES ASSOCIATED WITH THEM SHOULD BE LARGE. THE LARGER THE VALUE THE MORE EFFICIENT THE COUNTRY IS.***


![image](https://user-images.githubusercontent.com/38343820/117136272-c62e0780-adc5-11eb-8818-72a67762804d.png)

***Data scraped for a batsman***

![image](https://user-images.githubusercontent.com/38343820/117136337-df36b880-adc5-11eb-937c-b603e0efc323.png)

***Data scraped for a bowler***

![image](https://user-images.githubusercontent.com/38343820/117136468-08574900-adc6-11eb-9685-d4b38eea537a.png)
***BEST COUNTRIES IN HAVING BEST BATSMAN***

ALL THESE SCRAPED DATA IS FOR A PARTICULAR FORMAT.THOUGH DATA COLLECTED FOR EACH PLAYER IS SIMILAR. THE PLAYERS WILL BE DIFFERENT FOR EACH FORMAT.

# METHODOLOGY USED WHILE CODING IN PYTHON:

## WEB SCRAPPING:

THE STEPS FOLLOWED FOR SCRAPPING FROM THE WEBSITE ARE AS FOLLOWS:

- IN THE VERY FIRST PLACE WE NEED TO SCRAPE ALL THE AVAILABLE DATA FOR ALL THE TEAMS. THE WEBSITE HAS A RECORD TABBLE FOR ALL THE TEAMS AND ON CLICKING ON THE PARTICULAR NAMES, THE SITE CORRESPONDS US TO THE RESPECTIVE PAGE. NOW, ALL WE NEED TO FIND IS THE ***RECORD TABLE IN VIEW SOURCE PAGE.*** ON ACCESSING THE VIEW SOURCE PAGE WE PRESS THE ***CTRL+F*** AND SEARCH FOR ***RECORDS BY TEAM***. ON ACCESSING THE RECORDS BY TEAM, WE FIND A ***TABLE HTML TAG*** IN ORDER TO FIND A TABLE. NOW IN ORDER TO SEPERATE THE TABLE FROM THE REST, WE USE THE ***split** functionality again and again in order to get what we want. Finally, after seperating the table, we get all the country names and with them we get the url of the next page through ***href*** attribute.
```html
<p class="statRecHdrG">Records by team</p>
              <div class="standingsGutter">
                <div class="standings-nav" style="text-align:left;"><a class="active" id="recteam_link" href="javascript:void(0);" onClick="changeLead('recteam','recteam_link'); return false;" title="Team">Team</a> | <a id="reccntry_link" class="inactive" href="javascript:void(0);" onClick="changeLead('reccntry','reccntry_link'); return false;" title="Host Country">Host Country</a></div>
              </div>


              <div id="recteam" style="display: block;">

                <ul class="Record" style="width: 220px;">

<li>

                  <a class="RecordLinks" href="/ci/engine/records/index.html?id=40;type=team"> Afghanistan</a></li>

<li>

                  <a class="RecordLinks" href="/ci/engine/records/index.html?id=2;type=team"> Australia</a></li>
```
```python
  url = 'https://stats.espncricinfo.com/ci/engine/records/index.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
}
ls2=[]
url2=[]
country_names=[]
r = requests.get(url,headers=headers)
t = r.text.split('<p class="statRecHdrG">Records by team</p>')[1]
split1=t.split('<ul class="Record" style="width: 220px;">')[1]
ls=split1.split('<a class="RecordLinks"')[1:]
for i in ls:
    split2=i.split('</li>')
    ls2.append(split2[0])
#print(ls2)
for i in ls2:
    split3=i.split('"> ')[0].split('href="')
    #print('https://stats.espncricinfo.com/'+split3[1])
    url2.append('https://stats.espncricinfo.com/'+split3[1])
    split4=i.split('"> ')[1].split('</a>')[0]  
    #print(split4)
    country_names.append(split4) ### accessed names of the countries who play cricket
#print(url2)
   ```

***Now, in this code we can see that using the requests package, we have sent a get request on the main websites url that will the whole html when we use r. text. by using split , we can remove whatever needs to be removed thereby accessing linescontaining the names and the url which we put in ls variable. on splittinf further, we get url and country names seperated in different lists. here, variables url2 and country_names contain the url for each country and country names respectively.***


- Now, that we have seperated list, we need to make a dictionary of the names so that when we access our data, we can always tell that which record belongs to which country. Now , this dictionary will contain all country names and then further information about the country's payers will be stored in this particular dictionary. In order to do that we use the given particular code:


```python
countries=dict.fromkeys(country_names) ## main dictionary of names of the countries
```


- Now, that we have list of country names***country_names*** and a dictionary called ***countries***, we can traverse and add to the dictionary easily. Now, our major goal is to scrap the batting and bowling records for all countries. Thus, we will tranverse through ***country_names*** and access the records by going to the url of each country seperately.Meaning ***the loop*** will help us to ***access each url*** present in the variable***url2**( as explianed in above point) one by one. thus helping us ***fetch batting and bowling records*** for ***each country***. We will ***access the pages*** as explained above using the ***request module*** and using the ***get method***


```python
for i in range(0, len(country_names)):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
}
    r = requests.get(url2[i],headers=headers)
    t = r.text.split('<p class="statRecHdr">Batting records</b><a name="batting"></p>')[1]
    t27=r. text.split('<p class="statRecHdr">Bowling records</b><a name="bowling"></p>')[1]
```


***NOTE: For the view source using ctrl+F search Batting and Bowling records one by one and then split to get the necessary data***


```python
split5=t.split('<p class="RecBulAro">High scores</p>')[0]
split35=t27.split(' <p class="RecBulAro">Most wickets</p>')[1]
```


***NOTE: For batting records, we access the high scores-Most runs and for bowling, we access the most wickets records. The reason is clearly stated in the introduction above.***


```python
    url3=[]
    url47=[]
    for j in range(0,3):
        url3.append('https://stats.espncricinfo.com/'+split7[j].split('<a class="RecordLinks" href="')[1].split('">')[0])
    for u in range(0,3):
        url47.append('https://stats.espncricinfo.com'+split37[u].split('<a class="RecordLinks" href="')[1].split('">')[0])
    #print(url47[1]) # Indexing to get test url of bowling records
```


***NOTE: We are accessing data for 3 formats.Now, variable url3 and url47 contains records of batting and bowling respectively for all 3 formats.Thus, by indexing, we can use data for any one format.***


- Now, for all countries, ***we add the batting and bowling records of each format***. For that, we first ***add batting and bowling record's dictionary to the indivisula countries dictionary***. After that, we can ***add dictionaries of test, odi and twenty20 formats*** to ***each batting and bowlings dictionaries***. At last, ***we add players list which is a dictionary of every players and their record to each one one of these 3 format dictionaries***.


```python
   for d in range(0,len(country_names)):
        if(i==d):
            Records={}
            countries[country_names[i]]=Records
            Batting_Records={}
            Bowling_Records={}
            Records['Batting_Records']=Batting_Records
            Records['Bowling_Records']=Bowling_Records
```


Now, for different formats, we need to loop through the six urls that we produced above so as to add records seperately for each. The 6 urls are:
  
    - test_url which contains the urls of each country's batting records for test format 
    - odi_url which contains the urls of each country's batting records for odi format
    - twenty_url which contains the urls of each country's batting records for twenty20 format
    - twenty_url_bowling which contains the urls of each country's bowling records for twenty20 format
    - odi_url_bowling which contains the urls of each country's bowling records for Odi format
    - test_url_bowling which contains the urls of each country's bowling records for test format


***NOTE: Not in order, refer to code for proper order.***
 


```python
 for k in test_url:
                #print(k)
                headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
                }
                r2 = requests.get(k,headers=headers)
                t2 = r2.text.split('<caption>Most runs</caption>')[1]
                split8=t2.split('<tbody>')[1].split('</tbody>')[0]
                split9=split8.split('<td class="left"')
                #print(split9)
                Test_Matches2={}
                Batting_Records['Test_Matches']=Test_Matches2
                #print(split9[47])
                list10=[]
                Test_Matches2['players']=list10
                #print(countries)
                for t in range(1,len(split9)):
                    count2=0
                    if(t%2!=0):
                        player_test={}
                        player_test['NAME']=split9[t].split('<a href="')[1].split('" class="data-link">')[1].split('</a></td>')[0]
                        player_test['ABOUT_player']='https://stats.espncricinfo.com/'+split9[t].split('<a href="')[1].split('" class="data-link">')[0]
                        count2=count2+1
                        #print(player)
                        if count2==1:
                            list10.append(player_test)
                    else:
                        try:
                            player_test['PLAYING_SPAN']=(split9[t].split('"nowrap">')[1].split('</td>')[0])
                            player_test['MATCHES_PLAYED']=split9[t].split('"nowrap">')[2].split('</td>')[0]
                            player_test['INNING_BATTED']=split9[t].split('"nowrap">')[3].split('</td>')[0]
                            player_test['NO_OUT']=split9[t].split('"nowrap">')[4].split('</td>')[0]
                            player_test['RUNS_SCORED']=split9[t].split('"nowrap">')[5].split('</td>')[0].split('</b>')[0].split('<b>')[1]
                            player_test['HIGHEST_INNING_SCORED']=split9[t].split('"nowrap">')[6].split('</td>')[0]
                            player_test['BATTING_AVERAGE']=split9[t].split('"nowrap">')[7].split('</td>')[0]
                            player_test['BALLS_FACED']=split9[t].split('"nowrap">')[8].split('</td>')[0]
                            player_test['STRIKE_RATE']=split9[t].split('"nowrap">')[9].split('</td>')[0]
                            player_test['1OOs_SCORED']=split9[t].split('"nowrap">')[10].split('</td>')[0]
                            player_test['5Os_SCORED']=split9[t].split('"nowrap">')[11].split('</td>')[0]
                            player_test['DUCKS_SCORED']=split9[t].split('"nowrap">')[12].split('</td>')[0]
                            player_test['BOUNDARY_FOURS']=split9[t].split('"nowrap">')[13].split('</td>')[0]
                            player_test['BOUNDARY_SIXES']=split9[t].split('"nowrap">')[14].split('</td>')[0]
                        except IndexError:
                            player_test['PLAYING_SPAN']=(split9[t].split('"nowrap">')[1].split('</td>')[0])
                            player_test['MATCHES_PLAYED']=split9[t].split('"nowrap">')[2].split('</td>')[0]
                            player_test['INNING_BATTED']=split9[t].split('"nowrap">')[3].split('</td>')[0]
                            player_test['NO_OUT']=split9[t].split('"nowrap">')[4].split('</td>')[0]
                            player_test['RUNS_SCORED']=split9[t].split('"nowrap">')[5].split('</td>')[0].split('</b>')[0].split('<b>')[1]
                            player_test['HIGHEST_INNING_SCORED']=split9[t].split('"nowrap">')[6].split('</td>')[0]
                            player_test['BATTING_AVERAGE']=split9[t].split('"nowrap">')[7].split('</td>')[0]
                            player_test['1OOs_SCORED']=split9[t].split('"nowrap">')[8].split('</td>')[0]
                            player_test['5Os_SCORED']=split9[t].split('"nowrap">')[9].split('</td>')[0]
                            player_test['DUCKS SCORED']=split9[t].split('"nowrap">')[10].split('</td>')[0]
                            count2=count2+1
                            if count2==1:
                                list10.append(player_test)
 ```


***Note: REST 5 URLS ARE DONE THE SAME. INTERESTING POINT TO NOTE HERE IS THAT EXCEPTION HANDLING IS USED BECAUSE EVERY COUNTRY HAS ITS OWN DIFFERENT TABLES. SOME COUNTRIES LACK SOME OF THE ABOVE USED VARIABLES AND SOME HAVE MISSING OR NO VALUES AT ALL***
 


- NOW, WE HAVE ALL THE DATA SCRAPED SO NOW WILL PUT ALL THE CONTENT INTO A JASON FILE.



```python
with open("cricketdata.json", "w") as outfile:
        print("Loding data into file")
        json.dump(countries, outfile)
print("Done!!! you got the file")
```
![image](https://user-images.githubusercontent.com/38343820/117157217-08fada00-addc-11eb-8414-547d2a6fd44d.png)

***on running the scraping code***

![image](https://user-images.githubusercontent.com/38343820/117158039-b4a42a00-addc-11eb-935c-9943e6cf846a.png)


***finding your jason file***


