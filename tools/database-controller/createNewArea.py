import csv
import json
from collections import OrderedDict

sections = []

events = []

weather = []

traffic = []

riskAlerts = []

ongoing = []

roadIncidents = []

events_new = {}


# sections
with open('LV_sections.csv', newline='') as csvfile:
  reader = csv.reader(csvfile, delimiter=',')
  first = next(reader)

  for row in reader:
    id = row[0]
    name = row[1]
    path = [];

    print(len(row))
    for path_index in range(6, len(row) - 2,2):
      if (row[int(path_index)] != ""):
        p = {
          'lat': float(row[int(path_index)]),
          'lng': float(row[int(path_index+1)])
        }
        path.append(p)

    sectionGeometric = {
      'startPoint' : {
        'lat': float(row[2]),
        'lng': float(row[3])
      },
      'endPoint': {
        'lat': float(row[4]),
        'lng': float(row[5])
      },
      'path': path
    }

    section = {
      'id': id,
      'name': name,
      'sectionGeometric': sectionGeometric,
      'weather': [],
      'traffic': [],
      'crashPrediction': []
    }
    sections.append(section)


  jsonResult = {
    'sections': sections
  }

# Weather
with open('weather.csv', newline='') as csvfile:
  reader = csv.reader(csvfile, delimiter=',')
  first = next(reader)
  for row in reader:
    weatherline = {
      'temp': int(row[2]),
      'conditions': row[3],
      'conditionsIcon': row[4],
      'precipitation': int(row[5]),
      'humidity': row[6],
      'wind': int(row[7]),
      'windDirection': row[8],
      'visibility': int(row[9])
    }
    print(int(row[0]))
    sections[int(row[0])]['weather'].append(weatherline)
    # store only section0 weather as global weather
    if (int(row[0]) == 0):
      weather.append(weatherline)

