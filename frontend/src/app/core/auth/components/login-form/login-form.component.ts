import { Component, OnInit } from '@angular/core';

import { FormControl, FormGroup } from '@angular/forms';

@Component({
  selector: 'app-login-form',
  templateUrl: './login-form.component.html',
  styleUrls: ['./login-form.component.scss']
})
export class LoginFormComponent implements OnInit {
  signupForm: FormGroup;

  constructor() {
    this.signupForm = new FormGroup({
      email: new FormControl(null)
    });
  }

  ngOnInit(): void {}

  onSubmit() {
    console.log('form', this.signupForm);
  }
}
