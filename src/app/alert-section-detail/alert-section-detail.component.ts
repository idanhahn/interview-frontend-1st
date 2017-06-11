import {Component, Input, OnChanges, OnInit, SimpleChanges} from '@angular/core';
import {animate, state, style, transition, trigger} from '@angular/animations';

@Component({
  selector: 'app-alert-section-detail',
  templateUrl: './alert-section-detail.component.html',
  styleUrls: ['./alert-section-detail.component.scss'],
  animations: [
    trigger('toggleActionPanel', [
      state('close', style({
        transform: 'scale(0)'
      })),
      state('open', style({
        transform: 'scale(1)'
      })),
      transition('close => open', animate(200)),
      transition('open => close', animate(200))
    ])
  ]
})
export class AlertSectionDetailComponent implements OnInit, OnChanges {

  @Input() sectionRiskAlert;

  state = 'close';

  policeState = 'on';
  warningState = 'on';

  actionSelected = -1;

  incidents;

  constructor() {
  }

  ngOnInit() {
    this.state = 'close';
  }

  onActionClick() {

    if (this.state === 'close') {
      this.state = 'open';
    } else {
      this.state = 'close';
    }
  }

  onActionSelect(id) {
    this.actionSelected = id;
    this.onActionClick();
  }


  ngOnChanges(changes: SimpleChanges): void {
    this.state = 'close';
  }
}
