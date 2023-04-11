import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

import { IconsService } from '../../../../shared/services/icons.service';
import { ActivatedRoute } from '@angular/router';
import { ShopService } from '../../services/shop.service';
import { IShopItem } from '../../../../shared/interfaces/IShopItem';
import { Observable, tap } from 'rxjs';
import { CartService } from '../../../../shared/services/cart.service';
import { IShopData } from '../../../../shared/interfaces/IShopData';

@Component({
  selector: 'app-shop-details',
  templateUrl: './shop-details.component.html',
  styleUrls: ['./shop-details.component.scss'],
})
export class ShopDetailsComponent implements OnInit {
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
