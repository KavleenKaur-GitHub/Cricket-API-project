from flask import Flask
import json,pymysql,time
from flask import request,redirect
from collections import Counter
app = Flask(__name__)
res = {} 
AUTHKEY = '123'
@app.route("/", methods=['GET','POST'])
def root():
    res['code'] = 2
    res['msg'] = 'No endpoint specified'
    res['req'] = '/'
    return json.dumps(res,indent=4)
@app.route("/getBestBatsman", methods=['GET','POST'])
def getBestBatsman():
    country = request.args.get('Country')
    format=request.args.get('Format')
    #auth:
    qkey = request.args.get('key')
    if qkey is None or qkey!= AUTHKEY:
        res['code'] = 0
        res['msg'] = 'Bad key given'
        res['req'] = 'getBestBatsman'
        return json.dumps(res,indent=4)
    else:
        print("debug ",country)
        if country is None or country!='AllCountry':
            res['code'] = 2
            res['msg'] = 'Country not specified.'
            res['req'] = 'getBestBatsman'
            return json.dumps(res,indent=4)
        elif country=='AllCountry':
            with open('cricketdata.json', 'r') as openfile:
                json_object = json.load(openfile)
            country_names=[]
            country_names=json_object.keys()
            list=[]
            list2=[]
            list3=[]
            list5=[]
            list4=[]
            list6=[]
            for i in country_names:
                number_of_players_Twenty20=len(json_object[i]['Batting_Records']['Twenty20_Matches']['players'])
                number_of_players_Odi=len(json_object[i]['Batting_Records']['Odi_Matches']['players'])
                number_of_players=len(json_object[i]['Batting_Records']['Test_Matches']['players'])
                for j in range(0,number_of_players):
                    try:
                        a=int(json_object[i]['Batting_Records']['Test_Matches']['players'][j]['RUNS_SCORED'])
                        list.append(a)
                    except KeyError:
                        print("missing data encoutered")
                for e in range(0,number_of_players_Twenty20):
                    try:
                        a=int(json_object[i]['Batting_Records']['Twenty20_Matches']['players'][e]['RUNS_SCORED'])
                        list2.append(a)
                    except KeyError:
                        print("missing data encoutered")
                for d in range(0,number_of_players_Odi):
                    try:
                       a=int(json_object[i]['Batting_Records']['Odi_Matches']['players'][d]['RUNS_SCORED'])
                       list3.append(a)
                    except KeyError:
                        print("missing data encoutered")
            list.sort(reverse=True)
            #print(list[1])
            list2.sort(reverse=True)
            #print(list2)
            list3.sort(reverse=True)
            #print(list3)
            for k in range(1,50,2):
                for i in country_names:
                    number_of_players=len(json_object[i]['Batting_Records']['Test_Matches']['players'])
                    for j in range(0,number_of_players,2):
                        try:
                            if int(json_object[i]['Batting_Records']['Test_Matches']['players'][j]['RUNS_SCORED'])==list[k]:
                                list4.append(json_object[i]['Batting_Records']['Test_Matches']['players'][j])
                        except KeyError:
                            print("no value")
            for k in range(1,50,2):
                for i in country_names:
                    number_of_players_Twenty20=len(json_object[i]['Batting_Records']['Twenty20_Matches']['players'])                
                    for l in range(0,number_of_players_Twenty20,2):
                        try:
                            if int(json_object[i]['Batting_Records']['Twenty20_Matches']['players'][l]['RUNS_SCORED'])==list2[k]:
                                list5.append(json_object[i]['Batting_Records']['Twenty20_Matches']['players'][l])
                        except KeyError:
                            print("no value")
            for k in range(1,50,2):
                 for i in country_names:
                    number_of_players_Odi=len(json_object[i]['Batting_Records']['Odi_Matches']['players'])
                    for m in range(0,number_of_players_Odi,2):
                        try:
                            if int(json_object[i]['Batting_Records']['Odi_Matches']['players'][m]['RUNS_SCORED'])==list3[k]:
                                list6.append(json_object[i]['Batting_Records']['Odi_Matches']['players'][m])
                        except KeyError:
                                print("no value")
            if format is None or format not in ['TestMatches','Twenty20Matches','OdiMatches']:
                res['code'] = 2
                res['msg'] = 'Format not specified.'
                res['req'] = 'getBestBatsman'
                return json.dumps(res,indent=4)
            else:
                if format=='TestMatches':
                   res['code'] = 1
                   res['msg'] = 'Request:OK'
                   res['req'] = 'getBestBatsman'
                   d = {}
                   d['Test_Matches']=list4
                   res['data'] = d
                   return json.dumps(res,indent=4)
                if format=='Twenty20Matches':
                   res['code'] = 1
                   res['msg'] = 'Request:OK'
                   res['req'] = 'getBestBatsman'
                   d = {}
                   d['Twenty20_Matches']=list5
                   res['data'] = d
                   return json.dumps(res,indent=4)    
                if format=='OdiMatches':
                   res['code'] = 1
                   res['msg'] = 'Request:OK'
                   res['req'] = 'getBestBatsman'
                   d = {}
                   d['Odi_Matches']=list6
                   res['data'] = d
                   return json.dumps(res,indent=4)    
