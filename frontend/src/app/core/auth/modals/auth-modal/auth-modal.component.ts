import { Component, Inject, OnInit } from '@angular/core';
import { MAT_DIALOG_DATA } from '@angular/material/dialog';

import { patterns } from '../../../../shared/regexPatterns/patterns';
import { IFormData } from '../../interfaces/IFormData';
import { AuthService } from '../../services/auth.service';
import { MatSnackBar } from '@angular/material/snack-bar';
import { Router } from '@angular/router';

@Component({
  selector: 'app-auth-modal',
  templateUrl: './auth-modal.component.html',
  styleUrls: ['./auth-modal.component.scss']
})
export class AuthModalComponent implements OnInit {
  codePattern = patterns.regexCode;
  name = 'code';
  placeholder = 'Code';

  constructor(
    @Inject(MAT_DIALOG_DATA) readonly data: { email: string },
    private authService: AuthService,
    private snackBar: MatSnackBar,
    private router: Router
  ) {}

  ngOnInit(): void {}

  onSubmit(formValue: IFormData): void {
    const token = formValue[this.name];

    this.authService.verifyCode({ token, email: this.data.email }).subscribe({
      next: () => {
        this.authService.closeModal();
        this.router.navigate(['my-profile']);
      },
      error: err => {
        this.snackBar.open(err, 'Close', { duration: 5000 });
      }
    });
  }
}