# Traffic
with open('traffic.csv', newline='') as csvfile:
  reader = csv.reader(csvfile, delimiter=',')
  first = next(reader)
  for row in reader:

    disturbance = int(row[4])
    commuteTime = int(row[3])
    breaks = int(row[5])
    trafficCount = int(row[2])

    title = "Traffic Flowing"
    color = "#006600"

    if commuteTime > 25:
      title = "Minor Traffic Congestion"
      color = "#F0F000"
    elif commuteTime > 27:
      title = "Traffic Congestion"
      color = "#8B0000"
    elif disturbance > 300:
      title = "Minor Disturbances"
      color = "#F0F000"
    elif disturbance > 400:
      title = "Major Disturbances"
      color = "#8B0000"
    elif breaks > 1000:
      title = "Bottle neck forming"
      color = "#F0F000"


    trafficline = {
      'title': title,
      'color': color,
      'disturbances': disturbance,
      'commuteTime': commuteTime,
      'breaks': breaks,
      'trafficCount': trafficCount
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
    pr = float(row[2])
    title = ""
    color = ""

    if pr == 0.0:
      title = "Low"
      color = "#00EE76"
    elif pr == 0.1:
      title = "Low"
      color = "#00EE76"
    elif pr == 0.2:
      title = "Low"
      color = "#00CD66"
    elif pr == 0.3:
      title = "Low"
      color = "#008B45"
    elif pr == 0.4:
      title = "Low - Moderate"
      color = "#F0F000"
    elif pr == 0.5:
      title = "Low - Moderate"
      color = "#F0F000"
    elif pr == 0.6:
      title = "Moderate"
      color = "#FF4500"
    elif pr == 0.7:
      title = "Moderate - High"
      color = "#DC143C"
    elif pr == 0.8:
      title = "High"
      color = "#8B0000"
    elif pr == 0.9:
      title = "High"
      color = "#8B0000"
    elif pr == 1.0:
      title = "Very High"
      color = "#800000"
    else:
      title = "Low"
      color = "#008B45"
      print('something wrong ' + pr)
      exit(1)


    prediction = {
      'title': title,
      'color': color,
      'result': float(pr)
    }
    sections[int(row[0])]['crashPrediction'].append(prediction)


with open('risk_alerts.csv', newline='') as csvfile:
  reader = csv.reader(csvfile, delimiter=',')
  first = next(reader)
  for row in reader:
    riskAlertLine = {
      'type': row[0],
      'lat': float(row[1]),
      'lng': float(row[2]),
      'zoom': float(row[3]),
      'icon': row[4],
      'number': row[5],
      'title': row[6],
      'subtitle': row[7],
      'riskLevel': row[8],
      'riskLevelIcon': row[9],
      'commute': float(row[10]),
      'speed': float(row[11]),
      'hardBreaks': float(row[12]),
      'precipitation': float(row[13]),
      'visibility': float(row[14]),
      'wind': float(row[15]),
      'actionPatrolToggle': row[16],
      'actionPatrolTime': row[17],
      'actionWarningToggle': row[18],
      'actionWarningTime': row[19],
      'numberColor': row[20]
    }
    riskAlerts.append(riskAlertLine)

with open('risk_alerts_incidents.csv', newline='') as csvfile:
  reader = csv.reader(csvfile, delimiter=',')
  first = next(reader)
  for row in reader:
    riskAlertInicidentsLine = {
      'type': row[0],
      'lat': float(row[1]),
      'lng': float(row[2]),
      'zoom': float(row[3]),
      'icon': row[4],
      'number': row[5],
      'title': row[6],
      'subtitle': row[7],
      'alertIcon': row[8],
      'alertContent': row[9],
      'detailTitle': row[10],
      'detailSubTitle': row[11],
      'detailAmount': float(row[12]),
      'detailGraph': row[13]
    }
    riskAlerts.append(riskAlertInicidentsLine)


with open('ongoing.csv', newline='') as csvfile:
  reader = csv.reader(csvfile, delimiter=',')
  first = next(reader)
  for row in reader:
    ongoingLine = {
      'type': row[0],
      'lat': float(row[1]),
      'lng': float(row[2]),
      'zoom': float(row[3]),
      'icon': row[4],
      'number': row[5],
      'title': row[6],
      'subtitle': row[7],
      'riskLevel': row[8],
      'riskLevelIcon': row[9],
      'commute': float(row[10]),
      'speed': float(row[11]),
      'hardBreaks': float(row[12]),
      'precipitation': float(row[13]),
      'visibility': float(row[14]),
      'wind': float(row[15]),
      'actionPatrolToggle': row[16],
      'actionPatrolTime': row[17],
      'actionWarningToggle': row[18],
      'actionWarningTime': row[19],
      'numberColor': row[20]
    }
    ongoing.append(ongoingLine)

with open('road_incidents.csv', newline='') as csvfile:
  reader = csv.reader(csvfile, delimiter=',')
  first = next(reader)
  for row in reader:
    location = {
      'type': row[10],
      'latLng': {
        'lat': float(row[11]),
        'lng': float(row[12])
      },
      'sectionID': row[13]
    }
    roadIncidentLine = {
      'id': row[0],
      'type': row[1],
      'title': row[2],
      'description': row[3],
      'icon': row[4],
      'actions': row[5],
      'startTime': row[6],
      'endTime': row[7],
      'state': row[8],
      'lanesAffected': row[9],
      'location': location
    }
    roadIncidents.append(roadIncidentLine)

print('JSON ', json.dumps(jsonResult))

# printing to output file:
with open('lv_sections_result.json', 'w') as outfile:
  print('{', file=outfile)

  print('  \"sections\" :', file=outfile)
  json.dump(sections, outfile)

  print (',  \n' , file=outfile)
  print('  \"riskAlerts\":', file=outfile)
  json.dump(riskAlerts, outfile)

  print (',  \n' , file=outfile)
  print('  \"ongoing\":', file=outfile)
  json.dump(ongoing, outfile)

  print (',  \n' , file=outfile)
  print('  \"roadIncidents\":', file=outfile)
  json.dump(roadIncidents, outfile)

  print('\n}', file=outfile)

