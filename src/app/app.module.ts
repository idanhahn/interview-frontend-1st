import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';
import {FormsModule} from '@angular/forms';
import {HttpModule} from '@angular/http';

import {AppComponent} from './app.component';
import {MainComponent} from './main/main.component';
import {MapComponent} from './map/map.component';
import {HeaderComponent} from './header/header.component';
import {RouterModule} from '@angular/router';
import {AgmCoreModule} from 'angular2-google-maps/core';
import {firebaseConfig, googleConfig} from './config/config';
import {PanelComponent} from './panel/panel.component';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';
import {InfoCardComponent} from './info-card/info-card.component';
import {MonitorComponent} from './monitor/monitor.component';
import {ModeSwitcherComponent} from './mode-switcher/mode-switcher.component';
import {MainService} from './services/main.service';
import {RoadIncidentService} from './services/road-incident.service';
import {CrashService} from './services/crash.service';
import {EventService} from './services/event.service';
import {SectionService} from './services/section.service';
import {AngularFireModule} from 'angularfire2';
import {AngularFireDatabaseModule} from 'angularfire2/database';
import {CfgService} from './services/cfg.service';
import { PanelListComponent } from './panel-list/panel-list.component';
import { PanelDetailComponent } from './panel-detail/panel-detail.component';
import { IncidentCardComponent } from './incident-card/incident-card.component';
import { PlanComponent } from './plan/plan.component';
import { AnalyzeComponent } from './analyze/analyze.component';
import { AlertListComponent } from './alert-list/alert-list.component';
import { OngoingListComponent } from './ongoing-list/ongoing-list.component';
import { OngoingListItemComponent } from './ongoing-list-item/ongoing-list-item.component';
import { AlertSectionDetailComponent } from './alert-section-detail/alert-section-detail.component';
import { AlertIncidentDetailComponent } from './alert-incident-detail/alert-incident-detail.component';
import { AlertIncidentItemComponent } from './alert-incident-item/alert-incident-item.component';
import { AlertSectionItemComponent } from './alert-section-item/alert-section-item.component';
import {RiskAlertsService} from './services/risk-alerts.service';
import {OngoingService} from './services/ongoing.service';
import { OngoingSectionDetailComponent } from './ongoing-section-detail/ongoing-section-detail.component';
import {MapService} from './services/map.service';
import { MapFranticComponent } from './map-frantic/map-frantic.component';
import { PlanMapComponent } from './plan-map/plan-map.component';
import { PlanPanelComponent } from './plan-panel/plan-panel.component';
import 'hammerjs';
import {MdSliderModule} from '@angular/material';
import { PlanPanelListComponent } from './plan-panel-list/plan-panel-list.component';
import { PlanShiftComponent } from './plan-shift/plan-shift.component';
import {PlanService} from './services/plan.service';
import { IncidentCard1Component } from './incident-card-1/incident-card-1.component';
import { MapMoreComponent } from './map-more/map-more.component';
import { AddIncidentPanelComponent } from './add-incident-panel/add-incident-panel.component';
import { SafePipe } from './pipes/safe.pipe';

@NgModule({
  declarations: [
    AppComponent,
    MainComponent,
    MapComponent,
    HeaderComponent,
    PanelComponent,
    InfoCardComponent,
    MonitorComponent,
    ModeSwitcherComponent,
    PanelListComponent,
    PanelDetailComponent,
    IncidentCardComponent,
    PlanComponent,
    AnalyzeComponent,
    AlertListComponent,
    OngoingListComponent,
    OngoingListItemComponent,
    AlertSectionDetailComponent,
    AlertIncidentDetailComponent,
    AlertIncidentItemComponent,
    AlertSectionItemComponent,
    OngoingSectionDetailComponent,
    MapFranticComponent,
    PlanMapComponent,
    PlanPanelComponent,
    PlanPanelListComponent,
    PlanShiftComponent,
    IncidentCard1Component,
    MapMoreComponent,
    AddIncidentPanelComponent,
    SafePipe
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule,
    BrowserAnimationsModule,
    MdSliderModule,
    AngularFireModule.initializeApp(firebaseConfig),
    AngularFireDatabaseModule,
    AgmCoreModule.forRoot({
      apiKey: googleConfig.apiKey
    }),
    RouterModule.forRoot([
      {path: '', component: MainComponent},
      {path: 'plan', component: PlanComponent},
      {path: 'analyze', component: AnalyzeComponent}
    ])
  ],
  providers: [
    MainService,
    SectionService,
    RoadIncidentService,
    CrashService,
    EventService,
    RiskAlertsService,
    OngoingService,
    CfgService,
    PlanService,
    MapService
  ],
  bootstrap: [AppComponent]
})
export class AppModule {
}
