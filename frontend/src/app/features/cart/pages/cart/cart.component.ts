import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ActivatedRoute } from '@angular/router';

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

  constructor(
    private cartService: CartService,
    private router: Router,
    private route: ActivatedRoute,
  ) {}

  ngOnInit(): void {
    this.cartService.loadCart();
    this.getCartItems();
  }

  getCartItems(): void {
    this.cartItems = this.cartService.getProducts();
    this.prevCartItems = JSON.parse(JSON.stringify(this.cartItems));
  }

  get total(): number {
    return this.cartService.getTotal();
  }

  arraysAreIdentical(arr1: IShopItem[], arr2: IShopItem[]): boolean {
    const originalJson = JSON.stringify(arr1);
    const modifiedJson = JSON.stringify(arr2);

    return originalJson === modifiedJson;
  }

  updateCart(): void {
    this.cartService.updateCart(this.cartItems);
    this.getCartItems();
  }

  checkout(): void {
    this.router.navigate(['checkout'], { relativeTo: this.route });
  }
}
