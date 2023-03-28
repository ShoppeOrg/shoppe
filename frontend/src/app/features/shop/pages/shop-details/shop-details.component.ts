import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

import { ThemePalette } from "@angular/material/core";


import { IconsService } from '../../../../shared/services/icons.service';
import { ActivatedRoute } from '@angular/router';
import { ShopService } from '../../services/shop.service';
import { IShopItem } from '../../interfaces/IShopItem';
import { Observable } from 'rxjs';
import { OwlOptions } from 'ngx-owl-carousel-o';

type Rating = {
  value: number;
  max: number;
  color?: ThemePalette;
  disabled?: boolean;
  dense?: boolean;
  readonly?: boolean;
};

@Component({
  selector: 'app-shop-details',
  templateUrl: './shop-details.component.html',
  styleUrls: ['./shop-details.component.scss'],
})

  
export class ShopDetailsComponent implements OnInit {

  ratings: Rating[] = [

    {
      value: 3,
      max: 5,
      readonly: true,
    },
  ];

customOptions: OwlOptions = {
    loop: true,
    mouseDrag: true,
    touchDrag: false,
    pullDrag: false,
    dots: true,
    navSpeed: 700,
    navText: ['', ''],
   
  items: 1,
  margin: 16,

      
    nav: false
  }


  public form: FormGroup;

  shopItem!: Observable<IShopItem>;

  constructor(
    private fb: FormBuilder,
    private readonly iconService: IconsService,
    private route: ActivatedRoute,
    private shopService: ShopService,
  ) {
    this.iconService.addIcons();
    this.form = this.fb.group({
      rating: [3.5, Validators.required],
    });

    this.route.params.subscribe(() => {
      const id = this.route.snapshot.paramMap.get('id');
      if (!!id) {
        this.shopItem = this.shopService.getProduct(id);
      }
    });
  }
  ngOnInit(): void {}
}
