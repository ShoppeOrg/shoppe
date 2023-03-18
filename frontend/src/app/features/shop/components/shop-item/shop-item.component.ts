import { Component, OnInit } from '@angular/core';
import { IconsService } from 'src/app/shared/services/icons.service';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
@Component({
  selector: 'app-shop-item',
  templateUrl: './shop-item.component.html',
  styleUrls: ['./shop-item.component.scss'],
  
  
})

export class ShopItemComponent implements OnInit {

  
  public form: FormGroup;

  constructor(private fb: FormBuilder,private readonly iconService: IconsService){
    this.iconService.addIcons();
    this.form = this.fb.group({
      rating: [3.5, Validators.required],
    })
  }

  ngOnInit(): void {
  }
}