@app.route("/getBestBowler",methods=['GET','POST'])
def getBestBowler():
    country = request.args.get('Country')
    format=request.args.get('Format')
    #auth:
    qkey = request.args.get('key')
    if qkey is None or qkey!= AUTHKEY:
        res['code'] = 0
        res['msg'] = 'Bad key given'
        res['req'] = 'getBestBowler'
        return json.dumps(res,indent=4)
    else:
        print("debug ",country)
        if country is None or country!='AllCountry':
            res['code'] = 2
            res['msg'] = 'Country not specified.'
            res['req'] = 'getBestBowler'
            return json.dumps(res,indent=4)
        elif country=='AllCountry':
            with open('cricketdata.json', 'r') as openfile:
                 json_object = json.load(openfile)
            country_names=[]
            country_names=json_object.keys()
            list7=[]
            list8=[]
            list9=[]
            list10=[]
            list11=[]
            list12=[]
            for i in country_names:
                 number_of_players_Twenty20_bowling=len(json_object[i]['Bowling_Records']['twenty20_Matches_bowling']['players'])
                 number_of_players_Odi_bowling=len(json_object[i]['Bowling_Records']['odi_Matches_bowling']['players'])
                 number_of_players_bowling=len(json_object[i]['Bowling_Records']['test_Matches_bowling']['players'])
                 for j in range(0,number_of_players_bowling):
                      try:
                         a=int(json_object[i]['Bowling_Records']['test_Matches_bowling']['players'][j]['WICKETS TAKEN'])
                         list7.append(a)
                      except KeyError:
                         print("missing data encoutered")
                 for e in range(0,number_of_players_Twenty20_bowling):
                      try:
                          a=int(json_object[i]['Bowling_Records']['twenty20_Matches_bowling']['players'][e]['WICKETS TAKEN'])
                          list8.append(a)
                      except KeyError:
                         print("missing data encoutered")
                 for d in range(0,number_of_players_Odi_bowling):
                    try:
                         a=int(json_object[i]['Bowling_Records']['odi_Matches_bowling']['players'][d]['WICKETS TAKEN'])
                         list9.append(a)
                    except KeyError:
                         print("missing data encoutered")
            list7.sort(reverse=True)
            list8.sort(reverse=True)
            list9.sort(reverse=True)
            #print(list7)
            for t in range(1,50):
                 for i in country_names:
                     number_of_players_bowling=len(json_object[i]['Bowling_Records']['test_Matches_bowling']['players'])
                     for f in range(0,number_of_players_bowling):
                         try:
                             if int(json_object[i]['Bowling_Records']['test_Matches_bowling']['players'][f]['WICKETS TAKEN'])==list7[t]:
                                 list10.append(json_object[i]['Bowling_Records']['test_Matches_bowling']['players'][f])
                         except KeyError:
                             print("no value")
            for h in range(1,50):
                 for i in country_names:
                     number_of_players_bowling=len(json_object[i]['Bowling_Records']['twenty20_Matches_bowling']['players'])
                     for g in range(0,number_of_players_bowling):
                         try:
                             if int(json_object[i]['Bowling_Records']['twenty20_Matches_bowling']['players'][g]['WICKETS TAKEN'])==list8[h]:
                                 list11.append(json_object[i]['Bowling_Records']['twenty20_Matches_bowling']['players'][g])
                         except KeyError:
                              print("no value")
            for o in range(1,50):
                 for i in country_names:
                     number_of_players_bowling=len(json_object[i]['Bowling_Records']['odi_Matches_bowling']['players'])
                     for v in range(0,number_of_players_bowling):
                         try:
                             if int(json_object[i]['Bowling_Records']['odi_Matches_bowling']['players'][v]['WICKETS TAKEN'])==list9[o]:
                                 list12.append(json_object[i]['Bowling_Records']['odi_Matches_bowling']['players'][v])
                         except KeyError:
                             print("no value")
                                
            if format is None or format not in ['TestMatches','Twenty20Matches','OdiMatches']:
                res['code'] = 2
                res['msg'] = 'Format not specified.'
                res['req'] = 'getBestBatsman'
                return json.dumps(res,indent=4)
            else:
                if format=='TestMatches':
                   res['code'] = 1
                   res['msg'] = 'Request:OK'
                   res['req'] = 'getBestBowler'
                   d = {}
                   d['Test_Matches']=list10
                   res['data'] = d
                   return json.dumps(res,indent=4)
                if format=='Twenty20Matches':
                   res['code'] = 1
                   res['msg'] = 'Request:OK'
                   res['req'] = 'getBestBowler'
                   d = {}
                   d['Twenty20_Matches']=list11
                   res['data'] = d
                   return json.dumps(res,indent=4)    
                if format=='OdiMatches':
                   res['code'] = 1
                   res['msg'] = 'Request:OK'
                   res['req'] = 'getBestBowler'
                   d = {}
                   d['Odi_Matches']=list12
                   res['data'] = d
                   return json.dumps(res,indent=4)
