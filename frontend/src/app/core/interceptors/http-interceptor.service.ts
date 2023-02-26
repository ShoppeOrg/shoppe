import {
  HttpInterceptor,
  HttpRequest,
  HttpHandler,
  HttpEvent,
  HttpHeaders
} from '@angular/common/http';
import { Injectable } from '@angular/core';
import { finalize, Observable } from 'rxjs';
import { CookieService } from 'ngx-cookie-service';

import { SpinnerService } from '../../shared/services/spinner.service';

@Injectable()
export class HttpInterceptorService implements HttpInterceptor {
  constructor(private spinnerService: SpinnerService, private cookieService: CookieService) {}

  intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    this.spinnerService.show();

    const userToken: string = this.cookieService.get('auth-token');

    const headers = new HttpHeaders({
      Accept: 'application/json',
      Authorization: userToken ? `Token ${userToken}` : ''
    });

    const modifiedReq = req.clone({ headers });

    return next.handle(modifiedReq).pipe(finalize(() => this.spinnerService.hide()));
  }
}
