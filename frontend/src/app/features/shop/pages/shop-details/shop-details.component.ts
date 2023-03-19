import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

import { IconsService } from '../../../../shared/services/icons.service';
import { ActivatedRoute } from '@angular/router';
import { ShopService } from '../../services/shop.service';
import { IShopItem } from '../../interfaces/IShopItem';

@Component({
  selector: 'app-shop-details',
  templateUrl: './shop-details.component.html',
  styleUrls: ['./shop-details.component.scss'],
})
export class ShopDetailsComponent implements OnInit {
  public form: FormGroup;

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
        this.shopService.getProduct(+id).subscribe((shopItem: IShopItem) => {
          console.log('shopItem', shopItem);
        });
      }
    });
  }
  ngOnInit(): void {}
}
