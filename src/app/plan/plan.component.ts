import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-plan',
  templateUrl: './plan.component.html',
  styleUrls: ['./plan.component.scss']
})
export class PlanComponent implements OnInit {

  hour = 8;

  displayHour = 8;
  ampm = 'am';

  constructor() { }

  ngOnInit() {
  }

  onSliderChange($event) {
    this.hour = $event.value;
    this.displayHour = (this.hour >= 12) ? this.hour - 12 : this.hour;
    this.ampm = (this.hour >= 12) ? 'pm' : 'am';

  }
}
