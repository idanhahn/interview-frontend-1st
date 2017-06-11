import {Component, Input, OnInit} from '@angular/core';
import {FirebaseObjectObservable} from 'angularfire2/database';
import {RoadIncidentService} from '../services/road-incident.service';

@Component({
  selector: 'app-incident-card',
  templateUrl: './incident-card.component.html',
  styleUrls: ['./incident-card.component.scss']
})
export class IncidentCardComponent implements OnInit {

  @Input() incidentPtr;
  incident: FirebaseObjectObservable<any>;

  constructor(private _ris: RoadIncidentService) {}

  ngOnInit() {
    this.incident = this._ris.get(this.incidentPtr);
  }
}
