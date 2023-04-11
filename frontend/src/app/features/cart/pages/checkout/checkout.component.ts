import { Component, OnInit } from '@angular/core';

import { CartService } from '../../../../shared/services/cart.service';
import { IShopItem } from '../../../../shared/interfaces/IShopItem';

@Component({
  selector: 'app-checkout',
  templateUrl: './checkout.component.html',
  styleUrls: ['./checkout.component.scss'],
})
export class CheckoutComponent implements OnInit {
  cartItems: Array<IShopItem> = [];
  constructor(private cartService: CartService) {}

  ngOnInit(): void {
    this.cartService.loadCart();
    this.getCartItems();
  }

  getCartItems(): void {
    this.cartItems = this.cartService.getProducts();
  }

  get total(): number {
    return this.cartService.getTotal();
  }
}
