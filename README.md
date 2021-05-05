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
