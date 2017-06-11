import { Component, OnInit } from '@angular/core';
import {MainService} from '../services/main.service';
import {FirebaseListObservable} from 'angularfire2/database';

@Component({
  selector: 'app-plan-panel-list',
  templateUrl: './plan-panel-list.component.html',
  styleUrls: ['./plan-panel-list.component.scss']
})
export class PlanPanelListComponent implements OnInit {


  shift1 = {
    title: '8am - 12pm',
    totalPolice: 2,
    totalSigns: 4,
    incidents : [
      {
        title: 'Rain Showers',
        subTitle: '',
        icon: 'icon-incident-rain'
      },
      {
        title: 'CES 2017',
        subTitle: 'Las Vegas Convention center',
        icon: 'icon-incident-crowd'
      }
    ],
    sectionRisks : [
      {
        title: 'I-15',
        subTitle: 'Sec 4',
        danger: 'high',
        togglePolice: 'on',
        toggleWarning: 'on',
        incidents: '3 incidents'
      },
      {
        title: 'US-95',
        subTitle: 'Sec 12',
        danger: 'high',
        togglePolice: 'off',
        toggleWarning: 'on',
        incidents: ''
      },
      {
        title: 'I-515',
        subTitle: 'Sec 2',
        danger: 'med',
        togglePolice: 'on',
        toggleWarning: 'off',
        incidents: ''
      }
    ]
  };

  shift2 = {
    title: '12pm - 16pm',
    totalPolice: 3,
    totalSigns: 1,
    shiftIncidents : [
      {
        title: 'Rain Showers',
        subTitle: '',
        icon: 'icon-incident-rain'
      },
      {
        title: 'CES 2017',
        subTitle: 'Las Vegas Convention center',
        icon: 'icon-incident-crowd'
      }
    ],
    sectionRisk : [
      {
        title: 'I-15',
        subTitle: 'Sec 4',
        danger: 'high',
        togglePolice: 'on',
        toggleWarning: 'on',
        incidents: '3 incidents'
      },
      {
        title: 'US-95',
        subTitle: 'Sec 12',
        danger: 'high',
        togglePolice: 'off',
        toggleWarning: 'on',
        incidents: ''
      },
      {
        title: 'I-515',
        subTitle: 'Sec 2',
        danger: 'med',
        togglePolice: 'on',
        toggleWarning: 'off',
        incidents: ''
      }
    ]

  };


  shifts: FirebaseListObservable<any>;

  constructor(private _ms: MainService) {
    this.shifts = _ms.getPlanShifts();
  }

  ngOnInit() {
  }

}
