import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';

@Injectable()
export class QuerysetService {

  private _baseUrl = "/api/querysets";

  constructor(private http: HttpClient) {}

  list() {
    return this.http.get(`${this._baseUrl}/`);
  }

  query(querysetId: number, filters: object) {
    return this.http.get(`${this._baseUrl}/${querysetId}/results/`);
  }

  getFilters(querysetId: number) {
    return this.http.get(`${this._baseUrl}/${querysetId}/filters/`);
  }

}
