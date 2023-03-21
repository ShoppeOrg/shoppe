import { Component, OnDestroy, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { MatSnackBar } from '@angular/material/snack-bar';

import { AuthService } from '../../services/auth.service';
import { patterns } from '../../../../shared/regexPatterns/patterns';
import { IFormData } from '../../interfaces/IFormData';
import { AuthModalComponent } from '../../modals/auth-modal/auth-modal.component';
import { Subject, Subscription, takeUntil } from 'rxjs';

@Component({
  selector: 'app-login-form',
  templateUrl: './login-form.component.html',
  styleUrls: ['./login-form.component.scss']
})
export class LoginFormComponent implements OnInit, OnDestroy {
  emailPattern = patterns.regexEmail;
  name = 'email';
  placeholder = 'Email';
  onDestroy$ = new Subject<boolean>();

  constructor(
    private http: HttpClient,
    private authService: AuthService,
    private snackBar: MatSnackBar
  ) {}

  ngOnInit(): void {}

  onSubmit(formValue: IFormData): void {
    const email = formValue[this.name];
    this.authService
      .login(email)
      .pipe(takeUntil(this.onDestroy$))
      .subscribe({
        next: () => {
          this.authService.openModal(AuthModalComponent, email);
        },
        error: err => {
          this.snackBar.open(err, 'Close', { duration: 5000 });
        }
      });
  }

  ngOnDestroy(): void {
    this.onDestroy$.next(true);
    this.onDestroy$.unsubscribe();
  }
}
