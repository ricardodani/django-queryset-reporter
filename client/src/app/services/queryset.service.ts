import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { map } from 'rxjs/operators';
import { Observable } from 'rxjs';
import { Queryset, Model } from '../models/queryset'

@Injectable()
export class QuerysetService {

  baseUrl: string = '/api/querysets/';

  constructor(private http: HttpClient) {}

  list() {
    return this.http.get<Queryset[]>(this.baseUrl).pipe(
      map(resultList => resultList.map(querysetJson => new Queryset(querysetJson)))
    );
  }

  add(queryset: Queryset): Observable<Queryset> {
    return this.http.post<Queryset>(this.baseUrl, queryset).pipe(
      map(querysetJson => new Queryset(querysetJson))
    );
  }

  retrieve(querysetId: number): Observable<Queryset> {
    return this.http.get<Queryset>(this.baseUrl + `${querysetId}/`).pipe(
      map(querysetJson => new Queryset(querysetJson))
    );
  }

  update(querysetId: number, body: Queryset) {
    return this.http.patch(this.baseUrl + `${querysetId}/`, body);
  }

  delete(querysetId: number) {
    return this.http.delete(this.baseUrl + `${querysetId}/`);
  }

  query(querysetId: number, filters: object) {
    return this.http.get(this.baseUrl + `${querysetId}/results/`);
  }

  getFilters(querysetId: number) {
    return this.http.get(this.baseUrl + `${querysetId}/filters/`);
  }

  getModels() {
    return this.http.get<Model[]>(this.baseUrl + `models/`).pipe(
      map(modelsJson => modelsJson.map(model => new Model(model)))
    );
  }

}
