import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';
import { IQuery } from '../interfaces/IQuery';

@Injectable({
  providedIn: 'root',
})
export class FilterShopService {
  initialQuery: IQuery = {
    page: 1,
    page_size: 21,
    filterChanged: false
  };
  productsSubject = new BehaviorSubject(this.initialQuery);

  constructor() {}

  setQuery(query: IQuery): void {
    this.productsSubject.next({ ...this.getQuery(), ...query });
  }

  getQuery(): IQuery {
    return this.productsSubject.getValue();
  }
}
