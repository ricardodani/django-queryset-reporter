import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';

@Injectable()
export class QuerysetService {

  constructor(private http: HttpClient) {}

  list() {
    return this.http.get(`/api/querysets/`);
  }

  query(querysetId: number, filters: object) {
    return this.http.get(`/api/querysets/${querysetId}/results/`);
  }
}
