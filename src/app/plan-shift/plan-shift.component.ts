import {Component, Input, OnInit} from '@angular/core';

@Component({
  selector: 'app-plan-shift',
  templateUrl: './plan-shift.component.html',
  styleUrls: ['./plan-shift.component.scss']
})
export class PlanShiftComponent implements OnInit {

  @Input() shift;




  constructor() { }

  ngOnInit() {
  }

}
