import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ThemePalette } from '@angular/material/core';
import { OwlOptions } from 'ngx-owl-carousel-o';
import {Observable, tap} from 'rxjs';
import { ActivatedRoute } from '@angular/router';

import { IconsService } from '../../../../shared/services/icons.service';
import { ShopService } from '../../services/shop.service';
import { CartService } from '../../../../shared/services/cart.service';
import { IShopData } from '../../../../shared/interfaces/IShopData';
import { IShopItem } from '../../interfaces/IShopItem';

export  type Rating = {
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

    responsive: {
      0: {
        items: 1,
        margin: 16,
      },
      400: {
        items: 1,
      },
      740: {
        items: 1,
      },
      940: {
        items: 2,
      },
    },

    nav: false,
  };

  public form: FormGroup;
  similarItems$!: Observable<IShopData>;

  shopItem$!: Observable<IShopItem>;

  constructor(
    private fb: FormBuilder,
    private readonly iconService: IconsService,
    private route: ActivatedRoute,
    private shopService: ShopService,
    private cartService: CartService,
  ) {
    this.iconService.addIcons();
    this.form = this.fb.group({
      rating: [3.5, Validators.required],
    });

    this.route.params.subscribe(() => {
      const id = this.route.snapshot.paramMap.get('id');
      if (!!id) {
        this.shopItem$ = this.shopService
          .getProduct(id)
          .pipe(tap(item => (item.amount = 1)));

        this.similarItems$ = this.shopService.getSimilarItems(id);
      }
    });
  }
  ngOnInit(): void {}

  addToCart(shopItem: IShopItem): void {
    this.cartService.addToCart(shopItem);
  }
}
