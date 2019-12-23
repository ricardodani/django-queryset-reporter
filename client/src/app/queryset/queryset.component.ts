import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { QuerysetService } from '../services/queryset.service'

@Component({
  selector: 'app-queryset',
  templateUrl: './queryset.component.html',
  styleUrls: ['./queryset.component.scss']
})
export class QuerysetComponent implements OnInit {

  public queryset;

  constructor(
    private _querysetService: QuerysetService,
    private _route: ActivatedRoute
  ) {}

  ngOnInit() {
    console.log(this._route);
  }

}
