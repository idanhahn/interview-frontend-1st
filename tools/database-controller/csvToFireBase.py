import csv
import json
from collections import OrderedDict

sections = [
  {
    'id': '0',
	'name': 'West Desert Inn Rd.',
    'strokeColor': 'red',
    'strokeWeight': 6,
    'strokeOpacity': 1,
	'startPoint': {
		'lat': 36.129594,
		'lng': -115.334764
	},
	'endPoint': {
		'lat': 36.130543,
		'lng': -115.180477,
	},
	'path': [
	{
		'lat': 36.129594,
		'lng': -115.334764
	},
	{
		'lat': 36.129803,
		'lng': -115.333075
	},
        {
		'lat': 36.129833,
		'lng': -115.315200
	},
        {
		'lat': 36.129837,
		'lng': -115.297041
	},
        {
		'lat': 36.129537,
		'lng': -115.278927
	},
        {
		'lat': 36.129174,
		'lng': -115.260985
	},
        {
		'lat': 36.129468,
		'lng': -115.243015
	},
        {
		'lat': 36.129096,
		'lng': -115.224945
	},
        {
		'lat': 36.129998,
		'lng': -115.208073
	},
        {
		'lat': 36.130005,
		'lng': -115.199058
	},
        {
		'lat': 36.130214,
		'lng': -115.191788
	},
        {
		'lat': 36.129787,
		'lng': -115.182236
	},
        {
		'lat': 36.130543,
		'lng': -115.180477
	}

    ],
    'prediction': [],
    'incidents': {},
    'events': {},
    'weather': [],
	'traffic': []
  },
  {
    'id': '1',
	'name': 'East Desert Inn Rd.- West of Eastern Av.',
    'strokeColor': 'red',
    'strokeWeight': 6,
    'strokeOpacity': 1,
	'startPoint': {
		'lat': 36.130543,
		'lng': -115.180477
	},
	'endPoint': {
		'lat': 36.129928,
		'lng': -115.118657
	},
	'path': [
	{
		'lat': 36.130543,
		'lng': -115.180477
	},
	{
		'lat': 36.131342,
		'lng': -115.178497
	},
        {
		'lat': 36.131829,
		'lng': -115.175081
	},
        {
		'lat': 36.131774,
		'lng': -115.174046
	},
        {
		'lat': 36.131444,
		'lng': -115.172258
	},
        {
		'lat': 36.131364,
		'lng': -115.166666
	},
        {
		'lat': 36.130962,
		'lng': -115.165371
	},
        {
		'lat': 36.129857,
		'lng': -115.163496
	},
        {
		'lat': 36.129595,
		'lng': -115.162394
	},
        {
		'lat': 36.129648,
		'lng': -115.155970
	},
        {
		'lat': 36.129428,
		'lng': -115.153737
	},
        {
		'lat': 36.129435,
		'lng': -115.147714
	},
        {
		'lat': 36.129757,
		'lng': -115.146056
	},
        {
		'lat': 36.129860,
		'lng': -115.128120
	},
	{
		'lat': 36.129928,
		'lng': -115.118657
	}


    ],
    'prediction': [],
    'incidents': {},
    'events': {},
    'weather': [],
	'traffic': []
	},
   {
    'id': '2',
	'name': 'East Desert Inn Rd. - East of Eastern Av.',
    'strokeColor': 'red',
    'strokeWeight': 6,
    'strokeOpacity': 1,
	'startPoint': {
		'lat': 36.129928,
		'lng': -115.118657
	},
	'endPoint': {
		'lat': 36.129597,
		'lng': -115.065278
	},
	'path': [
	{
		'lat': 36.129928,
		'lng': -115.118657
	},
        {
		'lat': 36.129756,
		'lng': -115.109709
	},
        {
		'lat': 36.129604,
		'lng': -115.091873
	},
        {
		'lat': 36.129653,
		'lng': -115.084962
	},
        {
		'lat': 36.130156,
		'lng': -115.083877
	},
        {
		'lat': 36.130863,
		'lng': -115.083133
	},
        {
		'lat': 36.131085,
		'lng': -115.082946
	},
        {
		'lat': 36.130934,
		'lng': -115.082456
	},
        {
		'lat': 36.129759,
		'lng': -115.081529
	},
        {
		'lat': 36.129613,
		'lng': -115.081246
	},
        {
		'lat': 36.129597,
		'lng': -115.065278
	}


    ],
    'prediction': [],
    'incidents': {},
    'events': {},
    'weather': [],
	'traffic': []
	},
  {
    'id': '3',
    'name': 'I15 - int. 35-42a',
    'strokeColor': 'red',
    'strokeWeight': 6,
    'strokeOpacity': 1,
	'startPoint': {
		'lat': 36.168936,
		'lng': -115.158886
	},
	'endPoint': {
		'lat': 36.129037,
		'lng': -115.180747
	},
	'path': [
	{
		'lat': 36.168936,
		'lng': -115.158886
	},
	{
		'lat': 36.167135,
		'lng': -115.159626
	},
        {
		'lat': 36.164981,
		'lng': -115.160149
	},
        {
		'lat': 36.16317,
		'lng': -115.160353
	},
        {
		'lat': 36.158676,
		'lng': -115.160364
	},
        {
		'lat': 36.157503,
		'lng': -115.160417
	},
        {
		'lat': 36.15667,
		'lng': -115.160622
	},
        {
		'lat': 36.155931,
		'lng': -115.160987
	},
        {
		'lat': 36.15516,
		'lng': -115.161581
	},
        {
		'lat': 36.151481,
		'lng': -115.16485
	},
        {
		'lat': 36.148647,
		'lng': -115.167353
	},
        {
		'lat': 36.144955,
		'lng': -115.170571
	},
        {
		'lat': 36.141296,
		'lng': -115.173815
	},
        {
		'lat': 36.137627,
		'lng': -115.177055
	},
        {
		'lat': 36.135882,
		'lng': -115.178501
	},
        {
		'lat': 36.134712,
		'lng': -115.179236
	},
        {
		'lat': 36.134712,
		'lng': -115.179236
	},
        {
		'lat': 36.133595,
		'lng': -115.179761
	},
        {
		'lat': 36.132334,
		'lng': -115.180223
	},
        {
		'lat': 36.13118,
		'lng': -115.180531
	},
	{
		'lat': 36.129037,
		'lng': -115.180747
	}
   ],
    'prediction': [],
    'incidents': {},
    'events': {},
    'weather': [],
	'traffic': []
	},
  {
    'id': '4',
    'name': 'I15 - int. 33-35',
    'strokeColor': 'red',
    'strokeWeight': 6,
    'strokeOpacity': 1,
	'startPoint': {
		'lat': 36.129037,
		'lng': -115.180747
	},
	'endPoint': {
		'lat': 36.043602,
		'lng': -115.180871
	},
	'path': [
	{
		'lat': 36.129037,
		'lng': -115.180747
	},
	{
		'lat': 36.124473,
		'lng': -115.180772
	},
        {
		'lat': 36.122331,
		'lng': -115.180776
	},
        {
		'lat': 36.117823,
		'lng': -115.180778
	},
        {
		'lat': 36.113299,
		'lng': -115.180783
	},
        {
		'lat': 36.108795,
		'lng': -115.18075
	},
        {
		'lat': 36.104271,
		'lng': -115.180791
	},
        {
		'lat': 36.09975,
		'lng': -115.180799
	},
        {
		'lat': 36.09523,
		'lng': -115.180879
	},
        {
		'lat': 36.09071,
		'lng': -115.180836
	},
        {
		'lat': 36.08618,
		'lng': -115.180815
	},
        {
		'lat': 36.081711,
		'lng': -115.180816
	},
        {
		'lat': 36.077206,
		'lng': -115.180877
	},
        {
		'lat': 36.072717,
		'lng': -115.180876
	},
        {
		'lat': 36.068217,
		'lng': -115.180906
	},
        {
		'lat': 36.063689,
		'lng': -115.180929
	},
        {
		'lat': 36.059152,
		'lng': -115.180934
	},

        {
		'lat': 36.054635,
		'lng': -115.180939
	},

        {
		'lat': 36.050112,
		'lng': -115.180952
	},
        {
		'lat': 36.045627,
		'lng': -115.180937
	},
		{
		'lat': 36.043602,
		'lng': -115.180871
	}
   ],
    'prediction': [],
    'incidents': {},
    'events': {},
    'weather': [],
	'traffic': []
	},
    {
    'id': '5',
	'name': 'West Flamingo Rd.',
    'strokeColor': 'red',
    'strokeWeight': 6,
    'strokeOpacity': 1,
	'startPoint': {
		'lat': 36.115062,
		'lng': -115.302568
	},
	'endPoint': {
		'lat': 36.114489,
		'lng': -115.180620
	},
	'path': [
        {
		'lat':  36.115062,
		'lng': -115.302568
	},
	{
	        'lat': 36.114910,
	        'lng': -115.296985
	},
	{
	        'lat': 36.114910,
	        'lng': -115.279041
	},
        {
	        'lat': 36.114622,
	        'lng': -115.261023
	},
        {
	        'lat': 36.114606,
	        'lng': -115.252019
	},
        {
	        'lat': 36.114472,
	        'lng': -115.233921
	},
        {
	        'lat': 36.114445,
	        'lng': -115.224825
	},
        {
	        'lat': 36.114927,
	        'lng': -115.216479
	},
        {
	        'lat': 36.115436,
	        'lng': -115.208050
	},
        {
	        'lat': 36.115572,
	        'lng': -115.190041
	},
        {
	        'lat': 36.115456,
	        'lng': -115.188291
	},
        {
	        'lat': 36.114353,
	        'lng': -115.183443
	},
        {
	        'lat': 36.114319,
	        'lng': -115.182148
	},
        {
		'lat': 36.114489,
		'lng': -115.180620
	}

   ],
    'prediction': [],
    'incidents': {},
    'events': {},
    'weather': [],
	'traffic': []
	},
   {
    'id': '6',
	'name': 'East Flamingo Rd.- East of Eastern Av.',
    'strokeColor': 'red',
    'strokeWeight': 6,
    'strokeOpacity': 1,
	'startPoint': {
		'lat': 36.114698,
		'lng': -115.119181
	},
	'endPoint': {
		'lat': 36.114837,
		'lng': -115.064684
	},
	'path': [
	{
		'lat': 36.114698,
		'lng': -115.119181
	},
        {
		'lat': 36.115014,
		'lng': -115.109826
	},
        {
		'lat': 36.115223,
		'lng': -115.100911
	},
        {
		'lat': 36.115258,
		'lng': -115.091964
	},
        {
		'lat': 36.115007,
		'lng': -115.082694
	},
        {
		'lat': 36.114925,
		'lng': -115.079950
	},
        {
		'lat': 36.114903,
		'lng': -115.071412
	},
        {
		'lat': 36.114916,
		'lng': -115.066925
	},
    {
		'lat': 36.114837,
		'lng': -115.064684
	}


   ],
    'prediction': [],
    'incidents': {},
    'events': {},
    'weather': [],
	'traffic': []
	},
   {
    'id': '7',
	'name': 'East Flamingo Rd.- West of Eastern Av.',
    'strokeColor': 'red',
    'strokeWeight': 6,
    'strokeOpacity': 1,
	'startPoint': {
		'lat': 36.114489,
		'lng': -115.180620
	},
	'endPoint': {
		'lat': 36.114698,
		'lng': -115.119181
	},
	'path': [
	{
		'lat': 36.114489,
		'lng': -115.180620
	},
        {
		'lat': 36.114765,
		'lng': -115.176978
	},
	{
		'lat': 36.114623,
		'lng': -115.169706
	},
        {
		'lat': 36.114484,
		'lng': -115.163971
	},
        {
		'lat': 36.114314,
		'lng': -115.154030
	},
        {
		'lat': 36.114766,
		'lng': -115.150163
	},
        {
		'lat': 36.114565,
		'lng': -115.137845
	},
        {
		'lat': 36.114698,
		'lng': -115.119181
	}

   ],
    'prediction': [],
    'incidents': {},
    'events': {},
    'weather': [],
	'traffic': []
	},
   {
   'id': '8',
	'name': 'North Las Vegas Blv.',
    'strokeColor': 'red',
    'strokeWeight': 6,
    'strokeOpacity': 1,
	'startPoint': {
		'lat': 36.235970,
		'lng': -115.062105
	},
	'endPoint': {
		'lat': 36.173642,
		'lng': -115.137903
	},
	'path': [
	{
		'lat': 36.235970,
		'lng': -115.062105
	},
	{
		'lat': 36.225425,
		'lng': -115.080151
	},
        {
		'lat': 36.215509,
		'lng': -115.097174
	},
        {
		'lat': 36.206982,
		'lng': -115.111736
	},
        {
		'lat': 36.199651,
		'lng': -115.124037
	},
        {
		'lat': 36.197857,
		'lng': -115.126577
	},
        {
		'lat': 36.195517,
		'lng': -115.129352
	},
        {
		'lat': 36.193228,
		'lng': -115.131670
	},
        {
		'lat': 36.191356,
		'lng': -115.133180
	},
        {
		'lat': 36.190095,
		'lng': -115.133563
	},
        {
		'lat': 36.189365,
		'lng': -115.134047
	},
        {
		'lat': 36.182322,
		'lng': -115.133993
	},
        {
		'lat': 36.180428,
		'lng': -115.134357
	},
        {
		'lat': 36.176926,
		'lng': -115.135802
	},
        {
		'lat': 36.173642,
		'lng': -115.137903
	}


   ],
    'prediction': [],
    'incidents': {},
    'events': {},
    'weather': [],
	'traffic': []
	},
    {
    'id': '9',
	'name': 'South Las-Vegas Blvd.- North of Sands Av.',
    'strokeColor': 'red',
    'strokeWeight': 6,
    'strokeOpacity': 1,
	'startPoint': {
		'lat': 36.173642,
		'lng': -115.137903
	},
	'endPoint': {
		'lat': 36.125552,
		'lng': -115.169308
	},
	'path': [
	{
		'lat': 36.173642,
		'lng': -115.137903
	},
	{
		'lat': 36.158835,
		'lng': -115.147450
	},
        {
		'lat': 36.148418,
		'lng': -115.154264
	},
        {
		'lat': 36.131046,
		'lng': -115.165643
	},
        {
		'lat': 36.125552,
		'lng': -115.169308
	}

   ],
    'prediction': [],
    'incidents': {},
    'events': {},
    'weather': [],
	'traffic': []
	},
   {
    'id': '10',
	'name': 'South Las-Vegas Blvd.- South of Sands Av.',
    'strokeColor': 'red',
    'strokeWeight': 6,
    'strokeOpacity': 1,
	'startPoint': {
		'lat': 36.125552,
		'lng': -115.169308
	},
	'endPoint': {
		'lat': 36.063524,
		'lng': -115.172384
	},
	'path': [
	{
		'lat': 36.125552,
		'lng': -115.169308
	},
        {
		'lat': 36.121382,
		'lng': -115.171890
	},
        {
		'lat': 36.119916,
		'lng': -115.172486
	},
        {
		'lat': 36.117505,
		'lng': -115.172895
	},
        {
		'lat': 36.100849,
		'lng': -115.173001
	},
        {
		'lat': 36.086264,
		'lng': -115.172868
	},
        {
		'lat': 36.063524,
		'lng': -115.172384
	}

   ],
    'prediction': [],
    'incidents': {},
    'events': {},
    'weather': [],
	'traffic': []
	},
   {
    'id': '11',
   	'name': 'Paradise Rd.- North of Tropicana Av.',
    'strokeColor': 'red',
    'strokeWeight': 6,
    'strokeOpacity': 1,
	'startPoint': {
		'lat': 36.143619,
		'lng': -115.154752
	},
	'endPoint': {
		'lat': 36.101059,
		'lng': -115.149817
	},
	'path': [
	{
		'lat': 36.143619,
		'lng': -115.154752
	},
	{
		'lat': 36.121266,
		'lng': -115.154986
	},
        {
		'lat': 36.117865,
		'lng': -115.154985
	},
        {
		'lat': 36.114314,
		'lng': -115.154030
	},
        {
		'lat': 36.103852,
		'lng': -115.150755
	},
	{
		'lat': 36.101059,
		'lng': -115.149817
	}

   ],
    'prediction': [],
    'incidents': {},
    'events': {},
    'weather': [],
	'traffic': []
	},
   {
    'id': '12',
   	'name': 'Paradise Rd.- South of Tropicana Av.',
    'strokeColor': 'red',
    'strokeWeight': 6,
    'strokeOpacity': 1,
	'startPoint': {
		'lat': 36.101059,
		'lng': -115.149817
	},
	'endPoint': {
		'lat': 36.062705,
		'lng': -115.149654
	},
	'path': [
	{
		'lat': 36.101059,
		'lng': -115.149817
	},
        {
		'lat': 36.080384,
		'lng': -115.143278
	},
        {
		'lat': 36.078310,
		'lng': -115.143346
	},
        {
		'lat': 36.065934,
		'lng': -115.148242
	},
        {
		'lat': 36.062705,
		'lng': -115.149654
	}

   ],
    'prediction': [],
    'incidents': {},
    'events': {},
    'weather': [],
	'traffic': []
	},
   {
    'id': '13',
	'name': 'West Tropicana Av.',
    'strokeColor': 'red',
    'strokeWeight': 6,
    'strokeOpacity': 1,
	'startPoint': {
		'lat': 36.100000,
		'lng': -115.293890
	},
	'endPoint': {
		'lat': 36.100692,
		'lng': -115.180659
	},
	'path': [
	{
		'lat': 36.100000,
		'lng': -115.293890,
	},
	{
		'lat': 36.100053,
		'lng': -115.279237
	},
        {
		'lat': 36.099599,
		'lng': -115.261081
	},
        {
		'lat': 36.099644,
		'lng': -115.253557
	},
        {
		'lat': 36.099726,
		'lng': -115.251998
	},
        {
		'lat': 36.099782,
		'lng': -115.243103
	},
        {
		'lat': 36.099854,
		'lng': -115.238061
	},
        {
		'lat': 36.099773,
		'lng': -115.237096
	},
        {
		'lat': 36.099857,
		'lng': -115.225051
	},
        {
		'lat': 36.100854,
		'lng': -115.207958
	},
        {
		'lat': 36.100880,
		'lng': -115.199203
	},
        {
		'lat': 36.100863,
		'lng': -115.185523
	},
        {
		'lat': 36.100675,
		'lng': -115.184370
	},
        {
		'lat': 36.100692,
		'lng': -115.180659
	}

   ],
    'prediction': [],
    'incidents': {},
    'events': {},
    'weather': [],
	'traffic': []
	},
  {
    'id': '14',
	'name': 'East Tropicana Av.- West of Eastern Av.',
    'strokeColor': 'red',
    'strokeWeight': 6,
    'strokeOpacity': 1,
	'startPoint': {
		'lat': 36.100692,
		'lng': -115.180659
	},
	'endPoint': {
		'lat': 36.101059,
		'lng': -115.149817
	},
	'path': [
	{
		'lat': 36.100692,
		'lng': -115.180659
	},
	{
		'lat': 36.100862,
		'lng': -115.169861
	},
        {
		'lat': 36.100880,
		'lng': -115.164196
	},
        {
		'lat': 36.100887,
		'lng': -115.158584
	},
        {
		'lat': 36.101059,
		'lng': -115.149817
	}

   ],
    'prediction': [],
    'incidents': {},
    'events': {},
    'weather': [],
	'traffic': []
	},
   {
    'id': '15',
	'name': 'East Tropicana Av.- East of Eastern Av.',
    'strokeColor': 'red',
    'strokeWeight': 6,
    'strokeOpacity': 1,
	'startPoint': {
		'lat': 36.101059,
		'lng': -115.149817
	},
	'endPoint': {
		'lat': 36.100842,
		'lng': -115.050927
	},
	'path': [
	{
		'lat': 36.101059,
		'lng': -115.149817
	},
        {
		'lat': 36.101115,
		'lng': -115.147375
	},
        {
		'lat': 36.100963,
		'lng': -115.145889
	},
        {
		'lat': 36.100947,
		'lng': -115.142605
	},
        {
		'lat': 36.100963,
		'lng': -115.128040
	},
        {
		'lat': 36.100595,
		'lng': -115.124716
	},
        {
		'lat': 36.099982,
		'lng': -115.119242
	},
        {
		'lat': 36.100085,
		'lng': -115.098516
	},
        {
		'lat': 36.100324,
		'lng': -115.081812
	},
        {
		'lat': 36.100269,
		'lng': -115.063926
	},
        {
		'lat': 36.100531,
		'lng': -115.051809
	},
        {
		'lat': 36.100842,
		'lng': -115.050927
	}

   ],
    'prediction': [],
    'incidents': {},
    'events': {},
    'weather': [],
	'traffic': []
	},
   {
    'id': '16',
	'name': 'West Sahara Av.',
    'strokeColor': 'red',
    'strokeWeight': 6,
    'strokeOpacity': 1,
	'startPoint': {
		'lat': 36.144580,
		'lng': -115.336762
	},
	'endPoint': {
		'lat': 36.144168,
		'lng': -115.171059
	},
	'path': [
	{
		'lat': 36.144580,
		'lng': -115.336762
	},
	{
		'lat': 36.144359,
		'lng': -115.331722
	},
        {
		'lat': 36.144393,
		'lng': -115.315545
	},
        {
		'lat': 36.144411,
		'lng': -115.297671
	},
        {
		'lat': 36.144103,
		'lng': -115.286991
	},
        {
		'lat': 36.143888,
		'lng': -115.269954
	},
        {
		'lat': 36.143662,
		'lng': -115.260935
	},
        {
		'lat': 36.144164,
		'lng': -115.242924
	},
        {
		'lat': 36.144030,
		'lng': -115.233842
	},
        {
		'lat': 36.144377,
		'lng': -115.216708
	},
        {
		'lat': 36.144517,
		'lng': -115.207990
	},
        {
		'lat': 36.144443,
		'lng': -115.190781
	},
        {
		'lat': 36.144350,
		'lng': -115.180966
	},
        {
		'lat': 36.144168,
		'lng': -115.171059
	}

   ],
    'prediction': [],
    'incidents': {},
    'events': {},
    'weather': [],
	'traffic': []
	},
   {
    'id': '17',
	'name': 'East Sahara Av.- West of Eastern Av.',
    'strokeColor': 'red',
    'strokeWeight': 6,
    'strokeOpacity': 1,
	'startPoint': {
		'lat': 36.144168,
		'lng': -115.171059
	},
	'endPoint': {
		'lat': 36.144283,
		'lng': -115.118785
	},
	'path': [
	{
		'lat': 36.144168,
		'lng': -115.171059
	},
	{
		'lat': 36.143619,
		'lng': -115.154752
	},
        {
		'lat': 36.144242,
		'lng': -115.137015
	},
        {
		'lat': 36.144368,
		'lng': -115.125276
	},
        {
		'lat': 36.144283,
		'lng': -115.118785
	}


   ],
    'prediction': [],
    'incidents': {},
    'events': {},
    'weather': [],
	'traffic': []
	},
   {
    'id': '18',
	'name': 'East Sahara Av.- East of Eastern Av.',
    'strokeColor': 'red',
    'strokeWeight': 6,
    'strokeOpacity': 1,
	'startPoint': {
		'lat': 36.144281,
		'lng': -115.118789
	},
	'endPoint': {
		'lat': 36.144326,
		'lng': -115.065403
	},
	'path': [
	{
		'lat': 36.144281,
		'lng': -115.118789
	},
        {
		'lat': 36.144308,
		'lng': -115.117995
	},
        {
		'lat': 36.144363,
		'lng': -115.116341
	},
        {
		'lat': 36.144333,
		'lng': -115.107290
	},
        {
		'lat': 36.144433,
		'lng': -115.103531
	},
        {
		'lat': 36.144967,
		'lng': -115.102420
	},
        {
		'lat': 36.146252,
		'lng': -115.100677
	},
        {
		'lat': 36.146289,
		'lng': -115.099494
	},
        {
		'lat': 36.146282,
		'lng': -115.092033
	},
        {
		'lat': 36.146169,
		'lng': -115.091323
	},
        {
		'lat': 36.145761,
		'lng': -115.090607
	},
        {
		'lat': 36.144651,
		'lng': -115.089184
	},
    {
		'lat': 36.144388,
		'lng': -115.088436
	},
    {
		'lat': 36.144294,
		'lng': -115.082842
	},
	{
		'lat': 36.144341,
		'lng': -115.074418
	},
        {
		'lat': 36.144326,
		'lng': -115.065403
	}

   ],
    'prediction': [],
    'incidents': {},
    'events': {},
    'weather': [],
	'traffic': []
	},
   {
    'id': '19',
	'name': 'Spring Montain Rd.',
    'strokeColor': 'red',
    'strokeWeight': 6,
    'strokeOpacity': 1,
	'startPoint': {
		'lat': 36.126166,
		'lng': -115.315101
	},
	'endPoint': {
		'lat': 36.125448,
		'lng': -115.169301
	},
	'path': [
	{
		'lat': 36.126166,
		'lng': -115.315101
	},
	{
		'lat': 36.125979,
		'lng': -115.287947
	},
        {
		'lat': 36.125540,
		'lng': -115.261007
	},
        {
		'lat': 36.125713,
		'lng': -115.242773
	},
        {
		'lat': 36.125433,
		'lng': -115.224929
	},
        {
		'lat': 36.126276,
		'lng': -115.208117
	},
        {
		'lat': 36.126541,
		'lng': -115.190181
	},
        {
		'lat': 36.126103,
		'lng': -115.178321
	},
        {
		'lat': 36.125561,
		'lng': -115.173078
	},
        {
		'lat': 36.125448,
		'lng': -115.169301
	}


   ],
    'prediction': [],
    'incidents': {},
    'events': {},
    'weather': [],
	'traffic': []
    },
    {
    'id': '20',
	'name': 'West Harmon Av.',
    'strokeColor': 'red',
    'strokeWeight': 6,
    'strokeOpacity': 1,
	'startPoint': {
		'lat': 36.107092,
		'lng': -115.238022
	},
	'endPoint': {
		'lat': 36.110382,
		'lng': -115.051282
	},
	'path': [
        {
		'lat': 36.107092,
		'lng': -115.238022
	},
        {
	        'lat': 36.107166,
	        'lng': -115.224941
 	},
        {
	        'lat': 36.107640,
	        'lng': -115.216442
	},
        {
	        'lat': 36.108128,
	        'lng': -115.207970
	},
        {
	        'lat': 36.108208,
	        'lng': -115.194609
	},
        {
	        'lat': 36.108103,
	        'lng': -115.178947
	},
        {
	        'lat': 36.108536,
	        'lng': -115.177574
	},
        {
	        'lat': 36.109172,
	        'lng': -115.176326
	},
        {
	        'lat': 36.109211,
	        'lng': -115.173675
	},
        {
	        'lat': 36.108045,
	        'lng': -115.171943
	},
        {
	        'lat': 36.108017,
	        'lng': -115.163943
	},
        {
	        'lat': 36.107938,
	        'lng': -115.150430
	},
        {
	        'lat': 36.107762,
	        'lng': -115.137276
	},
        {
	        'lat': 36.107294,
	        'lng': -115.119072
	},
        {
	        'lat': 36.107600,
	        'lng': -115.100725
	},
        {
	        'lat': 36.107652,
	        'lng': -115.082414
	},
        {
	        'lat': 36.107571,
	        'lng': -115.064337
	},
        {
	        'lat': 36.107634,
	        'lng': -115.059907
	},
        {
	        'lat': 36.107777,
	        'lng': -115.059529
	},
        {
	        'lat': 36.109981,
	        'lng': -115.056476
	},
        {
	        'lat': 36.110226,
	        'lng': -115.055768
	},
        {
	        'lat': 36.110371,
	        'lng': -115.054095
	},
        {
		'lat': 36.110382,
		'lng': -115.051282
	}

   ],
    'prediction': [],
    'incidents': {},
    'events': {},
    'weather': [],
	'traffic': []
	},
   {
    'id': '21',
	'name': 'East Harmon Av.- West of Eastern Av.',
    'strokeColor': 'red',
    'strokeWeight': 6,
    'strokeOpacity': 1,
	'startPoint': {
		'lat': 36.107335,
		'lng': -115.119109
	},
	'endPoint': {
		'lat': 36.110388,
		'lng': -115.051333
	},
	'path': [
        {
		'lat': 36.107335,
		'lng': -115.119109
	},
        {
		'lat': 36.107608,
		'lng': -115.100695
	},
	{
		'lat': 36.107656,
		'lng': -115.091755
	},
	{
		'lat': 36.107665,
		'lng': -115.082432
	},
	{
		'lat': 36.107624,
		'lng': -115.073498
	},
	{
		'lat': 36.107640,
		'lng': -115.059873
	},
	{
		'lat': 36.110223,
		'lng': -115.055893
	},
	{
		'lat': 36.110388,
		'lng': -115.051333
	}

   ],
    'prediction': [],
    'incidents': {},
    'events': {},
    'weather': [],
	'traffic': []
	},
   {
    'id': '22',
	'name': 'East Harmon Av.- East of Eastern Av.',
    'strokeColor': 'red',
    'strokeWeight': 6,
    'strokeOpacity': 1,
	'startPoint': {
		'lat': 36.107335,
		'lng': -115.119109
	},
	'endPoint': {
		'lat': 36.110388,
		'lng': -115.051333
	},
	'path': [
        {
		'lat': 36.107335,
		'lng': -115.119109
	},
        {
		'lat': 36.107608,
		'lng': -115.100695
	},
	{
		'lat': 36.107656,
		'lng': -115.091755
	},
	{
		'lat': 36.107665,
		'lng': -115.082432
	},
	{
		'lat': 36.107624,
		'lng': -115.073498
	},
	{
		'lat': 36.107640,
		'lng': -115.059873
	},
	{
		'lat': 36.110223,
		'lng': -115.055893
	},
	{
		'lat': 36.110388,
		'lng': -115.051333
	}

   ],
    'prediction': [],
    'incidents': {},
    'events': {},
    'weather': [],
	'traffic': []
	},
   {
    'id': '23',
    'name': 'North Maryland Parkway',
    'strokeColor': 'red',
    'strokeWeight': 6,
    'strokeOpacity': 1,
    'startPoint': {
        'lat': 36.158667951,
        'lng': -115.136999886
    },
    'endPoint': {
        'lat': 36.1297988981,
        'lng': -115.136912594
    },
    'path': [
    {
        'lat': 36.158667951,
        'lng': -115.136999886
    },
    {
        'lat': 36.1550729,
        'lng': -115.1375112
    },
    {
        'lat': 36.132849053,
        'lng': -115.136872141
    },
    {
        'lat': 36.1297988981,
        'lng': -115.136912594
    }

   ],
    'prediction': [],
    'incidents': {},
    'events': {},
    'weather': [],
	'traffic': []
	},
  {
    'id': '24',
    'name': 'South Maryland Parkway',
    'strokeColor': 'red',
    'strokeWeight': 6,
    'strokeOpacity': 1,
    'startPoint': {
        'lat':  36.1297988981,
        'lng': -115.136912594
    },
    'endPoint': {
        'lat': 36.0903086,
        'lng': -115.136854
    },
    'path': [
    {
        'lat':  36.1297988981,
        'lng': -115.136912594
    },
    {
        'lat': 36.1287398173,
        'lng': -115.136973719
    },
    {
        'lat': 36.1249043,
        'lng': -115.1372201
    },
    {
        'lat': 36.1212962,
        'lng': -115.1375316
    },
    {
        'lat': 36.1010447334,
        'lng': -115.136888233
    },
    {
        'lat': 36.0973067,
        'lng': -115.1374979
    },
    {
        'lat': 36.0941631,
        'lng': -115.1368398
    },
    {
        'lat': 36.0903086,
        'lng': -115.136854
    }

   ],
    'prediction': [],
    'incidents': {},
    'events': {},
    'weather': [],
	'traffic': []
	},
   {
    'id': '25',
    'name': 'I-15 - interchange 42a-45',
    'strokeColor': 'red',
    'strokeWeight': 6,
    'strokeOpacity': 1,
    'startPoint': {
      'lat' : 36.20685,
      'lng' : -115.132158
    },
    'endPoint': {
      'lat' : 36.173705,
      'lng' : -115.209489
    },
    'path': [
	{
      'lat' : 36.20685,
      'lng' : -115.132158
    }, {
      'lat' : 36.202987,
      'lng' : -115.13496
    }, {
      'lat' : 36.20028,
      'lng' : -115.136779
    }, {
      'lat' : 36.196038,
      'lng' : -115.138737
    }, {
      'lat' : 36.193873,
      'lng' : -115.139733
    }, {
      'lat' : 36.192677,
      'lng' : -115.140482
    }, {
      'lat' : 36.190077,
      'lng' : -115.142526
    }, {
      'lat' : 36.189317,
      'lng' : -115.142991
    }, {
      'lat' : 36.188075,
      'lng' : -115.143491
    }, {
      'lat' : 36.186818,
      'lng' : -115.143778
    }, {
      'lat' : 36.184062,
      'lng' : -115.143803
    }, {
      'lat' : 36.183054,
      'lng' : -115.144018
    }, {
      'lat' : 36.182128,
      'lng' : -115.144418
    }, {
      'lat' : 36.181215,
      'lng' : -115.145023
    }, {
      'lat' : 36.180563,
      'lng' : -115.145581
    }, {
      'lat' : 36.17982,
      'lng' : -115.146583
    }, {
      'lat' : 36.177252,
      'lng' : -115.151187
    }, {
      'lat' : 36.176094,
      'lng' : -115.152969
    }, {
      'lat' : 36.173754,
      'lng' : -115.155553
    }, {
      'lat' : 36.171527,
      'lng' : -115.157388
    }, {
      'lat' : 36.169983,
      'lng' : -115.158379
    }, {
      'lat' : 36.168936,
      'lng' : -115.15886
    }

   ],
    'prediction': [],
    'incidents': {},
    'events': {},
    'weather': [],
	'traffic': []
	},
   {
    'id': '26',
    'name': 'I-95 - interchange 76-80',
    'strokeColor': 'red',
    'strokeWeight': 6,
    'strokeOpacity': 1,
    'startPoint': {
      'lat' : 36.174301,
      'lng' : -115.132158
    },
    'endPoint': {
       'lat' : 36.174301,
      'lng' : -115.132158
    },
     'path': [
	{
      'lat' : 36.174301,
      'lng' : -115.154842
    }, {
      'lat' : 36.17514,
      'lng' : -115.160331
    }, {
      'lat' : 36.17514,
      'lng' : -115.160331
    }, {
      'lat' : 36.175914,
      'lng' : -115.16516
    }, {
      'lat' : 36.17598,
      'lng' : -115.167184
    }, {
      'lat' : 36.175713,
      'lng' : -115.170351
    }, {
      'lat' : 36.175212,
      'lng' : -115.175186
    }, {
      'lat' : 36.175219,
      'lng' : -115.180771
    }, {
      'lat' : 36.175376,
      'lng' : -115.184169
    }, {
      'lat' : 36.17625,
      'lng' : -115.188826
    }, {
      'lat' : 36.176324,
      'lng' : -115.191234
    }, {
      'lat' : 36.175926,
      'lng' : -115.194101
    }, {
      'lat' : 36.174173,
      'lng' : -115.199218
    }, {
      'lat' : 36.173531,
      'lng' : -115.201592
    }, {
      'lat' : 36.173395,
      'lng' : -115.204173
    }, {
      'lat' : 36.173705,
      'lng' : -115.209489
    }

   ],
    'prediction': [],
    'incidents': {},
    'events': {},
    'weather': [],
	'traffic': []
	},
   {
    'id': '27',
    'name': 'I-515 - interchange 72-76',
    'strokeColor': 'red',
    'strokeWeight': 6,
    'strokeOpacity': 1,
    'startPoint': {
      'lat' : 36.174286,
      'lng' : -115.154838
    },
    'endPoint': {
      'lat' : 36.151822,
      'lng' : -115.091473
    },
     'path': [
	{
      'lat' : 36.158834,
      'lng' : -115.09161
    }, {
      'lat' : 36.16067,
      'lng' : -115.091782
    }, {
      'lat' : 36.163043,
      'lng' : -115.092898
    }, {
      'lat' : 36.164931,
      'lng' : -115.094615
    }, {
      'lat' : 36.166351,
      'lng' : -115.097072
    }, {
      'lat' : 36.167422,
      'lng' : -115.101352
    }, {
      'lat' : 36.167725,
      'lng' : -115.107886
    }, {
      'lat' : 36.167872,
      'lng' : -115.12267
    }, {
      'lat' : 36.168132,
      'lng' : -115.125063
    }, {
      'lat' : 36.16886,
      'lng' : -115.127241
    }, {
      'lat' : 36.17339,
      'lng' : -115.137015
    }, {
      'lat' : 36.174152,
      'lng' : -115.140234
    }, {
      'lat' : 36.175442,
      'lng' : -115.143882
    }, {
      'lat' : 36.175581,
      'lng' : -115.14562
    }, {
      'lat' : 36.175399,
      'lng' : -115.147122
    }, {
      'lat' : 36.174074,
      'lng' : -115.15269
    }, {
      'lat' : 36.174286,
      'lng' : -115.154838
    }
   ],
    'prediction': [],
    'incidents': {},
    'events': {},
    'weather': [],
	'traffic': []
	},
   {
    'id': '28',
    'name': 'I-515 - int. 65-72',
    'strokeColor': 'red',
    'strokeWeight': 6,
    'strokeOpacity': 1,
    'startPoint': {
      'lat' : 36.080539,
      'lng' : -115.044508
    },
    'endPoint': {
      'lat' : 36.129884,
      'lng' : -115.118507
    },
     'path': [  {
	  'lat' : 36.080539,
      'lng' : -115.044508
    }, {
      'lat' : 36.086747,
      'lng' : -115.056524
    }, {
      'lat' : 36.087692,
      'lng' : -115.06015
    }, {
      'lat' : 36.088403,
      'lng' : -115.065986
    }, {
      'lat' : 36.089632,
      'lng' : -115.069121
    }, {
      'lat' : 36.094812,
      'lng' : -115.077559
    }, {
      'lat' : 36.096771,
      'lng' : -115.079715
    }, {
      'lat' : 36.099406,
      'lng' : -115.081378
    }, {
      'lat' : 36.102873,
      'lng' : -115.082236
    }, {
      'lat' : 36.119554,
      'lng' : -115.08289
    }, {
      'lat' : 36.122206,
      'lng' : -115.083577
    }, {
      'lat' : 36.124754,
      'lng' : -115.085186
    }, {
      'lat' : 36.128411,
      'lng' : -115.088158
    }, {
      'lat' : 36.131687,
      'lng' : -115.089649
    }, {
      'lat' : 36.151822,
      'lng' : -115.091473
    }, {
      'lat' : 36.158834,
      'lng' : -115.091473
    }
   ],
    'prediction': [],
    'incidents': {},
    'events': {},
    'weather': [],
	'traffic': []
	} ,
   {
    'id': '29',
    'name': 'North Eastern Ave.',
    'strokeColor': 'red',
    'strokeWeight': 6,
    'strokeOpacity': 1,
    'startPoint': {
     'lat' : 36.1884411687,
      'lng' : -115.116118432
    },
    'endPoint': {
      'lat' : 36.0236203504,
      'lng' : -115.118458007
    },
     'path': [
	{
      'lat' : 36.1884411687,
      'lng' : -115.116118432
    }, {
      'lat' : 36.1884411687,
      'lng' : -115.116118432
    }, {
      'lat' : 36.1851411,
      'lng' : -115.1161598
    }, {
      'lat' : 36.1735979646,
      'lng' : -115.116261709
    }, {
      'lat' : 36.1697211,
      'lng' : -115.1160335
    }, {
      'lat' : 36.1659488,
      'lng' : -115.1158731
    }, {
      'lat' : 36.1638205,
      'lng' : -115.1159116
    }, {
      'lat' : 36.1605335515,
      'lng' : -115.117796024
    }, {
      'lat' : 36.159374319,
      'lng' : -115.118793443
    }, {
      'lat' : 36.143799376,
      'lng' : -115.118872357
    }, {
      'lat' : 36.144281,
      'lng' : -115.118789
    }, {
      'lat' : 36.129884,
      'lng' : -115.118507
    }
   ],
    'prediction': [],
    'incidents': {},
    'events': {},
    'weather': [],
	'traffic': []
	} ,
   {
    'id': '30',
    'name': 'South Eastern Ave.',
    'strokeColor': 'red',
    'strokeWeight': 6,
    'strokeOpacity': 1,
    'startPoint': {
      'lat' : 36.129884,
      'lng' : -115.118507
    },
    'endPoint': {
       'lat' : 36.158829,
      'lng' : -115.118882
    },
     'path': [
	 {
      'lat' : 36.129884,
      'lng' : -115.118507
    }, {
      'lat' : 36.1260588,
      'lng' : -115.1186931
    }, {
      'lat' : 36.1144031151,
      'lng' : -115.119207236
    }, {
      'lat' : 36.1104493,
      'lng' : -115.1191326
    }, {
      'lat' : 36.1066005,
      'lng' : -115.1190686
    }, {
      'lat' : 36.0914008332,
      'lng' : -115.118851294
    }, {
      'lat' : 36.0870833,
      'lng' : -115.1187885
    }, {
      'lat' : 36.0715088064,
      'lng' : -115.118689603
    }, {
      'lat' : 36.0676847,
      'lng' : -115.1185819
    }, {
      'lat' : 36.0496192554,
      'lng' : -115.118171048
    }, {
      'lat' : 36.0378209542,
      'lng' : -115.11829742
    }, {
      'lat' : 36.0236203504,
      'lng' : -115.118458007
    }
   ],
    'prediction': [],
    'incidents': {},
    'events': {},
    'weather': [],
	'traffic': []
	} ,
   {
    'id': '31',
    'name': 'West Charleston Blvd.',
    'strokeColor': 'red',
    'strokeWeight': 6,
    'strokeOpacity': 1,
    'startPoint': {
       'lat' : 36.159119,
      'lng' : -115.243708
    },
    'endPoint': {
      'lat' : 36.159034,
      'lng' : -115.062316
    },
     'path': [
	{
      'lat' : 36.159119,
      'lng' : -115.243708
    }, {
      'lat' : 36.15908,
      'lng' : -115.205877
    }, {
      'lat' : 36.158896,
      'lng' : -115.160302
    }, {
      'lat' : 36.158839,
      'lng' : -115.145258
    }, {
      'lat' : 36.158829,
      'lng' : -115.118882
    }
   ],
    'prediction': [],
    'incidents': {},
    'events': {},
    'weather': [],
	'traffic': []
	},
	{
    'id': '32',
    'name': 'East Charleston Blvd.',
    'strokeColor': 'red',
    'strokeWeight': 6,
    'strokeOpacity': 1,
    'startPoint': {
      'lat' : 36.158829,
      'lng' : -115.118882
    },
    'endPoint': {
      'lat' : 36.159034,
      'lng' : -115.062316
    },
     'path': [
	{
      'lat' : 36.158829,
      'lng' : -115.118882
    }, {
      'lat' : 36.158834,
      'lng' : -115.118856
    }, {
      'lat' : 36.159034,
      'lng' : -115.062316
    }

   ],
    'prediction': [],
    'incidents': {},
    'events': {},
    'weather': [],
	'traffic': []
   }






]



