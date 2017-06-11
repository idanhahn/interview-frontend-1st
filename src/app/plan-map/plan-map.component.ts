import {Component, Input, OnInit} from '@angular/core';
import {FirebaseListObservable} from 'angularfire2/database';
import {MainService} from '../services/main.service';

@Component({
  selector: 'app-plan-map',
  templateUrl: './plan-map.component.html',
  styleUrls: ['./plan-map.component.scss']
})
export class PlanMapComponent implements OnInit {

  @Input() hour;

  mapControl = {
    type: 'none',
    id: -1,
    center: {
      lat: 36.136507,
      lng: -115.162020
    },
    zoom: 12
  };


  sections: FirebaseListObservable<any>;

  constructor(private _mS: MainService ) {
    this.sections = _mS.getSections();
  }

  ngOnInit() {
  }


}
