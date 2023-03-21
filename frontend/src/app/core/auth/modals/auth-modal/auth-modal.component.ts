import { Component, Inject, OnDestroy, OnInit } from '@angular/core';
import { MAT_DIALOG_DATA } from '@angular/material/dialog';

import { patterns } from '../../../../shared/regexPatterns/patterns';
import { IFormData } from '../../interfaces/IFormData';
import { AuthService } from '../../services/auth.service';
import { MatSnackBar } from '@angular/material/snack-bar';
import { Router } from '@angular/router';
import { Subject, takeUntil } from 'rxjs';

@Component({
  selector: 'app-auth-modal',
  templateUrl: './auth-modal.component.html',
  styleUrls: ['./auth-modal.component.scss']
})
export class AuthModalComponent implements OnInit, OnDestroy {
  codePattern = patterns.regexCode;
  name = 'code';
  placeholder = 'Code';
  onDestroy$ = new Subject<boolean>();

  constructor(
    @Inject(MAT_DIALOG_DATA) readonly data: { email: string },
    private authService: AuthService,
    private snackBar: MatSnackBar,
    private router: Router
  ) {}

  ngOnInit(): void {}

  onSubmit(formValue: IFormData): void {
    const token = formValue[this.name];

    this.authService
      .verifyCode({ token, email: this.data.email })
      .pipe(takeUntil(this.onDestroy$))
      .subscribe({
        next: () => {
          this.authService.closeModal();
          this.router.navigate(['my-profile']);
        },
        error: err => {
          this.snackBar.open(err, 'Close', { duration: 5000 });
        }
      });
  }

  ngOnDestroy() {
    this.onDestroy$.next(true);
    this.onDestroy$.unsubscribe();
  }
}
