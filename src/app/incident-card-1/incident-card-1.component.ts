// Question

import {Component, Input, OnInit} from '@angular/core';

@Component({
  selector: 'app-incident-card-1',
  templateUrl: './incident-card-1.component.html',
  styleUrls: ['./incident-card-1.component.scss']
})
export class IncidentCard1Component implements OnInit {

  @Input() incident;

  constructor() { }

  ngOnInit() {
  }

}
