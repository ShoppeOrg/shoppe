import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { MatSnackBar } from '@angular/material/snack-bar';

import { AuthService } from '../../services/auth.service';
import { patterns} from '../../../../shared/regexPatterns/patterns';
import { IFormData } from '../../interfaces/IFormData';
import { AuthModalComponent } from '../../modals/auth-modal/auth-modal.component';

@Component({
  selector: 'app-login-form',
  templateUrl: './login-form.component.html',
  styleUrls: ['./login-form.component.scss']
})
export class LoginFormComponent implements OnInit {
  emailPattern = patterns.regexEmail;
  name = 'email';
  placeholder = 'Email';

  constructor(
    private http: HttpClient,
    private authService: AuthService,
    private snackBar: MatSnackBar
  ) {}

  ngOnInit(): void {}

  onSubmit(formValue: IFormData): void {
    const email = formValue[this.name];
    this.authService.login(email).subscribe({
      next: () => {
        this.authService.openModal(AuthModalComponent, email);
      },
      error: err => {
        this.snackBar.open(err, 'Close', { duration: 5000 });
      }
    });
  }
}