@app.route("/getHighestStrikeRate", methods=['GET','POST'])
def getHighestStrikeRate():
    country = request.args.get('Country')
    format=request.args.get('Format')
    #auth:
    qkey = request.args.get('key')
    if qkey is None or qkey!= AUTHKEY:
        res['code'] = 0
        res['msg'] = 'Bad key given'
        res['req'] = 'getHighestStrikeRate'
        return json.dumps(res,indent=4)
    else:
        print("debug ",country)
        if country is None or country!='AllCountry':
            res['code'] = 2
            res['msg'] = 'Country not specified.'
            res['req'] = 'getHighestStrikeRate'
            return json.dumps(res,indent=4)
        elif country=='AllCountry':
            with open('cricketdata.json', 'r') as openfile:
                 json_object = json.load(openfile)
            country_names=[]
            country_names=json_object.keys()
            list15=[]
            list16=[]
            list17=[]
            list18=[]
            list19=[]
            list20=[]
            for i in country_names:
                 number_of_players_Twenty20=len(json_object[i]['Batting_Records']['Twenty20_Matches']['players'])
                 number_of_players_Odi=len(json_object[i]['Batting_Records']['Odi_Matches']['players'])
                 number_of_players=len(json_object[i]['Batting_Records']['Test_Matches']['players'])
                 for j in range(0,number_of_players):
                     try:
                         a=float(json_object[i]['Batting_Records']['Test_Matches']['players'][j]['BATTING_AVERAGE'])
                         list15.append(a)
                     except:print("missing data encoutered")
                 for e in range(0,number_of_players_Twenty20):
                     try:
                         a=float(json_object[i]['Batting_Records']['Twenty20_Matches']['players'][e]['BATTING_AVERAGE'])
                         list16.append(a)
                     except:print("missing data encoutered")
                 for d in range(0,number_of_players_Odi):
                     try:
                         a=float(json_object[i]['Batting_Records']['Odi_Matches']['players'][d]['BATTING_AVERAGE'])
                         list17.append(a)
                     except:print("missing data encoutered")
            list15.sort(reverse=True)
            list16.sort(reverse=True)
            list17.sort(reverse=True)
            for k in range(1,50,2):
                 for i in country_names:
                     number_of_players=len(json_object[i]['Batting_Records']['Test_Matches']['players'])
                     for j in range(0,number_of_players,2):
                         try:
                              if float(json_object[i]['Batting_Records']['Test_Matches']['players'][j]['BATTING_AVERAGE'])==list15[k]:
                                 list18.append(json_object[i]['Batting_Records']['Test_Matches']['players'][j])
                         except:print("no value")
            for k in range(1,50,2):
                for i in country_names:
                     number_of_players_Twenty20=len(json_object[i]['Batting_Records']['Twenty20_Matches']['players'])                
                     for l in range(0,number_of_players_Twenty20,2):
                         try:
                             if float(json_object[i]['Batting_Records']['Twenty20_Matches']['players'][l]['BATTING_AVERAGE'])==list16[k]:
                                 list19.append(json_object[i]['Batting_Records']['Twenty20_Matches']['players'][l])
                         except:print("no value")
            for k in range(1,50,2):
                for i in country_names:
                      number_of_players_Odi=len(json_object[i]['Batting_Records']['Odi_Matches']['players'])
                      for m in range(0,number_of_players_Odi,2):
                         try:
                             if float(json_object[i]['Batting_Records']['Odi_Matches']['players'][m]['BATTING_AVERAGE'])==list17[k]:
                                 list20.append(json_object[i]['Batting_Records']['Odi_Matches']['players'][m])
                         except:print("no value")
            if format is None or format not in ['TestMatches','Twenty20Matches','OdiMatches']:
                res['code'] = 2
                res['msg'] = 'Format not specified.'
                res['req'] = 'getHighestStrikeRate'
                return json.dumps(res,indent=4)
            else:
                if format=='TestMatches':
                   res['code'] = 1
                   res['msg'] = 'Request:OK'
                   res['req'] = 'getHighestStrikeRate'
                   d = {}
                   d['Test_Matches']=list18
                   res['data'] = d
                   return json.dumps(res,indent=4)
                if format=='Twenty20Matches':
                   res['code'] = 1
                   res['msg'] = 'Request:OK'
                   res['req'] = 'getHighestStrikeRate'
                   d = {}
                   d['Twenty20_Matches']=list19
                   res['data'] = d
                   return json.dumps(res,indent=4)    
                if format=='OdiMatches':
                   res['code'] = 1
                   res['msg'] = 'Request:OK'
                   res['req'] = 'getHighestStrikeRate'
                   d = {}
                   d['Odi_Matches']=list20
                   res['data'] = d
                   return json.dumps(res,indent=4)
