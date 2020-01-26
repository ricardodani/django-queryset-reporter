import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule, HttpClientXsrfModule } from '@angular/common/http';
import { APP_BASE_HREF } from '@angular/common';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap'

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NavbarComponent } from './navbar/navbar.component';
import { QuerysetService } from './services/queryset.service';
import { ResultsComponent } from './results/results.component'
import { QuerysetsComponent } from './querysets/querysets.component'
import { QuerysetComponent } from './queryset/queryset.component'


@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    ResultsComponent,
    QuerysetsComponent,
    QuerysetComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    HttpClientXsrfModule.withOptions({
      cookieName: 'csrftoken', headerName: 'X-CSRFToken'
    }),
    NgbModule,
    FormsModule,
    ReactiveFormsModule
  ],
  providers: [
    QuerysetService,
  ],
  bootstrap: [ AppComponent ]
})
export class AppModule { }
