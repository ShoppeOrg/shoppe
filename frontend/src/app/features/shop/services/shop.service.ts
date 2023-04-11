import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { catchError, Observable, throwError } from 'rxjs';

import { IShopData } from '../../../shared/interfaces/IShopData';
import { IQuery } from '../interfaces/IQuery';
import { environment } from '../../../../environments/environment';
import { IShopItem } from '../../../shared/interfaces/IShopItem';

@Injectable({
  providedIn: 'root',
})
export class ShopService {
  constructor(private http: HttpClient) {}

  getProducts(query: IQuery): Observable<IShopData> {
    const params = { ...query };
    return this.http
      .get<IShopData>(`${environment.api}/products/`, { params })
      .pipe(
        catchError(() => {
          let errorMessage = 'An unknown error occurred!';
          return throwError(() => errorMessage);
        }),
      );
  }

  getProduct(id: string): Observable<IShopItem> {
    return this.http.get<IShopItem>(`${environment.api}/products/${id}`).pipe(
      catchError(() => {
        let errorMessage = 'An unknown error occurred!';
        return throwError(() => errorMessage);
      }),
    );
  }

  getSimilarItems(id: string): Observable<IShopData> {
    const params = { id };
    return this.http
      .get<IShopData>(`${environment.api}/products/related/`, { params })
      .pipe(
        catchError(() => {
          let errorMessage = 'An unknown error occurred!';
          return throwError(() => errorMessage);
        }),
      );
  }
}
