#!/usr/bin/env python
# coding: utf-8

# In[7]:


import requests
import json
import bs4
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
#print(country_names)
countries=dict.fromkeys(country_names) ## main dictionary of names of the countries
#print(countries)
for i in range(0, len(country_names)):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
}
    r = requests.get(url2[i],headers=headers)
    t = r.text.split('<p class="statRecHdr">Batting records</b><a name="batting"></p>')[1]
    t27=r. text.split('<p class="statRecHdr">Bowling records</b><a name="bowling"></p>')[1]
    #print(t27)
    #print(t)
    # countries[country_names[i]]= add value #### imp
    split5=t.split('<p class="RecBulAro">High scores</p>')[0]
    split35=t27.split(' <p class="RecBulAro">Most wickets</p>')[1]
    #print(split5)
    #print(split35)
    split6=split5.split('<ul class="Record">')
    split7=(split6[1].split(' <li>      ')[1].split('</a> |'))
    split36=split35.split('<ul class="Record">')
    split37=(split36[1].split(' <li>      ')[1].split('</a> |'))
    #print(split37)
    url3=[]
    url47=[]
    for j in range(0,3):
        url3.append('https://stats.espncricinfo.com/'+split7[j].split('<a class="RecordLinks" href="')[1].split('">')[0])
    for u in range(0,3):
        url47.append('https://stats.espncricinfo.com'+split37[u].split('<a class="RecordLinks" href="')[1].split('">')[0])
    #print(url47[1])
    test_url=[]
    test_url_bowling=[]
    test_url.append(url3[0])
    test_url_bowling.append(url47[0])
    twenty20_url=[]
    twenty20_url.append(url3[2])
    twenty20_url_bowling=[]
    twenty20_url_bowling.append(url47[2])
    odi_url_bowling=[]
    odi_url_bowling.append(url47[1])
    odi_url=[]
    odi_url.append(url3[1])
    #print(countries)
    #Player Country Span Mat Inns NO Runs HS Ave BF SR 100 50 0 4s 6s
    for d in range(0,len(country_names)):
        if(i==d):
            Records={}
            countries[country_names[i]]=Records
            Batting_Records={}
            Bowling_Records={}
            Records['Batting_Records']=Batting_Records
            Records['Bowling_Records']=Bowling_Records
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
            for y in twenty20_url:
                #print(y)
                headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
                }
                r9 = requests.get(y,headers=headers)
                t9 = r9.text.split('<caption>Most runs</caption>')[1]
                split18=t9.split('<tbody>')[1].split('</tbody>')[0]
                split19=split18.split('<td class="left"')
                #print(split9)
                Twenty20_Matches={}
                Batting_Records['Twenty20_Matches']=Twenty20_Matches
                #print(split9[47])
                list1=[]
                Twenty20_Matches['players']=list1
                for t in range(1,len(split19)):
                    count2=0
                    if(t%2!=0):
                        player={}
                        player['NAME']=split19[t].split('<a href="')[1].split('" class="data-link">')[1].split('</a></td>')[0]
                        player['ABOUT_player']='https://stats.espncricinfo.com/'+split19[t].split('<a href="')[1].split('" class="data-link">')[0]
                        count2=count2+1
                        #print(player)
                        if count2==1:
                            list1.append(player)
                    else:
                        player['PLAYING_SPAN']=(split19[t].split('"nowrap">')[1].split('</td>')[0])
                        player['MATCHES_PLAYED']=split19[t].split('"nowrap">')[2].split('</td>')[0]
                        player['INNING_BATTED']=split19[t].split('"nowrap">')[3].split('</td>')[0]
                        player['NO_OUT']=split19[t].split('"nowrap">')[4].split('</td>')[0]
                        player['RUNS_SCORED']=split19[t].split('"nowrap">')[5].split('</td>')[0].split('</b>')[0].split('<b>')[1]
                        player['HIGHEST_INNING_SCORED']=split19[t].split('"nowrap">')[6].split('</td>')[0]
                        player['BATTING_AVERAGE']=split19[t].split('"nowrap">')[7].split('</td>')[0]
                        player['BALLS_FACED']=split19[t].split('"nowrap">')[8].split('</td>')[0]
                        player['STRIKE_RATE']=split19[t].split('"nowrap">')[9].split('</td>')[0]
                        player['1OOs_SCORED']=split19[t].split('"nowrap">')[10].split('</td>')[0]
                        player['5Os_SCORED']=split19[t].split('"nowrap">')[11].split('</td>')[0]
                        player['DUCKS_SCORED']=split19[t].split('"nowrap">')[12].split('</td>')[0]
                        player['BOUNDARY_FOURS']=split19[t].split('"nowrap">')[13].split('</td>')[0]
                        player['BOUNDARY_SIXES']=split19[t].split('"nowrap">')[14].split('</td>')[0]
                        count2=count2+1
                        if count2==1:
                            list1.append(player)
            for p in odi_url:
                #print(p)
                headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
                }
                r13 = requests.get(p,headers=headers)
                t12 = r13.text.split('<caption>Most runs</caption>')[1]
                split28=t12.split('<tbody>')[1].split('</tbody>')[0]
                split29=split28.split('<td class="left"')
                #print(split9)
                Odi_Matches2={}
                Batting_Records['Odi_Matches']=Odi_Matches2
                #print(split9[47])
                list11=[]
                Odi_Matches2['players']=list11
                #print(countries)
                for t in range(1,len(split29)):
                    count2=0
                    if(t%2!=0):
                        player_odi={}
                        player_odi['NAME']=split29[t].split('<a href="')[1].split('" class="data-link">')[1].split('</a></td>')[0]
                        player_odi['ABOUT_player']='https://stats.espncricinfo.com/'+split29[t].split('<a href="')[1].split('" class="data-link">')[0]
                        count2=count2+1
                        #print(player)
                        if count2==1:
                            list11.append(player_odi)
                    else:
                        player_odi['PLAYING_SPAN']=(split29[t].split('"nowrap">')[1].split('</td>')[0])
                        player_odi['MATCHES_PLAYED']=split29[t].split('"nowrap">')[2].split('</td>')[0]
                        player_odi['INNING_BATTED']=split29[t].split('"nowrap">')[3].split('</td>')[0]
                        player_odi['NO_OUT']=split29[t].split('"nowrap">')[4].split('</td>')[0]
                        player_odi['RUNS_SCORED']=split29[t].split('"nowrap">')[5].split('</td>')[0].split('</b>')[0].split('<b>')[1]
                        player_odi['HIGHEST_INNING_SCORED']=split29[t].split('"nowrap">')[6].split('</td>')[0]
                        player_odi['BATTING_AVERAGE']=split29[t].split('"nowrap">')[7].split('</td>')[0]
                        player_odi['BALLS_FACED']=split29[t].split('"nowrap">')[8].split('</td>')[0]
                        player_odi['STRIKE_RATE']=split29[t].split('"nowrap">')[9].split('</td>')[0]
                        player_odi['1OOs_SCORED']=split29[t].split('"nowrap">')[10].split('</td>')[0]
                        player_odi['5Os_SCORED']=split29[t].split('"nowrap">')[11].split('</td>')[0]
                        player_odi['DUCKS_SCORED']=split29[t].split('"nowrap">')[12].split('</td>')[0]
                        try:
                            player_odi['BOUNDARY_FOURS']=split29[t].split('"nowrap">')[13].split('</td>')[0]
                            player_odi['BOUNDARY_SIXES']=split29[t].split('"nowrap">')[14].split('</td>')[0]
                        except IndexError:
                            count2=count2+1
                            if count2==1:
                                list11.append(player_odi)
            for x in test_url_bowling:
                #print(p)
                headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
                }
                r33 = requests.get(x,headers=headers)
                t32 = r33.text.split('<caption>Most wickets</caption>')[1]
                #print(t32)
                split58=t32.split('<tbody>')[1].split('</tbody>')[0]
                split59=split58.split('<td class="left"')
                #print(split59)
                test_Matches2_bowling={}
                Bowling_Records['test_Matches_bowling']=test_Matches2_bowling
                #print(split9[47])
                list51=[]
                test_Matches2_bowling['players']=list51
                for v in range(1,len(split59)):
                    count52=0
                    if(v%2!=0):
                        player_test_bowling={}
                        player_test_bowling['NAME']=split59[v].split('<a href="')[1].split('" class="data-link">')[1].split('</a></td>')[0]
                        player_test_bowling['ABOUT_player']='https://stats.espncricinfo.com'+split59[v].split('<a href="')[1].split('" class="data-link">')[0]
                        count52=count52+1
                        #print(player)
                        if count52==1:
                            list51.append(player_test_bowling)
                    else:
                        try:
                            player_test_bowling['PLAYING_SPAN']=split59[v].split('"nowrap">')[1].split('</td>')[0]
                            player_test_bowling['MATCHES PLAYED']=split59[v].split('"nowrap">')[2].split('</td>')[0]
                            player_test_bowling['INNING PLAYED']=split59[v].split('"nowrap">')[3].split('</td>')[0]
                            player_test_bowling['OVERS BOWLED']=split59[v].split('"nowrap">')[4].split('</td>')[0]
                            player_test_bowling['MAIDEN EARNED']=split59[v].split('"nowrap">')[5].split('</td>')[0]
                            try:
                                player_test_bowling['RUNS CONCEDED']=split59[v].split('"nowrap">')[6].split('</td>')[0].split('</b>')[0].split('<b>')[1]
                            except:
                                player_test_bowling['RUNS CONCEDED']=split59[v].split('"nowrap">')[6].split('</td>')[0]
                            
                            player_test_bowling['WICKETS TAKEN']=split59[v].split('"nowrap">')[7].split('</td>')[0].split('</b>')[0].split('<b>')[1]
                            player_test_bowling['BEST INNINGS BOWLING']=split59[v].split('"nowrap">')[8].split('</td>')[0]
                            player_test_bowling['BEST MATCH BOWLING']=split59[v].split('"nowrap">')[9].split('</td>')[0]
                            player_test_bowling['BOWLING AVERAGE']=split59[v].split('"nowrap">')[10].split('</td>')[0]
                            player_test_bowling['ECONOMY RATE']=split59[v].split('"nowrap">')[11].split('</td>')[0]
                            player_test_bowling['BOWLING STRIKE RATE']=split59[v].split('"nowrap">')[12].split('</td>')[0]
                            player_test_bowling['FIVE WKTS IN AN INNINGS']=split59[v].split('"nowrap">')[13].split('</td>')[0]
                            player_test_bowling['TEN WKTS IN A MATCH']=split59[v].split('"nowrap">')[14].split('</td>')[0]
                        except IndexError:
                            count52=count52+1
                            if count52==1:
                                list51.append(player_test_bowling)
            for f in twenty20_url_bowling:
                #print(p)
                headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
                }
                r233 = requests.get(f,headers=headers)
                t232 = r233.text.split('<caption>Most wickets</caption>')[1]
                #print(t32)
                split258=t232.split('<tbody>')[1].split('</tbody>')[0]
                split259=split258.split('<td class="left"')
                #print(split59)
                twenty20_Matches2_bowling={}
                Bowling_Records['twenty20_Matches_bowling']=twenty20_Matches2_bowling
                #print(split9[47])
                list512=[]
                twenty20_Matches2_bowling['players']=list512
                for q in range(1,len(split259)):
                    count152=0
                    if(q%2!=0):
                        player_twenty20_bowling={}
                        player_twenty20_bowling['NAME']=split259[q].split('<a href="')[1].split('" class="data-link">')[1].split('</a></td>')[0]
                        player_twenty20_bowling['ABOUT_player']='https://stats.espncricinfo.com'+split259[q].split('<a href="')[1].split('" class="data-link">')[0]
                        count152=count152+1
                        #print(player)
                    else:
                        try:
                            player_twenty20_bowling['PLAYING_SPAN']=split259[q].split('"nowrap">')[1].split('</td>')[0]
                            player_twenty20_bowling['MATCHES PLAYED']=split259[q].split('"nowrap">')[2].split('</td>')[0]
                            player_twenty20_bowling['INNING PLAYED']=split259[q].split('"nowrap">')[3].split('</td>')[0]
                            player_twenty20_bowling['OVERS BOWLED']=split259[q].split('"nowrap">')[4].split('</td>')[0]
                            player_twenty20_bowling['MAIDEN EARNED']=split259[q].split('"nowrap">')[5].split('</td>')[0]
                            try:
                                player_twenty20_bowling['RUNS CONCEDED']=split259[q].split('"nowrap">')[6].split('</td>')[0].split('</b>')[0].split('<b>')[1]
                            except:
                                player_twenty20_bowling['RUNS CONCEDED']=split259[q].split('"nowrap">')[6].split('</td>')[0]
                            
                            player_twenty20_bowling['WICKETS TAKEN']=split259[q].split('"nowrap">')[7].split('</td>')[0].split('</b>')[0].split('<b>')[1]
                            player_twenty20_bowling['BEST INNINGS BOWLING']=split259[q].split('"nowrap">')[8].split('</td>')[0]
                            player_twenty20_bowling['BEST MATCH BOWLING']=split259[q].split('"nowrap">')[9].split('</td>')[0]
                            player_twenty20_bowling['BOWLING AVERAGE']=split259[q].split('"nowrap">')[10].split('</td>')[0]
                            player_twenty20_bowling['ECONOMY RATE']=split259[q].split('"nowrap">')[11].split('</td>')[0]
                            player_twenty20_bowling['BOWLING STRIKE RATE']=split259[q].split('"nowrap">')[12].split('</td>')[0]
                            player_twenty20_bowling['FIVE WKTS IN AN INNINGS']=split259[q].split('"nowrap">')[13].split('</td>')[0]
                            player_twenty20_bowling['TEN WKTS IN A MATCH']=split259[q].split('"nowrap">')[14].split('</td>')[0]
                        except IndexError:
                            count152=count152+1
                            if count152==1:
                                list512.append(player_twenty20_bowling)
            for n in odi_url_bowling:
                #print(p)
                headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
                }
                r339=requests.get(n,headers=headers)
                t329=r339.text.split('<caption>Most wickets</caption>')[1]
                #print(t32)
                split589=t329.split('<tbody>')[1].split('</tbody>')[0]
                split599=split589.split('<td class="left"')
                #print(split59)
                odi_Matches2_bowling={}
                Bowling_Records['odi_Matches_bowling']=odi_Matches2_bowling
                #print(split9[47])
                list519=[]
                odi_Matches2_bowling['players']=list519
                for v in range(1,len(split599)):
                    count529=0
                    if(v%2!=0):
                        player_odi_bowling={}
                        player_odi_bowling['NAME']=split599[v].split('<a href="')[1].split('" class="data-link">')[1].split('</a></td>')[0]
                        player_odi_bowling['ABOUT_player']='https://stats.espncricinfo.com'+split599[v].split('<a href="')[1].split('" class="data-link">')[0]
                        count529=count529+1
                        #print(player)
                    else:
                        try:
                            player_odi_bowling['PLAYING_SPAN']=split599[v].split('"nowrap">')[1].split('</td>')[0]
                            player_odi_bowling['MATCHES PLAYED']=split599[v].split('"nowrap">')[2].split('</td>')[0]
                            player_odi_bowling['INNING PLAYED']=split599[v].split('"nowrap">')[3].split('</td>')[0]
                            player_odi_bowling['OVERS BOWLED']=split599[v].split('"nowrap">')[4].split('</td>')[0]
                            player_odi_bowling['MAIDEN EARNED']=split599[v].split('"nowrap">')[5].split('</td>')[0]
                            try:
                                player_odi_bowling['RUNS CONCEDED']=split599[v].split('"nowrap">')[6].split('</td>')[0].split('</b>')[0].split('<b>')[1]
                            except:
                                player_odi_bowling['RUNS CONCEDED']=split599[v].split('"nowrap">')[6].split('</td>')[0]
                            
                            player_odi_bowling['WICKETS TAKEN']=split599[v].split('"nowrap">')[7].split('</td>')[0].split('</b>')[0].split('<b>')[1]
                            player_odi_bowling['BEST INNINGS BOWLING']=split599[v].split('"nowrap">')[8].split('</td>')[0]
                            player_odi_bowling['BEST MATCH BOWLING']=split599[v].split('"nowrap">')[9].split('</td>')[0]
                            player_odi_bowling['BOWLING AVERAGE']=split599[v].split('"nowrap">')[10].split('</td>')[0]
                            player_odi_bowling['ECONOMY RATE']=split599[v].split('"nowrap">')[11].split('</td>')[0]
                            player_odi_bowling['BOWLING STRIKE RATE']=split599[v].split('"nowrap">')[12].split('</td>')[0]
                            player_odi_bowling['FIVE WKTS IN AN INNINGS']=split599[v].split('"nowrap">')[13].split('</td>')[0]
                            player_odi_bowling['TEN WKTS IN A MATCH']=split599[v].split('"nowrap">')[14].split('</td>')[0]
                        except IndexError:
                            count529=count529+1
                            if count529==1:
                                list519.append(player_odi_bowling)
    #print(countries)
    with open("cricketdata.json", "w") as outfile:
        print("Loding data into file")
        json.dump(countries, outfile)
print("Done!!! you got the file")


# In[ ]:




