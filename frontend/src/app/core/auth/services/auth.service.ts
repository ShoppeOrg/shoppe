import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { catchError, Observable, tap, throwError } from 'rxjs';
import { MatDialog, MatDialogConfig, MatDialogRef } from '@angular/material/dialog';
import { ComponentType } from '@angular/cdk/overlay';
import { CookieService } from 'ngx-cookie-service';

import { environment } from '../../../../environments/environment';
import { modalWidth, modalHeight } from '../../../shared/constants';
import { ICodeData } from '../interfaces/ICodeData';
import { IToken } from '../interfaces/IToken';
import { AuthModalComponent } from '../modals/auth-modal/auth-modal.component';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  constructor(
    private http: HttpClient,
    private dialog: MatDialog,
    private cookieService: CookieService
  ) {}

  login(email: string): Observable<void> {
    return this.http.post<void>(`${environment.api}/auth/email/`, { email }).pipe(
      catchError((err: HttpErrorResponse) => {
        let errorMessage = 'An unknown error occurred!';
        if (!err.error || !err.error.email) {
          return throwError(() => errorMessage);
        }
        switch (err.error.email[0]) {
          case 'Enter a valid email address.':
            errorMessage = 'Please, enter a valid email';
            break;
          case 'This field may not be blank.':
            errorMessage = 'This field must not be empty';
        }
        return throwError(() => errorMessage);
      })
    );
  }

  verifyCode(codeData: ICodeData): Observable<IToken> {
    return this.http.post<IToken>(`${environment.api}/auth/token/`, codeData).pipe(
      catchError((err: HttpErrorResponse) => {
        let errorMessage = 'An unknown error occurred!';
        if (!err.error || !err.error.token) {
          return throwError(() => errorMessage);
        }
        switch (err.error.token[0]) {
          case 'Invalid Token':
            errorMessage = 'Please enter code in number format ';
            break;
          case "The token you entered isn't valid.":
            errorMessage = 'Code you have entered is not valid';
        }
        return throwError(() => errorMessage);
      }),
      tap((data: IToken) => {
        this.setToken(data.token);
      })
    );
  }

  private setToken(token: string): void {
    this.cookieService.deleteAll();
    this.cookieService.set('auth-token', token);
  }

  openModal(
    component: ComponentType<AuthModalComponent>,
    email: string
  ): MatDialogRef<AuthModalComponent> {
    const modalConfig = new MatDialogConfig();
    modalConfig.autoFocus = false;
    modalConfig.width = modalWidth.xs;
    modalConfig.height = modalHeight.s;
    modalConfig.data = { email };
    return this.dialog.open(component, modalConfig);
  }

  closeModal(): void {
    this.dialog.closeAll();
  }
}
