import {Component, Input, OnInit} from '@angular/core';

@Component({
  selector: 'app-map-more',
  templateUrl: './map-more.component.html',
  styleUrls: ['./map-more.component.scss']
})
export class MapMoreComponent implements OnInit {

  @Input() type;

  constructor() { }

  ngOnInit() {
  }

}