@app.route("/getLowestEconomyRate", methods=['GET','POST'])
def getLowestEconomyRate():
    country = request.args.get('Country')
    format=request.args.get('Format')
    #auth:
    qkey = request.args.get('key')
    if qkey is None or qkey!= AUTHKEY:
        res['code'] = 0
        res['msg'] = 'Bad key given'
        res['req'] = 'getLowestEconomyRate'
        return json.dumps(res,indent=4)
    else:
        print("debug ",country)
        if country is None or country!='AllCountry':
            res['code'] = 2
            res['msg'] = 'Country not specified.'
            res['req'] = 'getLowestEconomyRate'
            return json.dumps(res,indent=4)
        elif country=='AllCountry':
            with open('cricketdata.json', 'r') as openfile:
                 json_object = json.load(openfile)
            country_names=[]
            country_names=json_object.keys()
            list21=[]
            list22=[]
            list23=[]
            list24=[]
            list25=[]
            list26=[]
            for i in country_names:
                 number_of_players_Twenty20_bowling=len(json_object[i]['Bowling_Records']['twenty20_Matches_bowling']['players'])
                 number_of_players_Odi_bowling=len(json_object[i]['Bowling_Records']['odi_Matches_bowling']['players'])
                 number_of_players_bowling=len(json_object[i]['Bowling_Records']['test_Matches_bowling']['players'])
                 for j in range(0,number_of_players_bowling):
                     try:
                         a=float(json_object[i]['Bowling_Records']['test_Matches_bowling']['players'][j]['ECONOMY RATE'])
                         list21.append(a)
                     except:print("missing data encoutered")
                 for e in range(0,number_of_players_Twenty20_bowling):
                     try:
                         a=float(json_object[i]['Bowling_Records']['twenty20_Matches_bowling']['players'][e]['ECONOMY RATE'])
                         list22.append(a)
                     except:print("missing data encoutered")
                 for d in range(0,number_of_players_Odi_bowling):
                     try:
                         a=float(json_object[i]['Bowling_Records']['odi_Matches_bowling']['players'][d]['ECONOMY RATE'])
                         list23.append(a)
                     except:print("missing data encoutered")
            list21.sort()
            list22.sort()
            list23.sort()
            #print(list7)
            for t in range(1,50):
                 for i in country_names:
                     number_of_players_bowling=len(json_object[i]['Bowling_Records']['test_Matches_bowling']['players'])
                     for f in range(0,number_of_players_bowling):
                         try:
                             if float(json_object[i]['Bowling_Records']['test_Matches_bowling']['players'][f]['ECONOMY RATE'])==list21[t]:
                                 list24.append(json_object[i]['Bowling_Records']['test_Matches_bowling']['players'][f])
                         except:print("no value")
            for h in range(1,50):
                 for i in country_names:
                     number_of_players_bowling=len(json_object[i]['Bowling_Records']['twenty20_Matches_bowling']['players'])
                     for g in range(0,number_of_players_bowling):
                         try:
                             if float(json_object[i]['Bowling_Records']['twenty20_Matches_bowling']['players'][g]['ECONOMY RATE'])==list22[h]:
                                 list25.append(json_object[i]['Bowling_Records']['twenty20_Matches_bowling']['players'][g])
                         except:print("no value")
            for o in range(1,50):
                 for i in country_names:
                     number_of_players_bowling=len(json_object[i]['Bowling_Records']['odi_Matches_bowling']['players'])
                     for v in range(0,number_of_players_bowling):
                         try:
                             if float(json_object[i]['Bowling_Records']['odi_Matches_bowling']['players'][v]['ECONOMY RATE'])==list23[o]:
                                 list26.append(json_object[i]['Bowling_Records']['odi_Matches_bowling']['players'][v])
                         except:print("no value")     
            if format is None or format not in ['TestMatches','Twenty20Matches','OdiMatches']:
                res['code'] = 2
                res['msg'] = 'Format not specified.'
                res['req'] = 'getLowestEconomyRate'
                return json.dumps(res,indent=4)
            else:
                if format=='TestMatches':
                   res['code'] = 1
                   res['msg'] = 'Request:OK'
                   res['req'] = 'getLowestEconomyRate'
                   d = {}
                   d['Test_Matches']=list24
                   res['data'] = d
                   return json.dumps(res,indent=4)
                if format=='Twenty20Matches':
                   res['code'] = 1
                   res['msg'] = 'Request:OK'
                   res['req'] = 'getLowestEconomyRate'
                   d = {}
                   d['Twenty20_Matches']=list25
                   res['data'] = d
                   return json.dumps(res,indent=4)    
                if format=='OdiMatches':
                   res['code'] = 1
                   res['msg'] = 'Request:OK'
                   res['req'] = 'getLowestEconomyRate'
                   d = {}
                   d['Odi_Matches']=list26
                   res['data'] = d
                   return json.dumps(res,indent=4)   
