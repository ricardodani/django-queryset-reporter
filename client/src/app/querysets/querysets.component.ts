import { Component, OnInit } from '@angular/core';
import { formatDate } from '@angular/common';
import { QuerysetService } from '../services/queryset.service'

@Component({
  selector: 'app-querysets',
  templateUrl: './querysets.component.html',
  styleUrls: ['./querysets.component.scss']
})
export class QuerysetsComponent implements OnInit {

  public querysets;
  public loadingQuerysets: boolean = false;

  constructor(private _querysetService: QuerysetService) { }

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

  getQuerysets = () => {
    this.loadingQuerysets = true;
    this._querysetService.list().subscribe(
      this._handleQuerysets,
      this._handleError,
      this._handleConcluded,
    );
  }

  _handleDeleteQueryset = (result) => {
    console.log(result);
    // this.setAlert('success', 'Removido com sucesso.');
    this.getQuerysets();
  }

  deleteQueryset(querysetId: number, popOver: any) {
    this._querysetService.delete(querysetId).subscribe(
      this._handleDeleteQueryset,
      this._handleError,
      () => {
        this._handleConcluded();
        popOver.close();
      }
    )
  }

  addThenEdit() {
  }

}
