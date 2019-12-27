import { Component, OnInit } from '@angular/core';
import { QuerysetService } from '../services/queryset.service'

@Component({
  selector: 'app-results',
  templateUrl: './results.component.html',
  styleUrls: ['./results.component.scss']
})
export class ResultsComponent implements OnInit {
  public querysets;
  public querysetResponse;
  public selectedQueryset;
  public filtersResponse;
  public loadingQuerysets: boolean = false;
  public loadingQueryset: boolean = false;
  public loadingFilters: boolean = false;

  constructor(private _querysetService: QuerysetService) {}

  ngOnInit() {
    this.getQuerysets();
  }

  _handleQuerysets = (querysets) => {
    this.querysets = querysets;
  }

  _handleError(err) {
    console.error(err);
  }

  _handleConcluded = () => {
    this.loadingQuerysets = false;
  }

  _handleQuerysetConcluded = () => {
    this.loadingQueryset = false;
  }

  _handleFiltersConcluded = () => {
    this.loadingFilters = false;
  }

  getQuerysets = () => {
    this.loadingQuerysets = true;
    this._querysetService.list().subscribe(
      this._handleQuerysets,
      this._handleError,
      this._handleConcluded,
    );
  }

  onQuerysetChange = () => {
    this.getQueryset(this.selectedQueryset.id);
  }

  _handleQuery = (querysetResponse) => {
    console.log(querysetResponse);
    this.querysetResponse = querysetResponse;
  }

  _handleFilters = (filtersResponse) => {
    console.log(filtersResponse)
    this.filtersResponse = filtersResponse;
  }

  getQueryset = (querysetId) => {
    this.loadingQueryset = true;
    this._querysetService.query(querysetId, {}).subscribe(
      this._handleQuery,
      this._handleError,
      this._handleQuerysetConcluded
    );
    this.loadingFilters = true;
    this._querysetService.getFilters(querysetId).subscribe(
      this._handleFilters,
      this._handleError,
      this._handleFiltersConcluded,
    );
  }

}