@app.route("/getBestCountriesBowling", methods=['GET','POST'])
def getBestCountriesBowling():
    country = request.args.get('Country')
    format=request.args.get('Format')
    #auth:
    qkey = request.args.get('key')
    if qkey is None or qkey!= AUTHKEY:
        res['code'] = 0
        res['msg'] = 'Bad key given'
        res['req'] = 'getBestCountriesBowling'
        return json.dumps(res,indent=4)
    else:
        print("debug ",country)
        if country is None or country!='AllCountry':
            res['code'] = 2
            res['msg'] = 'Country not specified.'
            res['req'] = 'getBestCountriesBowling'
            return json.dumps(res,indent=4)
        elif country=='AllCountry':
             with open('cricketdata.json', 'r') as openfile:
                 json_object = json.load(openfile)
        country_names=[]
        country_names=json_object.keys()
        list7=[]
        list8=[]
        list9=[]
        list10=[]
        list11=[]
        list12=[]
        test_bowling_allrecords=[]
        d1={}
        d2={}
        d3={}
        count=0
        test_bowling=[]
        twenty20_bowling_allrecords=[]
        odi_bowling_allrecords=[]
        twenty20_bowling=[]
        odi_bowling=[]
        for i in country_names:
             number_of_players_Twenty20_bowling=len(json_object[i]['Bowling_Records']['twenty20_Matches_bowling']['players'])
             number_of_players_Odi_bowling=len(json_object[i]['Bowling_Records']['odi_Matches_bowling']['players'])
             number_of_players_bowling=len(json_object[i]['Bowling_Records']['test_Matches_bowling']['players'])
             for j in range(0,number_of_players_bowling):
                 try:
                     a=int(json_object[i]['Bowling_Records']['test_Matches_bowling']['players'][j]['WICKETS TAKEN'])
                     list7.append(a)
                 except KeyError:
                     print("missing data encoutered")
             for e in range(0,number_of_players_Twenty20_bowling):
                  try:
                     a=int(json_object[i]['Bowling_Records']['twenty20_Matches_bowling']['players'][e]['WICKETS TAKEN'])
                     list8.append(a)
                  except KeyError:
                     print("missing data encoutered")
             for d in range(0,number_of_players_Odi_bowling):
                  try:
                     a=int(json_object[i]['Bowling_Records']['odi_Matches_bowling']['players'][d]['WICKETS TAKEN'])
                     list9.append(a)
                  except KeyError:
                     print("missing data encoutered")
        list7.sort(reverse=True)
        list8.sort(reverse=True)
        list9.sort(reverse=True)
        #print(list7)
        for t in range(1,50):
             for i in country_names:
                 number_of_players_bowling=len(json_object[i]['Bowling_Records']['test_Matches_bowling']['players'])
                 for f in range(0,number_of_players_bowling):
                     try:
                         if int(json_object[i]['Bowling_Records']['test_Matches_bowling']['players'][f]['WICKETS TAKEN'])==list7[t]:
                             test_bowling.append(i)
                             list10.append(json_object[i]['Bowling_Records']['test_Matches_bowling']['players'][f])                    
                     except KeyError:
                             print("no value")
        for h in range(1,50):
             for i in country_names:
                 number_of_players_bowling=len(json_object[i]['Bowling_Records']['twenty20_Matches_bowling']['players'])
                 for g in range(0,number_of_players_bowling):
                     try:
                         if int(json_object[i]['Bowling_Records']['twenty20_Matches_bowling']['players'][g]['WICKETS TAKEN'])==list8[h]:
                             twenty20_bowling.append(i)
                             list11.append(json_object[i]['Bowling_Records']['twenty20_Matches_bowling']['players'][g])
                     except KeyError:
                         print("no value")
        for o in range(1,50):
             for i in country_names:
                 number_of_players_bowling=len(json_object[i]['Bowling_Records']['odi_Matches_bowling']['players'])
                 for v in range(0,number_of_players_bowling):
                     try:
                         if int(json_object[i]['Bowling_Records']['odi_Matches_bowling']['players'][v]['WICKETS TAKEN'])==list9[o]:
                             odi_bowling.append(i)
                             list12.append(json_object[i]['Bowling_Records']['odi_Matches_bowling']['players'][v])
                     except KeyError:
                         print("no value")
        for h in country_names:
             d1[h]=test_bowling.count(h)
             test_bowling_allrecords.append(d1)
        for h in country_names:
             d2[h]=twenty20_bowling.count(h)
             twenty20_bowling_allrecords.append(d2)
        for h in country_names:
             d3[h]=odi_bowling.count(h)
             odi_bowling_allrecords.append(d3)  
        if format is None or format not in ['TestMatches','Twenty20Matches','OdiMatches']:
                res['code'] = 2
                res['msg'] = 'Format not specified.'
                res['req'] = 'getLowestEconomyRate'
                return json.dumps(res,indent=4)
        else:
            if format=='TestMatches':
                 res['code'] = 1
                 res['msg'] = 'Request:OK'
                 res['req'] = 'getBestCountriesBowling'
                 d = {}
                 d['Test_Matches']=test_bowling_allrecords
                 res['data'] = d
                 return json.dumps(res,indent=4)
            if format=='Twenty20Matches':
                 res['code'] = 1
                 res['msg'] = 'Request:OK'
                 res['req'] = 'getBestCountriesBowling'
                 d = {}
                 d['Twenty20_Matches']=twenty20_bowling_allrecords
                 res['data'] = d
                 return json.dumps(res,indent=4)    
            if format=='OdiMatches':
                 res['code'] = 1
                 res['msg'] = 'Request:OK'
                 res['req'] = 'getBestCountriesBowling'
                 d = {}
                 d['Odi_Matches']=odi_bowling_allrecords
                 res['data'] = d
                 return json.dumps(res,indent=4)
