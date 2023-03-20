import { Component, EventEmitter, Input, OnInit, Output, ViewChild } from '@angular/core';
import { AbstractControl, FormControl, FormGroup, NgForm, Validators } from '@angular/forms';

import { IFormData } from '../../interfaces/IFormData';

@Component({
  selector: 'app-custom-form',
  templateUrl: './custom-form.component.html',
  styleUrls: ['./custom-form.component.scss']
})
export class CustomFormComponent implements OnInit {
  @ViewChild('formDirective') private formDirective!: NgForm;

  @Input() name!: string;
  @Input() placeholder!: string;
  @Input() pattern!: RegExp ;
  @Input() formAction!: string;
  @Output() formSubmit = new EventEmitter<IFormData>();

  customForm!: FormGroup;

  constructor() {}

  ngOnInit() {
    this.customForm = new FormGroup({
      [this.name]: new FormControl('', [Validators.required, Validators.pattern(this.pattern)])
    });
  }

  onSubmit(): void {
    if (!this.customForm.valid) {
      return;
    }
    this.formSubmit.emit(this.customForm.value);
    this.formDirective.resetForm();
  }

  get field() {
    return this.customForm.get(this.name);
  }
}