events = []

weather = []

traffic = []

incidents = {}

events_new = {}

# Events
with open('events.csv', newline='') as csvfile:
  reader = csv.reader(csvfile, delimiter=',')
  # get date (first row)
  date = next(reader)
  # skip second row (headings)
  first = next(reader)
  cnt = 0
  for row in reader:
    eventLine = {
	  'event_pointer' : row[1],
	  'event_id' : row[2],
      'title': row[3],
      'icon': row[4],
      'description': row[5],
      'startTime': row[6],
      'endTime': row[7],
      'lat': float(row[8]),
      'lng': float(row[9]),
    }
    sectionsAffected = row[0].split('|');
#    print(sectionsAffected)
#    for s in sectionsAffected:
#      print(s)
#    sections[int(s)]['events'].append(eventLine)
#    events.append(eventLine)

# Events_new
with open('events.csv', newline='') as csvfile:
  reader = csv.reader(csvfile, delimiter=',')
  # get date (first row)
  date_new = next(reader)
  # skip second row (headings)
  first_new = next(reader)
  cnt = 0
  for row in reader:
    eventID = row[2]
    eventLine2 ={
	  'affectedSections' : '',
	  'type' : 'Event',
	  'title': row[3],
	  'icon': row[4],
	  'description' : row[5],
	  'startTime': row[6],
	  'startTime1' : date_new[1]+'T'+row[6],
      'endTime' : row[7],
      'endTime1' : date_new[1]+'T'+row[7],
	  'lat': float(row[8]),
      'lng': float(row[9]),
	  'eventEditCfg'  : '',
	  'event_id' : row[2]

    }
    EventEntry_for_section = {
      'event_id' : row[2],
      'valid' : 'true'
    }
    sectionsAffected = row[0].split('|');
    print(sectionsAffected)
    for s in sectionsAffected:
      #sections[int(s)]['events'].append(EventEntry_for_section)
      sections[int(s)]['events'][eventID]= { 'valid' : bool('true') }
      if eventLine2['affectedSections']== '':
        eventLine2['affectedSections']+=s
      else:
        eventLine2['affectedSections']+= ', '
        eventLine2['affectedSections']+=s
 #   events.append(eventLine2)
    events_new[eventID] = eventLine2


 # Incidents
