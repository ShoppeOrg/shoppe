import { Component, OnInit } from '@angular/core';

import { CartService } from '../../../../shared/services/cart.service';
import { IShopItem } from '../../../../shared/interfaces/IShopItem';

@Component({
  selector: 'app-cart',
  templateUrl: './cart.component.html',
  styleUrls: ['./cart.component.scss'],
})
export class CartComponent implements OnInit {
  cartItems: Array<IShopItem> = [];
  prevCartItems: Array<IShopItem> = [];

  constructor(private cartService: CartService) {}

  ngOnInit(): void {
    this.cartService.loadCart();
    this.cartItems = this.cartService.getProducts();
    this.prevCartItems = JSON.parse(JSON.stringify(this.cartItems));
  }

  get total() {
    return this.cartItems.reduce(
      (sum, product) => ({
        quantity: 1,
        price: sum.price + product.amount * +product.price,
      }),
      { quantity: 1, price: 0 },
    ).price;
  }

  arraysAreIdentical(arr1: IShopItem[], arr2: IShopItem[]): boolean {
    const originalJson = JSON.stringify(arr1);
    const modifiedJson = JSON.stringify(arr2);

    return originalJson === modifiedJson;
  }

  updateCart(): void {
    this.cartService.updateCart(this.cartItems);
  }
}
