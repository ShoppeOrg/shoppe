import { Injectable } from '@angular/core';

import { environment } from '../../../../environments/environment';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  constructor(private http: HttpClient) {}

  login(email: string) {
    return this.http.post(`${environment.api}/auth/email`, { email }).subscribe(data => {
      console.log('data',data);
    });
  }
}