@app.route("/getBestCountriesBatting", methods=['GET','POST'])
def getBestCountriesBatting():
    country = request.args.get('Country')
    format=request.args.get('Format')
    #auth:
    qkey = request.args.get('key')
    if qkey is None or qkey!= AUTHKEY:
        res['code'] = 0
        res['msg'] = 'Bad key given'
        res['req'] = 'getBestCountriesBatting'
        return json.dumps(res,indent=4)
    else:
        print("debug ",country)
        if country is None or country!='AllCountry':
            res['code'] = 2
            res['msg'] = 'Country not specified.'
            res['req'] = 'getBestCountriesBatting'
            return json.dumps(res,indent=4)
        elif country=='AllCountry':
            with open('cricketdata.json', 'r') as openfile:
                json_object = json.load(openfile)
            country_names=[]
            country_names=json_object.keys()
            list=[]
            list2=[]
            list3=[]
            list5=[]
            list4=[]
            list6=[]
            test_batting_allrecords=[]
            d1={}
            d2={}
            d3={}
            count=0
            test_batting=[]
            twenty20_batting_allrecords=[]
            odi_batting_allrecords=[]
            twenty20_batting=[]
            odi_batting=[]
            for i in country_names:
                number_of_players_Twenty20=len(json_object[i]['Batting_Records']['Twenty20_Matches']['players'])
                number_of_players_Odi=len(json_object[i]['Batting_Records']['Odi_Matches']['players'])
                number_of_players=len(json_object[i]['Batting_Records']['Test_Matches']['players'])
                for j in range(0,number_of_players):
                    try:
                        a=int(json_object[i]['Batting_Records']['Test_Matches']['players'][j]['RUNS_SCORED'])
                        list.append(a)
                    except KeyError:
                        print("missing data encoutered")
                for e in range(0,number_of_players_Twenty20):
                    try:
                        a=int(json_object[i]['Batting_Records']['Twenty20_Matches']['players'][e]['RUNS_SCORED'])
                        list2.append(a)
                    except KeyError:
                        print("missing data encoutered")
                for d in range(0,number_of_players_Odi):
                    try:
                       a=int(json_object[i]['Batting_Records']['Odi_Matches']['players'][d]['RUNS_SCORED'])
                       list3.append(a)
                    except KeyError:
                        print("missing data encoutered")
            list.sort(reverse=True)
            #print(list[1])
            list2.sort(reverse=True)
            #print(list2)
            list3.sort(reverse=True)
            #print(list3)
            for k in range(1,50,2):
                for i in country_names:
                    number_of_players=len(json_object[i]['Batting_Records']['Test_Matches']['players'])
                    for j in range(0,number_of_players,2):
                        try:
                            if int(json_object[i]['Batting_Records']['Test_Matches']['players'][j]['RUNS_SCORED'])==list[k]:
                                test_batting.append(i)
                                list4.append(json_object[i]['Batting_Records']['Test_Matches']['players'][j])
                        except KeyError:
                            print("no value")
            for k in range(1,50,2):
                for i in country_names:
                    number_of_players_Twenty20=len(json_object[i]['Batting_Records']['Twenty20_Matches']['players'])                
                    for l in range(0,number_of_players_Twenty20,2):
                        try:
                            if int(json_object[i]['Batting_Records']['Twenty20_Matches']['players'][l]['RUNS_SCORED'])==list2[k]:
                                twenty20_batting.append(i)
                                list5.append(json_object[i]['Batting_Records']['Twenty20_Matches']['players'][l])
                        except KeyError:
                            print("no value")
            for k in range(1,50,2):
                 for i in country_names:
                    number_of_players_Odi=len(json_object[i]['Batting_Records']['Odi_Matches']['players'])
                    for m in range(0,number_of_players_Odi,2):
                        try:
                            if int(json_object[i]['Batting_Records']['Odi_Matches']['players'][m]['RUNS_SCORED'])==list3[k]:
                                odi_batting.append(i)
                                list6.append(json_object[i]['Batting_Records']['Odi_Matches']['players'][m])
                        except KeyError:
                                print("no value")
            for h in country_names:
                d1[h]=test_batting.count(h)
                test_batting_allrecords.append(d1)
            for h in country_names:
                d2[h]=twenty20_batting.count(h)
                twenty20_batting_allrecords.append(d2)
            for h in country_names:
                d3[h]=odi_batting.count(h)
                odi_batting_allrecords.append(d3)
            if format is None or format not in ['TestMatches','Twenty20Matches','OdiMatches']:
                res['code'] = 2
                res['msg'] = 'Format not specified.'
                res['req'] = 'getBestCountriesBatting'
                return json.dumps(res,indent=4)
            else:
                if format=='TestMatches':
                   res['code'] = 1
                   res['msg'] = 'Request:OK'
                   res['req'] = 'getBestCountriesBatting'
                   d = {}
                   d['Test_Matches']=test_batting_allrecords
                   res['data'] = d
                   return json.dumps(res,indent=4)
                if format=='Twenty20Matches':
                   res['code'] = 1
                   res['msg'] = 'Request:OK'
                   res['req'] = 'getBestCountriesBatting'
                   d = {}
                   d['Twenty20_Matches']=twenty20_batting_allrecords
                   res['data'] = d
                   return json.dumps(res,indent=4)    
                if format=='OdiMatches':
                   res['code'] = 1
                   res['msg'] = 'Request:OK'
                   res['req'] = 'getBestCountriesBatting'
                   d = {}
                   d['Odi_Matches']=odi_batting_allrecords
                   res['data'] = d
                   return json.dumps(res,indent=4)                     
if __name__ == "__main__":
    app.run(host='127.0.0.1',debug=False)