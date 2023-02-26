import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

@Injectable({ providedIn: 'root'})
export class SpinnerService {
  private visibilitySubject = new BehaviorSubject(false);
  public visibility$ = this.visibilitySubject.asObservable();


  show() {
    this.visibilitySubject.next(true);
  }

  hide() {
    this.visibilitySubject.next(false);
  }
}
