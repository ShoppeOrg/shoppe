import { Component, OnInit, Input } from '@angular/core';

import { IShopItem } from '../../../../shared/interfaces/IShopItem';
import { CartService } from '../../../../shared/services/cart.service';

@Component({
  selector: 'app-cart-item',
  templateUrl: './cart-item.component.html',
  styleUrls: ['./cart-item.component.scss'],
})
export class CartItemComponent implements OnInit {
  @Input() cartItem!: IShopItem;
  constructor(private cartService: CartService) {}

  ngOnInit(): void {}

  removeFromCart() {
    this.cartService.removeShopItem(this.cartItem);
  }
}
