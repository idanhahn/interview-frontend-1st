import {Component, Input, OnInit} from '@angular/core';

@Component({
  selector: 'app-ongoing-section-detail',
  templateUrl: './ongoing-section-detail.component.html',
  styleUrls: ['./ongoing-section-detail.component.scss']
})
export class OngoingSectionDetailComponent implements OnInit {

  @Input() sectionOngoing;

  incidents;

  constructor() { }

  ngOnInit() {
  }

  onActionClick(){
    console.log('implement');
  }
}
