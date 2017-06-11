import {Component, Input, OnInit} from '@angular/core';
import {MainService} from '../services/main.service';
import {DomSanitizer} from '@angular/platform-browser';

@Component({
  selector: 'app-alert-incident-detail',
  templateUrl: './alert-incident-detail.component.html',
  styleUrls: ['./alert-incident-detail.component.scss']
})
export class AlertIncidentDetailComponent implements OnInit {

  @Input() incidentRiskAlert;

  incidents;

  constructor(private _ms: MainService, private sanitizer: DomSanitizer) {

  }

  ngOnInit() {
  }

  onActionClick() {
    console.log('implement');
  }


  videoURL() {
    console.log(this.incidentRiskAlert.alertVideo);
    return this.sanitizer.bypassSecurityTrustResourceUrl(this.incidentRiskAlert.alertVideo);
  }
}
