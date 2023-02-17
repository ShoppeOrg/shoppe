import { Injectable } from '@angular/core';
import { CanMatch, UrlTree, Route, UrlSegment,  } from '@angular/router';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AuthGuard implements CanMatch {
  canMatch(
    route: Route,
    segments: UrlSegment[]
  ): Observable<boolean | UrlTree> | Promise<boolean | UrlTree> | boolean | UrlTree {
    return false;
  }


}
