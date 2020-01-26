import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { ResultsComponent } from './results/results.component'
import { QuerysetsComponent } from './querysets/querysets.component'
import { QuerysetComponent } from './queryset/queryset.component'


const routes: Routes = [
  { path: '', component: ResultsComponent },
  { path: 'querysets', component: QuerysetsComponent },
  { path: 'querysets/add', component: QuerysetComponent },
  { path: 'querysets/:id', component: QuerysetComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes, { useHash: true })],
  exports: [RouterModule]
})
export class AppRoutingModule { }
