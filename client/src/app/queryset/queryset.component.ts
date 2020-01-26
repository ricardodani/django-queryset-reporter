import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { QuerysetService } from '../services/queryset.service';
import { Queryset, Model } from '../models/queryset';
import { Validators } from '@angular/forms';
import { FormBuilder } from '@angular/forms';

@Component({
  selector: 'app-queryset',
  templateUrl: './queryset.component.html',
  styleUrls: ['./queryset.component.scss']
})
export class QuerysetComponent implements OnInit {

  queryset: Queryset;
  loading: boolean = false;
  querysetForm = this.formBuilder.group({
    name: ['', Validators.required],
    model: [''],
    distinct: ['']
  });
  models: Model[];

  constructor(
    private querysetService: QuerysetService,
    private actRoute: ActivatedRoute,
    private formBuilder: FormBuilder
  ) {}

  ngOnInit() {
    this.getQueryset();
    this.getModels();
    // this.querysetService.get()
  }

  private handleQueryset = (queryset: Queryset) => {
    this.queryset = queryset;
    this.querysetForm.patchValue(this.queryset.getFormData());
  }

  private handleError = (error) => {
    console.warn(error);
  }

  private handleConcluded = () => {
    this.loading = false;
  }

  getQuerysetId = () => {
    return parseInt(
      this.actRoute.snapshot.paramMap.get('id')
    );
  }

  getQueryset() {
    this.loading = true;
    this.querysetService.retrieve(this.getQuerysetId()).subscribe(
      this.handleQueryset,
      this.handleError,
      this.handleConcluded
    );
  }

  private handleModels = (models: Model[]) => {
    this.models = models;
  }

  getModels() {
    this.loading = true;
    this.querysetService.getModels().subscribe(
      this.handleModels,
      this.handleError,
      this.handleConcluded
    );
  }

  onSubmit() {
    console.warn(this.querysetForm.value);
  }



}
