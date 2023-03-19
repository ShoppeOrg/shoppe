import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { IconsService } from '../../../../shared/services/icons.service';

@Component({
  selector: 'app-shop-details',
  templateUrl: './shop-details.component.html',
  styleUrls: ['./shop-details.component.scss']
})
export class ShopDetailsComponent implements OnInit {
  public form: FormGroup;

  constructor(private fb: FormBuilder, private readonly iconService: IconsService) {
    this.iconService.addIcons();
    this.form = this.fb.group({
      rating: [3.5, Validators.required]
    });
  }
  ngOnInit(): void {}
}