with open('road_incidents.csv', newline='') as csvfile:
  reader = csv.reader(csvfile, delimiter=',')
  # get date (first row)
  date_inc = next(reader)
  # skip second row (headings)
  first = next(reader)
  cnt = 0
  for row in reader:
    incidentID = row[2]
    incidentLine ={
	  'affectedSections' : '',
	  'type' : 'Incident',
	  'title': row[3],
	  'icon': row[4],
	  'incidentType' : row[5],
	  'hour': row[6],
	  'time' : date_new[1]+'T'+row[6],
      #'endTime' : row[7],
      #'endTime1' : date_new[1]+'T'+row[7],
	  'lat': float(row[8]),
      'lng': float(row[9]),
	  'eventEditCfg'  : '',
	  'incident_id' : row[2]

    }
    IncidentEntry_for_section = {
      'incident_id' : row[2],
      'valid' : 'true'
    }
    sectionsAffected = row[0].split('|');
    print(sectionsAffected)
    for s in sectionsAffected:
      #sections[int(s)]['incidents'].append(EventEntry_for_section)
      sections[int(s)]['incidents'][incidentID]= { 'valid' : bool('true') }
      if incidentLine['affectedSections']== '':
        incidentLine['affectedSections']+=s
      else:
        incidentLine['affectedSections']+= ', '
        incidentLine['affectedSections']+=s
 #   events.append(eventLine2)
    incidents[incidentID] = incidentLine

