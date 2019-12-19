import { Component, OnInit } from '@angular/core';
import { QuerysetService } from '../services/queryset.service'
import { Router, ActivateRoute, ParamMap } from '@angular/router';
import { switchMap } from 'rxjs/operators';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
})
export class AppComponent implements OnInit {

  public loadingQueryset: boolean = false;

  constructor(
    private _querysetService: QuerysetService,
    private _route: ActivatedRoute,
    private _router: Router
  ) { }

  ngOnInit() {
    this.queryset = this.route.paramMap.pipe(
      switchMap(this._mapInitParams)
    );
  }

  _mapInitParams = (params: ParamMap) => {
    return this.getQueryset(params.get('id'));
  }

  _handleQuerysets = (queryset) => {
    this.queryset = queryset;
  }

  _handleError(err) {
    console.error(err);
  }

  _handleConcluded = () => {
    this.loadingQueryset = false;
  }

  getQueryset = (querysetId: number) => {
    this.loadingQueryset = true;
    this._querysetService.get(querysetId).subscribe(
      this._handleQueryset,
      this._handleError,
      this._handleConcluded,
    )
  }
}
