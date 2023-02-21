import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { FormControl, FormGroup, NgForm, Validators } from '@angular/forms';
import { AuthService } from '../../services/auth.service';

@Component({
  selector: 'app-login-form',
  templateUrl: './login-form.component.html',
  styleUrls: ['./login-form.component.scss']
})
export class LoginFormComponent implements OnInit {
  signupForm: FormGroup;

  constructor(private http: HttpClient, private authService: AuthService) {
    this.signupForm = new FormGroup({
      email: new FormControl('', [Validators.required, Validators.email])
    });
  }

  ngOnInit(): void {}

  onSubmit(authForm: NgForm) {
    if (!authForm.valid) {
      return;
    }

    const email = authForm.value.email;

    this.authService.login(email);

    // console.log('form', this.signupForm.value.email);
    // return this.http
    //   .post('http://127.0.0.1:8000/auth/email/', { email:this.signupForm.value.email })
    //   .subscribe(res => {
    //     console.log('res', res);
    //   });
  }

  loginHandler() {
    return this.http
      .post('http://127.0.0.1:8000/auth/token/', {
        email: 'tyrpuchy0611@gmail.com',
        token: '219142'
      })
      .subscribe(res => {
        console.log('res', res);
      });
  }
}