# Weather
with open('weather.csv', newline='') as csvfile:
  reader = csv.reader(csvfile, delimiter=',')
  first = next(reader)
  for row in reader:
    weatherline = {
      'hour': row[1],
      'temp': row[2],
      'conditions': row[3],
      'conditionsIcon': row[4],
      'precipitation': row[5],
	  'humidity': row[6],
      'wind': row[7],
      'windDirection': row[8]
    }
    sections[int(row[0])]['weather'].append(weatherline)
    # store only section0 weather as global weather
    if (int(row[0]) == 0):
      weather.append(weatherline)

# Traffic
with open('traffic.csv', newline='') as csvfile:
  reader = csv.reader(csvfile, delimiter=',')
  first = next(reader)
  for row in reader:
    trafficline = {
      'hour': row[1],
      'disturbance': row[2],
      'commute_time': row[3],
      'breaks': row[4],
      'traffic_count' : row[5]
    }
    sections[int(row[0])]['traffic'].append(trafficline)
    # store only section0 weather as global weather
    if (int(row[0]) == 0):
      traffic.append(trafficline)

# Prediction
with open('prediction.csv', newline='') as csvfile:
  reader = csv.reader(csvfile, delimiter=',')
  for row in reader:
    print(', '.join(row))
    prediction = {
      'hour': row[1],
      'result': row[2]
    }
    sections[int(row[0])]['prediction'].append(prediction)

  jsonResult = {
    'date': date[1],
    'events': events_new,
    'sections': sections,
    'weather': weather,
    'traffic': traffic,
    'incidents': incidents
  }

print('JSON ', json.dumps(jsonResult))

 # printing to output file:
with open(date[1] + '_result.json', 'w') as outfile:
  print ('{' , file=outfile)
#  print ('\"'+ date[1] + '\" : {' , file=outfile)

  print ('  \"events\" :' , file=outfile)
  json.dump(events_new, outfile)

  print (',  \n' , file=outfile)
  print ('  \"incidents\" :' , file=outfile)
  json.dump(incidents, outfile)

  print (',  \n' , file=outfile)
  print ('  \"sections\" :' , file=outfile)
  json.dump(sections, outfile)

  print (',  \n' , file=outfile)
  print ('  \"weather\" :' , file=outfile)
  json.dump(weather, outfile)

#  print ('  \n  \"traffic\" :' , file=outfile)
#  json.dump(traffic, outfile)

  # printing the legacy code
#  print ('  \n', file=outfile)
#  json.dump(jsonResult, outfile)


  print ('\n}', file=outfile)
