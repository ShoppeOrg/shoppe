import { Component, Input, OnInit } from '@angular/core';

import { IShopItem } from '../../../../shared/interfaces/IShopItem';

@Component({
  selector: 'app-shop-item',
  templateUrl: './shop-item.component.html',
  styleUrls: ['./shop-item.component.scss']
})
export class ShopItemComponent implements OnInit {
  @Input() productItem!: IShopItem;

  constructor() {}

  ngOnInit(): void {}
}
